from scrapy.item import Field, Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

class Ram(Item):
    nombre = Field()
    precio = Field()

class Amazon(CrawlSpider):
    name = "ram"
    custom_settings = {
        'USER_AGENT': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        #'CLOSESPIDER_PAGECOUNT': 10,
        'FEED_EXPORT_ENCODING': 'utf-8', 
        #'FEED_EXPORT_FIELDS': ['nombre', 'precio'] # Hace que se exporten los campos en ese orden
    }
    start_urls = ['https://www.amazon.com.mx/s?k=sodimm+ddr4+32gb+3200mhz&crid=1BBHXNV0NVOOI&sprefix=ddr4+sodimm+32gb+%2Caps%2C199&ref=nb_sb_ss_ts-doa-p_1_17']

    download_delay = 2

    # Lista de DOMINIOS a los cuales mi spider tiene permitido dirigirse. Si un dominio de una URL no se encuentra en esta lista, mi spider no irá a esta url.
    allowed_domains = ['amazon.com.mx']

    rules = (
        Rule(
            LinkExtractor(
                restrict_xpaths="//span[@data-component-type='s-search-results']",
                allow=r'=sr_pg_\d+'
            ), follow=True, callback="parse_start_url"
        ),
    )

    def limpiarTexto(self, texto):
        nuevoTexto = texto.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ').strip()
        return nuevoTexto

    def parse_start_url(self, response):
        sel = Selector(response)

        #articulos = sel.xpath("//span[@data-component-type='s-search-results']")
        articulos = sel.xpath('//div[contains(@cel_widget_id, "MAIN-SEARCH_RESULTS")]')

        for articulo in articulos:
            item = ItemLoader(Ram(), articulo)

            item.add_xpath('nombre','.//h2//span/text()', MapCompose(self.limpiarTexto))
            item.add_xpath('precio','.//span[@class="a-price-whole"]/text()')

            yield item.load_item()