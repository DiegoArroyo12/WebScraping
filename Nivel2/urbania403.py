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

class Urbanianpe(CrawlSpider):
    name = "Departamentos"
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'CLOSESPIDER_ITEMCOUNT': 24
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

    download_delay = 1

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

"""
Estrategias en caso de 403:
1. Cambiar USER AGENT
2. Cambiarnos de red de internet
3. Cambiarnos de máquina
4. Deshabilitar los cookies (COOKIES_ENABLED: False, dentro de custom_settings)
5. Utilizar encabezados diferentes para emular a un navegador
"""