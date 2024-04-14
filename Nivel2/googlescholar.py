from scrapy.item import Field, Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

class Articulo(Item):
    titulo = Field()
    citaciones = Field()
    autores = Field()
    url = Field()

# CrawlSpider es para ir viajando a través de la página
# Spider es para hacer extracción de una sola URL
class GoogleScholar(CrawlSpider):
    name = 'googlescholar'
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'DEPTH_LIMIT': 1, # Límite de Profundidad: Detiene al scraper cuando la regla se ejecute las veces especificadas, en este caso 1
        'FEED_EXPORT_ENCODING': 'utf-8', # Hace que la extracción de acentos, ñ o caracteres especiales se extraigan correctamente
        'CONCURRENT_REQUESTS': 1
    }

    download_delay = 2

    start_urls = ['https://scholar.google.com/scholar?as_ylo=2023&q=AI&hl=en&as_sdt=0,5']

    allowed_domains = ['scholar.google.com']

    rules = (
        Rule(
            LinkExtractor(
                restrict_xpaths="//div[@class='gs_ri']",
                allow=r'\?cites=' # Los signos de interrogación simbolizan caracter especial (\?)
            ), follow=True, callback='parse_start_url'
        ),
    )

    """
    # Función para poder parsear la url semilla
    def parse_start_url(self, response, **kwargs):
        return super().parse_start_url(response, **kwargs)

    Para no copiar y pegar el mismo código en las dos funciones, lo que hacemos es nombrar a nuestra función parseadora para la url semilla
    y que también la llame el callback de nuestra regla.
    """

    def parse_start_url(self, response):
        sel = Selector(response)

        articulos = sel.xpath('//div[@class="gs_ri"]')

        for articulo in articulos:
            item = ItemLoader(Articulo(), articulo)
            
            # Lleva el punto porque la búsqueda es relativa al punto
            titulo = articulo.xpath('.//h3/a//text()').getall() # Con este método puedo preprocesar la información con Python
            titulo = "".join(titulo)
            item.add_value('titulo', titulo)

            url = articulo.xpath('.//h3/a/@href').get() # Con el '@' puedo extraer el texto de cualquier atributo (@href por ejemplo)
            item.add_value('url', url)

            # Con get nos devuelve el primer valor que coincida con la solicitud del xpath
            autores = articulo.xpath('.//div[@class="gs_a"]//text()').getall() # getall() devuelve todos los elementos que coincidan en forma de lista
            autores = "".join(autores)
            autores = autores.split('-')[0].strip()
            item.add_value('autores', autores)

            try:
                citaciones = articulo.xpath('.//a[contains(@href, "cites")]//text()').get()
                citaciones = citaciones.replace('Cited by ', '')
            except:
                pass
            item.add_value('citaciones', citaciones)

            yield item.load_item()

"""
Concurrencia

Controlar cuantos requerimientos puedo hacer como máximo al mismo tiempo, y por defecto es 16
"""