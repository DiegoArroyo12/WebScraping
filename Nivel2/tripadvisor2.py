from scrapy.item import Field, Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

"""
Nunca nos olvidemos de la receta a seguir:
1. Definir la abstracción de mis items
2. Defino mi CrawlSpider
3. Configuración de Scrapy (Headears y Limitaciones)
4. Defino URL Semilla
5. Definir las reglas de direccionamiento
"""

class Opinion(Item):
    titulo = Field()
    calificacion = Field()
    contenido = Field()
    autor = Field()

class TripAdvisor(CrawlSpider):
    name = "OpinionesTripAdvisor"
    custom_settings = {
        'USER_AGENT': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        'CLOSESPIDER_PAGECOUNT': 100
    }

    allowed_domains = ['tripadvisor.com']
    start_urls = ['https://www.tripadvisor.com/Hotels-g303845-Guayaquil_Guayas_Province-Hotels.html']

    download_delay = 1

    rules = (
        # Paginación de Hoteles
        Rule(
            LinkExtractor(
                allow=r'-oa\d+-'
            ), follow=True
        ),
        # Detalle Hoteles
        Rule(
            LinkExtractor(
                allow=r'/Hotel_Review-',
                restrict_xpaths=['//div[contains(@id,"hotel-listing")]//div[@data-automation="hotel-card-title"]/a']
            ), follow=True
        ),
        # Paginación de Opiniones de un hotel
        Rule(
            LinkExtractor(
                allow=r'-or\d+-'
            ), follow=True
        ),
        #  Detalle de Perfil de Usuario
        Rule(
            LinkExtractor(
                allow=r'/Profile/',
                restrict_xpaths=['//div[@data-test-target="reviews-tab"]//span/a']
            ), follow=True, callback='parse_opinion'
        ),
    )

    def obtenerCalificacion(self, texto):
        calificacion = texto.split("_")[-1]
        return calificacion

    def parse_opinion(self, response):
        sel = Selector(response)
        opiniones = sel.xpath('//div[@id="content"]/div/div')
        autor = sel.xpath('//h1/span/text()').get()

        for opinion in opiniones:
            item = ItemLoader(Opinion(), opinion)
            item.add_value('autor', autor)
            item.add_xpath('titulo', './/div[@class="AzIrY b _a VrCoN"]/text()')
            item.add_xpath('contenido', './/q/text()', MapCompose(lambda i: i.replace('\n', '').replace('\r', '')))
            # Recordemos que al final de una expresión xpath, yo puedo extraer atributos del tag, en vez del texto como usualmente hemos realizado.
            # Se lo realiza poniendo "@" seguido del atributo del cual quiero extraer su valor.
            item.add_xpath('calificacion', './/div[@class="BWFIX Pd"]//span[contains(@class, "ui_bubble_rating")]/@class',
                           MapCompose(self.obtenerCalificacion))

            yield item.load_item()