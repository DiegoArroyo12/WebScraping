from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Las tres librerías que ocuparemos para hacer la espera de la carga de la página
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

"""
Objetivo: 
Mejorar nuestra extracción para que se realice de una manera más óptima.
Sin tener que esperar tiempo demás por la carga de información.
Para esto utilizaremos las esperas por evento que nos provee Selenium para esperar que la información este cargada.
"""

opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
opts.add_argument("--headless") # Hace que no se abra la interfaz del navegador y todo se realice detrás de cámaras
# Instancia el driver de selenium que va a controlar el navegador
# A partir de este objeto voy a realizar el web scraping e interacciones
driver = webdriver.Chrome(
    service = Service(ChromeDriverManager().install()), # Esta librería mantiene actualizado el driver manager para no tener que descargarlo siempre
    options=opts
)

# Voy a la página que requiero
driver.get('https://www.olx.in/')

for i in range(3): # Voy a darle click en cargar más 3 veces
    try:
        # WebDriverWait espera a que aparezca el botón y luego me lo retorna
        boton = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//button[@data-aut-id="btnLoadMore"]'))
        )
        # Le doy click
        boton.click()
        # Espero que cargue la información dinámica
        WebDriverWait(driver, 10).until( # No la guardo en una variable puesto que no reutilizare el elemento
            EC.presence_of_all_elements_located((By.XPATH, '//li[@data-aut-id="itemBox"]//span[@data-aut-id="itemPrice"]'))
        )
        
    except: 
        # Si hay algún error, rompo el lazo. No me complico.
        break

# Encuentro cual es el XPATH de cada elemento donde esta la información que quiero extraer
# Esto es una LISTA. Por eso  el método esta en plural
anuncios = driver.find_elements(By.XPATH, '//li[@data-aut-id="itemBox"]')

# Recorro cada uno de los anuncios que he encontrado
for anuncio in anuncios:
    try:
        # Por cada anuncio hallo el precio
        precio = anuncio.find_element(By.XPATH, './/span[@data-aut-id="itemPrice"]').text
        print (precio)
        # Por cada anuncio hallo la descripcion
        descripcion = anuncio.find_element(By.XPATH, './/div[@data-aut-id="itemTitle"]').text
        print (descripcion)
    except Exception as e:
        print ('Anuncio carece de precio o descripcion')