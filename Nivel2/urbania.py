from scrapy.item import Field, Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

"""
process_value: Yo pudiera definir process_value como una función que concatene mi URL: 
"https://urbania.pe/buscar/proyectos-propiedades?page="
con este numerito que extraeríamos del href del tag a podríamos armar la URL final.
"""
# Cuando tengamos problemas con la paginación, que no tenga las urls y que no podamos armarlas, hacemos que cada url de paginación sea una url semilla

class Departamentos(Item):
    nombre = Field()
    direccion = Field()

"""
WEB SCRAPING EN LA NUBE

Yo escribo el código en mi máquina y lo ejecuto a través de redes o servidores virtuales que poseen mecanismos sofisticados para evitar baneos 
y hacer extracciones lo más óptimamente posibles.
scrapinghub

Poxy

Es un servidor virtual que hace de intermediario entre los requerimientos que realizamos nosotros y la página que recibe los requerimientos.
Al hacer requerimientos a través de proxies, la página que recibe los requerimientos nunca sabe de nuestra existencia.

SE COBRA POR EL SERVICIO

Proxy Pool

Es una piscina donde existen un conjunto de Proxies. Cada uno es capaz de redirigir requerimientos con una IP diferente. Ideal para evitar baneos
al hacer Web Scraping.

Video Número 53
"""

class Urbanianpe(CrawlSpider):
    name = "Departamentos"
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'CLOSESPIDER_ITEMCOUNT': 24, 
        'DOWNLOADER_MIDDLEWARES': {'scrapy_crawlera.CrawleraMiddleware': 610}, # Crawlera: Ya no existe
        'DOWNLOADER_MIDDLEWARES': {'scrapy_zyte_smartproxy.ZyteSmartProxyMiddleware': 610}, # Zyte
        'CRAWLERA_ENABLED': True, # Crawlera: Ya no existe
        'ZYTE_SMARTPROXY_ENABLED': True, # Zyte
        'CRAWLERA_APIKEY': 'Llave Otorgada al comprar el servicio', # Crawlera
        'ZYTE_SMARTPROXY_APIKEY': 'Llave Otorgada al comprar el servicio' # Zyte
    }

    # Esta lista la podríamos armar dinámicamente con un lazo for, en el caso de que hablemos de docenas o cientos de páginas.
    start_urls = [
        'https://urbania.pe/buscar/proyectos-propiedades?page=1'
        'https://urbania.pe/buscar/proyectos-propiedades?page=2'
        'https://urbania.pe/buscar/proyectos-propiedades?page=3'
        'https://urbania.pe/buscar/proyectos-propiedades?page=4'
        'https://urbania.pe/buscar/proyectos-propiedades?page=5'
    ]

    allowed_domains = ['urbania.pe']

    rules = (
        Rule(
            LinkExtractor(
                allow=r'/proyecto-'
            ), follow=True, callback="parse_depa"
        ),
    )

    def parse_depa(self, response):
        sel = Selector(response)
        item = ItemLoader(Departamentos(), sel)

        item.add_xpath('nombre', '//h1[@class="title-h1-development"]/text()')
        item.add_xpath('direccion', '//h4[@id="ref-map"]/text()')

        yield item.load_item()