from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

"""
Logearnos dentro de la plataforma de Twitter/X, llenando un formulario de log in desde Selenium. Y, una vez dentro descargar los tweets que veamos dentro de la página principar de Twitter/X.
"""

opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options=opts)
driver.get('https://twitter.com/i/flow/login')

user = "diegoarroyopalacioscr7@hotmail.com"
password = "Diegop7736fuRy_"

inputUser = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//input[@name="text"]'))
)
inputUser.send_keys(user) # Me permite, desde Selenium, escribir un texto dentro de un input en la página web.

# Debemos presionar primero el botón antes de poder ingresar el password
botonSiguiente = driver.find_element(By.XPATH, '//span[text()="Siguiente"]')
botonSiguiente.click()

inputPass = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//input[@name="password"]'))
)
inputPass.send_keys(password)

loginButton = driver.find_element(By.XPATH, '//div[@data-testid="LoginForm_Login_Button"]')
loginButton.click()

tweets = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//div[@data-testid="tweetText"]'))
)

for tweet in tweets:
    print(tweet.text)