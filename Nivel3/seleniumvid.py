import random
from time import sleep
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver.exe')

driver.get('https://www.olx.in/cars_c84')

# Selenium también tiene sus propios métodos para encontrar elementos en el HTML:
# find_element: Me devuelve un solo elemento
# find_elements: Me devuelve un LISTADO de varios elementos

boton = driver.find_element('xpath', '//button[@data-aut-id="btnLoadMore"]')

for i in range(3):
    try:
        boton.click()
        # random.uniform(8, 10) da un número random entre 8 y 10
        sleep(random.uniform(8.0, 10.0)) # Espera este tiempo para dar click al botón y cargar más elementos, pero hay que humanizar el proceso haciendo el tiempo random
        boton = driver.find_element('xpath', '//button[@data-aut-id="btnLoadMore"]')
    except:
        break # Cuando hay algo sobre el botón como un anuncio, selenium nos dará error, por eso para blindar el código, hacemos un try except

autos = driver.find_elements('xpath', '//li[@data-aut-id="itemBox"]') # Todos los anuncios en una lista

for auto in autos:
    precio = auto.find_element('xpath', './/span[@data-aut-id="itemPrice]').text
    print(precio)
    descripcion = auto.find_element('xpath', './/span[@data-aut-id="itemTitle"]').text
    print(descripcion)
    # Las funciones de find_element y find_elements me devuelven elementos HTML.
    # Si yo quiero obtener el texto de ese elemento tengo que hacerle .text al elemento
    "La información no se encuentra cargada en su totalidad. Debido a que esta información se carga solamente al hacer click en un botón."