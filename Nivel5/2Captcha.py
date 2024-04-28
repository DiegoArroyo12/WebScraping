"""
Objetivo:
Extraer la información a la cual solo tenemos acceso una vez resuelto un captcha. Este captcha es de tipo Google reCAPTCHA v2. 
Y lo resolveremos de manera automática utilizando 2CAPTCHA.com
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import requests

opts = Options()
opts.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36')

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options=opts)

driver.get('https://www.google.com/recaptcha/api2/demo') # Paso 2

try:
    captcha_key = driver.find_element(By.ID, 'recaptcha-demo').get_attribute('data-sitekey') # Paso 1

    url = "https://2captcha.com/in.php?"
    url += "key=" + "f693ef97b9d4da4e798101b79c8973ab"
    url += "&method=userrecaptcha"
    url += "&googlekey=" + captcha_key
    url += "&pageurl=" + url
    url += "&jsom=0"

    print(url)

    respuesta = requests.get(url) # Paso 3
    captchaServiceKey = respuesta.text

    print(captchaServiceKey)

    captchaServiceKey = captchaServiceKey.split('|')[-1]

    urlResp = "https://2captcha.com/in.php?"
    urlResp += "key=" + "f693ef97b9d4da4e798101b79c8973ab"
    urlResp += "&action=get"
    urlResp += "&id=" + captchaServiceKey
    urlResp += "&json=0"

    print(urlResp)

    sleep(20)
    while True: # Paso 4
        respuestaSolver = requests.get(urlResp)
        respuestaSolver = respuestaSolver.text
        print(respuestaSolver)
        if respuestaSolver == "CAPTCHA_NOT_READY" or respuestaSolver == "ERROR_CAPTCHA_UNSOLVABLE" or respuestaSolver == "ERROR_ZERO_CAPTCHA_FILESIZE":
            sleep(5)
        else: break

    respuestaSolver = respuestaSolver.split('|')[-1] # Paso 5
    print()
    insertarSolucion = 'document.getElementById("g-recaptcha-response").innerHTML="' + respuestaSolver + '";'
    print(insertarSolucion) # Paso 6

    driver.execute_script(insertarSolucion)

    submitButton = driver.find_element(By.XPATH, '//input[@id="recaptcha-demo-submit"]')
    submitButton.click()
except Exception as e:
    print(e)

# Lógica una vez resuelto el captcha
print("Ya debo de estar en la página principal...")

contenido = driver.find_element(By.CLASS_NAME, 'recaptcha-success')
print(contenido.text)