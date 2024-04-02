from scrapy.item import Field, Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup

from scrapy.crawler import CrawlerProcess # Con esto no necesitamos ejecutar la terminal

class Noticia(Item):
    titular = Field()
    descripcion = Field()
    
class ElUniversoSpider(Spider):
    name = "MiSegundoSpider"
    custom_settings = {
        'USER_AGENT': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"    
    }

    start_urls = ['https://www.eluniverso.com/deportes/']
    
    def parse(self, response):
        """
        sel = Selector(response)
        noticias = sel.xpath('//div[contains(@class,"content-feed")]//li')
        for noticia in noticias:
            item = ItemLoader(Noticia(), noticia)
            item.add_xpath('titular', './/h2//a/text()')
            item.add_xpath('descripcion', './/p/text()')
            yield item.load_item()
        """
        
        soup = BeautifulSoup(response.body)
        contenedorNoticias = soup.find_all('div', class_='content-feed')

        for contenedor in contenedorNoticias:
            noticias = contenedor.find_all('div', class_='relative ', recursive = False)
            for noticia in noticias:
                item = ItemLoader(Noticia(), response.body)
                
                titular = noticia.find('h2').text
                descripcion = noticia.find('p').text

                if (descripcion != None):
                    descripcion = descripcion.text
                else:
                    descripcion = 'N/A'    
                
                item.add_value('titular', '')
                item.add_value('descripcion', '')
                
                yield item.load_item()
                
process = CrawlerProcess({
    'FEED_FORMAT': 'csv', # Equivalente al formato
    'FEED_URI': 'resultadosuniverso.csv' # Equivalente al nombre que le asignamos al archivo
})

process.crawl(ElUniversoSpider) # Recibe como par�metro la clase Spider
process.start() # Inicia el proceso