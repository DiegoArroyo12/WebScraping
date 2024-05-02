"""
Objetivo:
Extraer las imágenes de los anuncios.

Estrategia:
1. De cada anuncio extraemos el tag "img", del cual extraemos el atributo "src".
2. El atributo src es la URL donde se encuentra la imagen. Por lo tanto, haremos un requerimiento a esta URL.
3. Con ayuda de librerías adiconales, descargaremos la imagen a nuestra PC.

Herramientas:
Selenium: Requerimiento y parseo de OLX
requests: Requerimiento de cada una de las imágenes
Pillow: Procesamiento de las imágenes para poder descargarlas
"""
import requests # Haremos el requerimiento a la imagen y esta nos devolverá unos y ceros
from PIL import Image
import io

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

encabezados = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
}

opts = Options()
opts.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36')

# Instanciamos el driver de selenium que va a controlar el navegador
# A partir de este objeto voy a realizar el web scraping e interacciones
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options=opts)

# Voy a la página que requiero
driver.get('https://www.olx.in/')
sleep(3)

for i in range(2): # Voy a darle click en cargar más 3 veces
    try:
        # Busco el botón para cargar más información
        boton = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//button[@data-aut-id="btnLoadMore"]'))
        )
        boton.click() # Le doy click
        # Espero a que se cargue la información dinámica
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//li[@data-aut-id="itemBox"]//span[@data-aut-id="itemPrice"]'))
        )
    except Exception as e: break

# Las imágenes solo son cargadas cuando se encuentran dentro del paneo visual del usuario
# Por lo tanto ejecuto un script de scrolling "smooth", que hará scrolling lentamente
# Hasta el comienzo de la página
driver.execute_script("window.scrollTo({top:0, behavior:'smooth'});")
sleep(5)
"""
Este script también me sirve en algunas webs para realizar carga dinámica de información.
En este caso OLX carga más información al dar click.
En otras páginas, se carga más información al hacer scrolling.
"""

# Encuentro cual es el XPATH de cada elemento donde esta la informacion que quiero extraer
# Esto es una LISTA. Por eso el metodo esta en plural
anuncios = driver.find_elements('xpath', '//li[@data-aut-id="itemBox"]')

i = 0
# Recorro cada uno de los anuncios que he encontrado
for anuncio in anuncios:
    # print(anuncio.get_attribute('innerHTML'))
    # Por cada anuncio hallo el preico
    precio = anuncio.find_element('xpath', './/span[@data-aut-id="itemPrice"]').text
    print (precio)
    # Por cada anuncio hallo la descripcion
    descripcion = anuncio.find_element('xpath', './/span[@data-aut-id="itemTitle"]').text
    print (descripcion)

    try:
        url = anuncio.find_element('xpath', './/figure[@data-aut-id="itemImage"]/img')
        # Obtengo el URl de la imagen del anuncio
        url = url.get_attribute('src')
        
        # Con requests, hago el requerimiento a la URL de la imagen
        # Es importante aqui no olvidar los principios que hemos aprendido en el curso, y pasar headers con un user-agent
        image_content = requests.get(url, headers=encabezados).content

        # PROCESAMIENTO DE LA IMAGEN
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file).convert('RGB') # Convertimos los unos y ceros
        file_path = './NivelFinal/Imagenes/'+ str(i) + '.jpg'  # Nombre a guardar de la imagen
        with open(file_path, 'wb') as f: 
            image.save(f, "JPEG", quality=85) # "quality": Indica la calidad en la que yo quiero guardar la imagen.
            # Es un número que va de 1 a 100 dependiendo de el % de calidad que yo quiero mantener de la calidad original de la imagen.
    except Exception as e:
        print(e)
        print ("Error")
    i += 1