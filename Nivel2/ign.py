from scrapy.item import Field, Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

class Articulo(Item):
    titulo = Field()
    contenido = Field()

class Review(Item):
    titulo = Field()
    calificacion = Field()

class Video(Item):
    titulo = Field()
    fechaPublicacion = Field()

class IGNCrawler(CrawlSpider):
    name = 'ign'
    custom_settings = {
        'USER_AGENT': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        'CLOSESPIDER_PAGECOUNT': 150
    }

    allowed_domains = ['latam.ign.com']

    download_delay = 1

    start_urls = ['https://latam.ign.com/se/?model=article&q=ps5']

    rules = (
        # Horizontalidad por tipo de información
        Rule(
            LinkExtractor(
                allow = r'/?type='
            ), follow=True
        ),
        # Horizontalidad por paginación
        Rule(
            LinkExtractor(
                allow=r'&page=\d+' #  \d+ puede ser reemplazado por cualquier número
            ), follow=True
        ),
        # Una regla por cada tipo de contenido donde ire verticalmente
        # RESEÑAS
        Rule(
            LinkExtractor(
                allow=r'/review/'
            ), follow=True, callback='parse_review'
        ),
        # VIDEOS
        Rule(
            LinkExtractor(
                allow=r'/video/'
            ), follow=True, callback='parse_video'
        ),
        # ARTICULOS
        Rule(
            LinkExtractor(
                allow=r'/news/'
            ), follow=True, callback='parse_news'
        ),
    )

    def parse_news(self, response):
        item = ItemLoader(Articulo(), response)
        item.add_xpath('titulo', '//h1[@id="id_title"]/text()')
        item.add_xpath('contenido', '//div[@id="id_text"]//*/text()') # El asterisco simboliza que seleccione de todos los tags o cualquier tag

        yield item.load_item()

    def parse_review(self, response):
        item =ItemLoader(Review(), response)
        item.add_xpath('titulo', '//h1/text()')
        item.add_xpath('calificacion', '//span[@class="side-wrapper side-wrapper hexagon-content"]/div/text()')

        yield item.load_item()

    def parse_video(self, response):
        item = ItemLoader(Video(), response)
        item.add_xpath('titulo', '//h1/text()')
        item.add_xpath('fechaPublicacion', '//span[@class="publish-date"]/text()')

        yield item.load_item()