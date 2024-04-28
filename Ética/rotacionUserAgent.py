from scrapy.item import Field, Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

class Hotel(Item):
    nombre = Field()
    precio = Field()
    descripcion = Field()
    amenities = Field()

class TripAdvisor(CrawlSpider):
    name = "Hoteles"
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": { # Haciendo Rotación de User Agent
            'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None, # Le decímos a Scrapy que no utilice el sistema de User Agent default
            'scrapy_useragents.downloadermiddlewares.useragents.UserAgentsMiddleware': 500, # Si no que utilice este de nuestra librería 
        },
        "USER_AGENTS": { # Se rotará sobre estos 5 User Agent
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        }
    }
    start_urls = ['https://www.tripadvisor.com/Hotels-g303845-Guayaquil_Guayas_Province-Hotels.html']

    download_delay = 2

    rules = (
        Rule(
            LinkExtractor(
                allow=r'/Hotel_Review-'
            ), follow=True, callback="parse_hotel"
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