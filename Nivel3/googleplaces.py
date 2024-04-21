from time import sleep
from random import uniform
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

"""
Extraer de los perfiles de los usuarios algunas de las opiniones que ellos han realizado a cualquier restaurante. De cada opinión vamos a extraer el número de estrellas y también el texto de la reseña.
"""

# Lógica de Scrolling
# Paso 1: Copiar el script de scrolling en mi código como una cadena de texto
# Paso 2: Identificar el contenedor al cual le debo hacer SCROLLING.
# Paso 3: Definir el número de pixeles que voy a hacer SCROLL

scrollingScript = """
    document.getElementsByClassName('m6QErb DxyBCb kA9KIf dS8AEf')[0].scroll(0,100000)
"""

opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options=opts)
driver.get('https://www.google.com/maps/place/Amaz%C3%B3nico/@40.423706,-3.6872655,17z/data=!4m8!3m7!1s0xd422899dc90366b:0xce28a1dc0f39911d!8m2!3d40.423715!4d-3.6850997!9m1!1b1!16s%2Fg%2F11df4t5hhs?entry=ttu')

sleep(uniform(4.0, 5.0))

SCROLLS = 0
while (SCROLLS != 3):
    driver.execute_script(scrollingScript) # Me permite ejecutar código de JavaScript dentro del navegador automatizado de Selenium.
    sleep(uniform(5, 6))
    SCROLLS += 1

restaurantsReviews = driver.find_elements(By.XPATH, '//div[@data-review-id and not(@aria-label)]')

for review in restaurantsReviews:
    userLink = review.find_element(By.XPATH, ".//div[contains(@class, 'WNx')]//button")

    try:
        userLink.click()

        "Selenium necesita cambiarse de pestaña de manera explícita. Ya que, por así decirlo, el driver se queda en al pestaña anterior."
        "Y no podremos utilizar el driver para encontrar elementos dentro de la nueva pestaña que hemos abierto."
        driver.switch_to.window(driver.window_handles[1]) # Regresa una lista de todas las pestañas abiertas en el navegador
        "window_handles: Contiene una lista con todas las pestañas y ventanas que se encuentran abiertas dentro del navegador automatizado de Selenium."

        botonOpiniones = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//button[@class="hh2c6 G7m0Af"]'))
        )

        botonOpiniones.click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="m6QErb DxyBCb kA9KIf dS8AEf "]'))
        )

        USER_SCROLLS = 0
        while (USER_SCROLLS != 3):
            driver.execute_script(scrollingScript)
            sleep(uniform(5, 6))
            USER_SCROLLS += 1

        userReviews = driver.find_elements(By.XPATH, '//div[@class="GHT2ce"]')

        for userReview in userReviews:
            texto = userReview.find_element(By.XPATH, './/span[@class="wiI7pd"]').text
            rating = userReview.find_element(By.XPATH, './/span[@class="kvMYJc"]').get_attribute("aria-label") # get_attribute(): Me sirve para obtener cualquier atributo que exista dentro de un elemento HTML

            print(texto)
            print(rating)

        # driver.close(): Me sirve para cerra la ventana en la cual me encuentro actualmente
        driver.close()

        # Volvemos a la página principal
        driver.switch_to.window(driver.window_handles[0])
    except Exception as e:
        print(e)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

