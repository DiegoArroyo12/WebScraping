from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

"Disclaimers: Diálogos donde tenemos que aceptar términos y condciones o aceptar el uso de cookies. Estos muchas veces inhiben la extracción de datos antes de ser cerrados."

def obtenerScriptScrolling(iteration):
    scrollingScript = """
        window.scrollTo(0,20000)
    """
    return scrollingScript.replace('20000', str(20000 * (iteration + 1)))

opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)
driver.get('https://www.youtube.com/playlist?list=PLuaGRMrO-j-8NndtkHMA7Y_7798tdJWKH')
sleep(2)

try:
    botonDisclainer = driver.find_element(By.XPATH, '//button[@aria-label="Accept all"]')
    botonDisclainer.click()
    sleep(2)
except:
    print("No hay botón disclaimer")

videos = driver.find_elements(By.XPATH, '//div[@id="contents"]/ytd-playlist-video-renderer')
urlsVideos = []

for video in videos:
    url = video.find_element(By.XPATH, './/h3/a[@id="video-title"]').get_attribute("href")
    urlsVideos.append(url)

print(urlsVideos)

for url in urlsVideos:
    driver.get(url)
    sleep(3)
    
    driver.execute_script(obtenerScriptScrolling("window.scrollTo(0, 400)"))
    sleep(3)

    # No cargaba la sección de el número de comentarios
    # Debido es debido a que este elemento solamente se carga si es que el usuario lo "mira" explícitamente en su navegador.
    # Al hacer el scrolling instantáneo, nos saltamos este elemento y nunca lo vemos y nunca se carga
    numComentariosTotales = driver.find_element(By.XPATH, '//h2[@id="count"]//span[1]').text
    numComentariosTotales = int(numComentariosTotales) * 0.90
    print('Comentarios Totales: ', numComentariosTotales)

    comentariosCargados = driver.find_elements(By.XPATH, '//yt-formatted-string[@id="content-text"]')

    nScrolls = 0
    nScrollsMaximo = 10
    while len(comentariosCargados) < numComentariosTotales and nScrolls < nScrollsMaximo:
        driver.execute_script(obtenerScriptScrolling(nScrolls))
        nScrolls += 1
        sleep(2)
        comentariosCargados = driver.find_elements(By.XPATH, '//yt-formatted-string[@id="content-text"]')

    comentarios = driver.find_elements(By.XPATH, '//yt-formatted-string[@id="content-text"]')
    for comentario in comentarios:
        textoComentario = comentario.text
        print(textoComentario)

    print()
    print()