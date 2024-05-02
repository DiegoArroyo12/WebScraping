"""
Extracción Incremental:
Se dice de una extracción que ocurre en diferentes momentos en el tiempo.
De tal manera que no extraiga información repetida, si no solamente información nueva, pudiendo al mismo tiempo
actualizar información ya extraída.

Objetivo:
Actualizar las temperaturas de las ciudades dentro de nuestra base de datos, y si la ciudad no existe, agregarla a la base.

Herramientas:
Selenium: Requerimiento y parseo
Scrapy: Requerimiento y parseo
Pymongo: Acceso a MongoDB
"""
from twisted.internet import reactor
from twisted.internet.task import LoopingCall
from scrapy.crawler import CrawlerRunner
from scrapy.spiders import Spider
from pymongo import MongoClient


client = MongoClient('localhost')
db = client['WebScrapingCurso']
col = db['climaScrapy']


class ExtractorClima(Spider):
    name = "MiCrawlerDeClima"
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        #'CLOSESPIDER_PAGECOUNT': 20,
        'LOG_ENABLED': False
    }
    start_urls = [
        "https://www.accuweather.com/es/ec/guayaquil/127947/weather-forecast/127947",
        "https://www.accuweather.com/es/ec/quito/129846/weather-forecast/129846",
        "https://www.accuweather.com/es/es/madrid/308526/weather-forecast/308526"
    ]
    def parse(self, response):
        print(response)
        ciudad = response.xpath('//h1/text()').get()
        current = response.xpath('//div[contains(@class, "cur-con-weather-card__body")]//div[@class="temp"]/text()').get()
        real_feel = response.xpath('//div[contains(@class, "cur-con-weather-card__body")]//div[@class="real-feel"]/text()').get()
        ciudad = ciudad.replace('\n', '').replace('\r', '').strip()
        current = current.replace('C', '').replace('°', '').replace('\n', '').replace('\r', '').strip()
        real_feel = real_feel.replace('RealFeel®', '').replace('°', '').replace('\n', '').replace('\r', '').strip()

        # Debo elegir cual de mis propiedades va a ser UNICA a lo largo de todos los documentos
        col.update_one({
            'ciudad': ciudad # En este caso es mi ciudad, es decir. Por esta condición voy a buscar para actualizar
        }, {
            '$set': { # Si no se encuentra ni un documento con el identificador, se inserta un documento nuevo
                'ciudad': ciudad, # Si si se encuentra un documento con el identificador, se actualiza ese documento con la nueva información
                'current': current,
                'real_feel': real_feel
            }
        }, upsert=True) # Flag para utilizar la lógica de Upsert
        """
        UPSERT:
        Operación de INSERCIÓN en caso de no existri un documento que cumpla con mi condición.
        Y operación de ACTUALIZACIÓN en caso de que exista un documento que cumpla con mi condición.
        Upsert hace que si se encuetra una coincidencia con el primer parámetro, actualiza el elemento, si no lo añade a la base
        """

# Logica de automatización
runner = CrawlerRunner()
task = LoopingCall(lambda: runner.crawl(ExtractorClima))
task.start(30) # ejecutar cada 30 segundos
reactor.run()