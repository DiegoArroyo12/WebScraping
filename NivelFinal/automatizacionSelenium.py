"Selenium: Requerimiento y parseo"
"Schedule: Automatización de extracción"
"Objetivo: Extraer la misma información que con Scrapy pero ahora con Selenium"
import schedule
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

start_urls = [
    "https://www.accuweather.com/es/ec/guayaquil/127947/weather-forecast/127947",
    "https://www.accuweather.com/es/ec/quito/129846/weather-forecast/129846",
    "https://www.accuweather.com/es/es/madrid/308526/weather-forecast/308526"
]

def extraerDatos():
    driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))

    for url in start_urls:
        driver.get(url)

        ciudad = driver.find_element(By.XPATH, '//h1').text
        current = driver.find_element(By.XPATH, '//div[contains(@class, "cur-con-weather-card__body")]//div[@class="temp"]').text
        realFeel = driver.find_element(By.XPATH, '//div[contains(@class, "cur-con-weather-card__body")]//div[@class="real-feel"]').text

        # Limpieza de datos
        ciudad = ciudad.replace('\n', '').replace('\r', '').strip()
        current = current.replace('C', '').replace('°', '').replace('\n', '').replace('\r', '').strip()
        realFeel = realFeel.replace('RealFeel®', '').replace('°', '').replace('\n', '').replace('\r', '').strip()

        # Guardado de datos en un archivo
        f = open("./NivelFinal/datosClimaSelenium.csv", "a")
        f.write(ciudad + "," + current + "," + realFeel + "\n")
        f.close()

        print(ciudad)
        print(current)
        print(realFeel)
        print()

    driver.close()

# "Agenda" una nueva consulta
schedule.every(1).minutes.do(extraerDatos)

# Llamamos a la funcion fuera del lazo para una primera llamada instantanea
extraerDatos()

# Reviso la cola de procesos cada segundo, para verificar si tengo que correr algun proceso pendiente
while True:
    schedule.run_pending()
    time.sleep(1)