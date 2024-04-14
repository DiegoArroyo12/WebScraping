from scrapy.item import Field, Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

class Teclado(Item):
    nombre = Field()
    precio = Field()
    descripcion = Field()

class MercadoLibre(CrawlSpider):
    name = "Teclados"
    custom_settings = {
        'USER_AGENT': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        'CLOSESPIDER_PAGECOUNT': 20,  # Número de páginas a visitar de las cuales se descarga información antes de parar mi extracción.
        'FEED_EXPORT_FIELDS': ['nombre', 'precio'] # Hace que se exporten los campos en ese orden
    }
    start_urls = ['https://listado.mercadolibre.com.mx/teclado-mecanico-espa%C3%B1ol#filter']

    # Va a ser un rango entre 0.5 * download_delay y 1.5 * download_delay
    download_delay = 2

    # Lista de DOMINIOS a los cuales mi spider tiene permitido dirigirse. Si un dominio de una URL no se encuentra en esta lista, mi spider no irá a esta url.
    allowed_domains = ['www.mercadolibre.com.mx', 'articulo.mercadolibre.com.mx']

    rules = (
        # Paginación
        Rule(
            LinkExtractor(
                allow=r'/teclado-mecanico-español_Desde_'
            ), follow=True
        ),
        # Detalle de los productos
        Rule(
            LinkExtractor(
                allow=r'/MLM'  # /MLM- Hay que corregirlo y encontrar un patrón
            ), follow=True, callback="parse_teclado"
        ),
    )

    def limpiarTexto(self, texto):
        nuevoTexto = texto.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ').strip()
        return nuevoTexto

    def parse_teclado(self, response):
        item = ItemLoader(Teclado(), response)
        item.add_xpath('nombre','//h1/text()', MapCompose(self.limpiarTexto))
        item.add_xpath('precio','//div[@class="ui-pdp-price__second-line"]//span[@class="andes-money-amount__fraction"]/text()')
        item.add_xpath('descripcion','//p[@class="ui-pdp-description__content"]/text()', MapCompose(self.limpiarTexto))

        yield item.load_item()
