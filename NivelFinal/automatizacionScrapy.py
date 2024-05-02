"""
Objetivo:
Extraer la ciudad, la temperatura actual y la sensación térmica real de Guayaquil, Quinto y Madrid.

Herramientas:
Scrapy: Requerimiento y parseo
Twisted: Automatización de extracción
"""
from twisted.internet import reactor
from twisted.internet.task import LoopingCall
from scrapy.crawler import CrawlerRunner
from scrapy.spiders import Spider

class ExtractorClima(Spider):
    name = "CLIMA"
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        #'CLOSESPIDER_PAGECOUNT': 20,
        'LOG_ENABLED': False # False elimina los miles de logs que salen al ejecutar Scrapy en terminal
        # Determina si Scrapy va a mostrar dentro de la terminal, los logs de todo lo que está haciendo por detrás al momento de realizar una extracción.
    }

    start_urls = [ # Como es una lista, podemos visitar varias páginas a la vez agregandolas en esta lista
        "https://www.accuweather.com/es/ec/guayaquil/127947/weather-forecast/127947",
        "https://www.accuweather.com/es/ec/quito/129846/weather-forecast/129846",
        "https://www.accuweather.com/es/es/madrid/308526/weather-forecast/308526"
    ]

    def parse(self, response):
        ciudad = response.xpath('//h1/text()').get() # El get se ponde ya que obtenemos un elemento y sin el get no lo extraemos correctamente
        current = response.xpath('//div[contains(@class, "cur-con-weather-card__body")]//div[@class="temp"]/text()').get()
        realFeel = response.xpath('//div[contains(@class, "cur-con-weather-card__body")]//div[@class="real-feel"]/text()').get()

        # Limpieza de datos
        ciudad = ciudad.replace('\n', '').replace('\r', '').strip()
        current = current.replace('C', '').replace('°', '').replace('\n', '').replace('\r', '').strip()
        realFeel = realFeel.replace('RealFeel®', '').replace('°', '').replace('\n', '').replace('\r', '').strip()

        # Guardado de datos en un archivo
        f = open("./NivelFinal/datosClimaScrapy.csv", "a")
        f.write(ciudad + "," + current + "," + realFeel + "\n")
        f.close()

        print(ciudad)
        print(current)
        print(realFeel)
        print()
        # No necesito hacer yield. El yield me sirve cuando voy a guardar los datos
        # en un archivo, corriendo Scrapy desde Terminal

"""
Funciones anónimas en Python: Son funciones qu eno tienen un nombre, y se las define en una sola línea.
Es decir, no necesitan la palabra "def" para ser definidas.
Se las define utilizando la palabra reservada "lambda".
Seguido de ":", y finalmente el "cuerpo" de una línea de la función.
"""

runner = CrawlerRunner()
task = LoopingCall(lambda: runner.crawl(ExtractorClima)) # Para Investigar: Funciones Anonimas en Python
task.start(10) # Tiempo en segundos desde la primera corrida del programa para repetir la extraccion
reactor.run()