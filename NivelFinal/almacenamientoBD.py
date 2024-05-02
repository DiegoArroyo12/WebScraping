"""
Guardar los datos extraídos en una base de datos es ideal para tener una persistencia de los datos.
Y para tener rápido acceso y consultas a los mismos.

Objetivo:
Guardar los datos extraídos de OLX dentro de una base de datos.
En este caso, MongoDB.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

from pymongo import MongoClient

# Conectamos con el cliente
client = MongoClient('localhost')
# Conectamos con la base de datos, si no existe la crea
db = client['WebScrapingCurso']
# Conectamos con la colección, si no existe la crea
col = db['anunciosSelenium']

opts = Options()
opts.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36')

# Instancia el driver de selenium que va a controlar el navegador
# A partir de este objeto voy a realizar el web scraping e interacciones
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options=opts)

# Voy a la página que requiero
driver.get('https://www.olx.in/')
sleep(3)

# Voy a darle click en cargar más 3 veces
for i in range(3):
    try:
        # Esperamos a que el botón se encuentre disponible
        boton = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//button[@data-aut-id="btnLoadMore"]'))
        )
        boton.click()

        # Espero hasta 10 segundos a que la información en el último elemento este cargada
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//li[@data-aut-id="itemBox"]//span[@data-aut-id="itemPrice"]'))
        )
        # Luego de que se halla el elemento, seguimos con la ejecución
    except Exception as e:
        print(e)
        break

driver.execute_script("window.scrollTo({top: 0, behavior: 'smooth'});")
sleep(5)
driver.execute_script("window.scrollTo({top: 20000, behavior: 'smooth'});")
sleep(5)
# Encuentro cual es el XPATH de cada elemento donde esta la informacion que quiero extraer
# Esto es una LISTA. Por eso el metodo esta en plural
autos = driver.find_elements('xpath', '//li[@data-aut-id="itemBox"]')

# Recorro cada uno de los anuncios que he encontrado
for auto in autos:
    # Por cada anuncio hallo el precio, que en esta pagina principal, a veces suele no estar
    try:
      precio = auto.find_element('xpath', './/span[@data-aut-id="itemPrice"]').text
    except:
      precio = 'NO DISPONIBLE'
    # Por cada anuncio hallo la descripcion
    descripcion = auto.find_element('xpath', './/span[@data-aut-id="itemTitle"]').text

    # Se agregan por medio de la colección
    col.insert_one({
        'precio': precio,
        'descripcion': descripcion
    })