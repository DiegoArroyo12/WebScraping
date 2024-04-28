"""
Objetivo:
Extraer la información a la cual solo tenemos acceso una vez resuelto un captcha.
Este captcha es de tipo Google reCAPTCHA v2
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

opts = Options()
opts.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36')

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options=opts)

url = 'https://www.google.com/recaptcha/api2/demo'
driver.get(url)

try:
    driver.switch_to.frame(driver.find_element(By.XPATH, '//iframe')) # Hacemos esto para cambiarnos de contexto ya que dentro del iframe no podemos extraer sin seleccionarlo

    captcha = driver.find_element(By.XPATH, '//div[@class="recaptcha-checkbox-border"]')
    captcha.click()

    input() # Input es una instrucción que va a parar el código hasta que el usuario ingrese unos datos y de Enter dentro de la Terminal

    driver.switch_to.default_content() # Aquí regresamos del iframe a la página original

    submit = driver.find_element(By.XPATH, '//input[@id="recaptcha-demo-submit"]')
    submit.click()
except Exception as e:
    print(e)

# Yo ta voy a estar en la siguiente página
contenido = driver.find_element(By.CLASS_NAME, 'recaptcha-success')
print(contenido.text)