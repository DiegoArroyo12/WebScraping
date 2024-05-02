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
import schedule
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pymongo import MongoClient # pip install pymongo
client = MongoClient('localhost')
db = client['WebScrapingCurso']
col = db['climaSelenium']

start_urls = [
    "https://www.accuweather.com/es/ec/guayaquil/127947/weather-forecast/127947",
    "https://www.accuweather.com/es/ec/quito/129846/weather-forecast/129846",
    "https://www.accuweather.com/es/es/madrid/308526/weather-forecast/308526"
]

def extraerDatos():
    driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))

    for url in start_urls:
        driver.get(url)

        ciudad = driver.find_element('xpath', '//h1').text
        current = driver.find_element('xpath', '//div[contains(@class, "cur-con-weather-card__body")]//div[@class="temp"]').text
        real_feel = driver.find_element('xpath', '//div[contains(@class, "cur-con-weather-card__body")]//div[@class="real-feel"]').text

        ciudad = ciudad.replace('\n', '').replace('\r', '').strip()
        current = current.replace('°', '').replace('\n', '').replace('\r', '').strip()
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
    driver.close()


# Llamamos a la función fuera del lazo para una primera llamada instantánea
extraerDatos()
# Lógica de automatización de extracción
schedule.every(2).minutes.do(extraerDatos) # Cada 2 minutos ejecuta la extracción
while True:
    schedule.run_pending()
    time.sleep(1)