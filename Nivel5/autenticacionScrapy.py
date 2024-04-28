import scrapy
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.crawler import CrawlerProcess

class LoginSpider(Spider):
    name = "GitHubLogin"
    start_urls = ['https://github.com/login']

    def parse(self, response):
        return scrapy.FormRequest.from_response( # Con esto simulamos que Scrapy fuera un humano haciendo los requerimientos
            response, # Aquí viene el formulario
            formdata={
                'login': 'DiegoArroyo12',
                'password': 'Contraseña'
            },
            callback=self.after_login # Que función voy a llamar después de darle al botón y recibiré la primera página que sale después de pasar la autenticación
        )

    def after_login(self, response):
        request = scrapy.Request(
            'https://github.com/DiegoArroyo12?tab=repositories', # Hace un requerimiento forsozo a la url asignada aquí
            callback=self.parse_repositorios # En esta función ya haré la extracción deseada
        )
        yield request

    def parse_repositorios(self, response):
        sel = Selector(response)
        repositorios = sel.xpath('//h3[@class="wb-break-all"]/a/text()')

        for repositorio in repositorios:
            print(repositorio.get())

process = CrawlerProcess() # Para correr el código sin necesidad de terminal
process.crawl(LoginSpider)
process.start() # En su defecto hacer: scrapy runspider autenticacionScrapy.py -o githubScrapy.json