from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from random import uniform

"Tuve que poner un debug de botón rojo en las líneas que tienen un *"

opts = Options()
opts.add_argument(
    "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options=opts)

driver.get('https://listado.mercadolibre.com.mx/listado-herramientas-vehiculos?internal_referrer=true&matt_tool=6166775&matt_word=SEARCH') # *

herramientas = open("Nivel3/herramientas.txt", "w") # *

while True: # Metemos todo el código en un while porque se ejecutará hasta que ya no exista el botón "Siguiente" dentro de la página
    linksProductos = driver.find_elements(By.XPATH, '//a[@class="ui-search-item__group__element ui-search-link__title-card ui-search-link"]') # *
    linksPagina = []

    try:
        for tagA in linksProductos:
            linksPagina.append(tagA.get_attribute("href")) # get_attribute(): Me permite obtener el valor de cualquier atributo de un tag HTML. # *
    except Exception as e:
        print(e)
        break

    for link in linksPagina:
        sleep(uniform(5.0, 7.0))
        try:
            driver.get(link) # Para que mi navegador Selenium se dirija a una nueva URL simplemente llamo de nuevo a la función.get()
            titulo = driver.find_element(By.XPATH, '//h1').text # *
            precio = driver.find_element(By.XPATH, '//div[@class="ui-pdp-price__second-line"]//span[@class="andes-money-amount__fraction"]').text # *
            resultado = f"Titulo: {titulo} Precio: {precio}\n"
            herramientas.write(resultado) # *
            # Para volver a la url semilla
            driver.back()
        except Exception as e:
            print(e)
            # Si ocurre un error volvemos a la url semilla
            driver.back() # .back() funciona exactamente igual que la flechita para ir "atrás" en nuestros navegadores
            print("Error")

    try:
        # Paginación Horizontal: Nos apoyaremos en el botón "Siguiente"
        botonSiguiente = driver.find_element(By.XPATH, '//span[text()="Siguiente"]')
        botonSiguiente.click()
    except:
        break # Rompe el bucle
"""
La velocidad de la extracción depende de 3 factores:
    1. La velocidad de nuestro Internet
    2. La potencia de nuestra Computadora
    3. El nivel de optimización de nuestro Código
"""