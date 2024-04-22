"Noten que el iframe es un árbol HTML dentro de el árbol HTML original"
from scrapy.item import Field, Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy import Request

class Dummy(Item):
    titulo = Field()
    titulo_iframe = Field()

class W3SCrawler(CrawlSpider):
    name = 'w3s'
    custom_settings = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        'REDIRECT_ENABLED': True  # Parametro para activar los redirects (codigo 302)
    }

    allowed_domains = ['w3schools.com']
    start_urls = ['https://www.w3schools.com/tags/tag_iframe.asp']

    download_delay = 2

    def parse(self, response):
        sel = Selector(response)
        titulo = sel.xpath('//div[@id="main"]//h1/span/text()')

        # Extraigo la informacion que me interesa de la pagina que tiene el iframe
        titulo = sel.xpath('//div[@id="main"]//h1/span/text()').get()
        # Armo un objeto con esta informacion
        previous_data = {
            'titulo': titulo
        }

        # Obtengo la URL del iframe
        iframe_url = sel.xpath('//div[@id="main"]//iframe[@width="99%"]/@src').get()
        # La naturaleza de esta web, me pide completar la URL del iframe con el dominio y el protocolo de la pagina
        iframe_url = "https://www.w3schools.com/html/" + iframe_url

        # Hago un request forzoso a la URL del iframe
        yield Request(
            iframe_url,  # url del iframe a la cual hare el requerimiento
            callback=self.parse_iframe,  # funcion dentro de la clase que va a procesar el iframe
            meta=previous_data
            # Debido a que el item no se puede cargar hasta que yo no tenga los datos que obtendre en el request al iframe, tengo que pasar los datos obtenidos en esta pagina, al siguiente request
        )

    # Funcion que llamara el callback al hacer el requerimiento a la URL del iframe
    # Este respone, tiene el ARBOL HTML de la pagina que estaba en el iframe.
    # Es decir, hago una extraccion normal y comun y corriente.
    def parse_iframe(self, response):
        item = ItemLoader(Dummy(), response)  # Ahora si voy a cargar el item
        item.add_xpath('titulo_iframe', '//div[@id="main"]//h1/span/text()')

        # Extraigo los datos obtenidos en la pagina que embebia al iframe a traves de la meta_data del request, que traspasamos al request del iframe en la linea 54.
        # Los cargo en el Item
        item.add_value('titulo', response.meta.get('titulo'))

        yield item.load_item()

# EJECUCION
# scrapy runspider w3s.py -o w3s.json