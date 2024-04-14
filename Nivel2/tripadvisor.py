from scrapy.item import Field, Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose # Clase pra pre-procesar datos extraídos del árbol, antes de guardarlos en un archivo
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

# Objetivo: Extraer el nombre, precio, descripción y facilidades de los hoteles que aparecen en la primera página de una búsqueda en TripAdvisor

class Hotel(Item):
    nombre = Field()
    precio = Field()
    descripcion = Field()
    amenities = Field()

class TripAdvisor(CrawlSpider):
    name = "Hoteles"
    custom_settings = {
        'USER_AGENT': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"    
    }
    start_urls = ['https://www.tripadvisor.com/Hotels-g303845-Guayaquil_Guayas_Province-Hotels.html']

    # Mecanismo para protegernos de baneos, esto hace que espere el tiempo asignado para realizar otra consulta 
    download_delay = 2

    # Son el orquestador de mi CrawlSpider. Son reglas que definen a cuales links dentro de la URL semilla mi spider tiene o no tien que ir en búsqueda de información
    rules = (
        Rule(
            LinkExtractor(
                allow=r'/Hotel_Review-'
            ), follow=True, callback="parse_hotel" # Callback solamente lo definimos en las reglas que me van a llevar a las páginas en donde yo voy a extraer la información
        ),
    )

    def quitarSimboloDolar(self, texto):
        nuevoTexto = texto.replace("$", "")
        return nuevoTexto

    def parse_hotel(self, response):
        "Este es el callback de rules"
        sel = Selector(response)
        item = ItemLoader(Hotel(), sel)

        item.add_xpath('nombre', '//h1[@id="HEADING"]/text()')
        item.add_xpath('precio', '//div[@class="aLfMd"]/div/text()', MapCompose(self.quitarSimboloDolar))
        item.add_xpath('descripcion', '//div[@id="ABOUT_TAB"]/div[2]/div[1]/div[4]/div/text()')
        item.add_xpath('amenities', '//div[@id="ABOUT_TAB"]/div[2]/div[2]/div[2]//div//text()')

        yield item.load_item()