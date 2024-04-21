from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

"""
TRADEOFF
Nos referimos como tradeoff al intercambio entre dos cualidades que deseamos en un programa, pero que no pueden convivir juntas en sus extremos.
En este caso deseamos que el scrolling sea rápido y que sea funcional (que cargue la información).
"""

def scrollingSuavizado(driver, iteracion):
    "Este Script va a funcionar si el scrolling es en un contenedor global, si es en un contenedor específico, no va a funcionar, primero tenemos que obtener dicho contenedor en el Script."
    bajarHasta = 2000 + (iteracion + 1)
    inicio = (iteracion * 2000) # Inicio donde termine la anterior iteracion
    for i in range(inicio, bajarHasta, 5): # Cada vez avanzo 5 pixeles
        scrollingScript = f"window.scrollTo(0, {i})"
        driver.execute_script(scrollingScript)

opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)
driver.get('https://www.facebook.com/elcorteingles')
sleep(2)

botonDialogo = driver.find_element(By.XPATH, '//div[@role="dialog"]//i[@data-visualcompletion="css-img"]')
botonDialogo.click()
sleep(0.5)

nScrolls = 0
maxScrolls = 50
maxPosts = 20
posts = driver.find_elements(By.XPATH, '//div[@role="article"]')

while len(posts) < maxPosts and nScrolls < maxScrolls:
    scrollingSuavizado(driver, nScrolls)
    nScrolls += 1
    posts = driver.find_elements(By.XPATH, '//div[@role="article"]')
    sleep(2)

posts = driver.find_elements(By.XPATH, '//div[@role="article"]')

for post in posts:
    textoPost = post.find_element(By.XPATH, './/div[@data-ad-preview="message"]').text
    reaccionesPost = post.find_element(By.XPATH, './/span[@class="x1e558r4"]').text

    comentariosYcompartidos = post.find_elements(By.XPATH, './/div[@class="x9f619 x1n2onr6 x1ja2u2z x78zum5 xdt5ytf x2lah0s x193iq5w xeuugli xsyo7zv x16hj40l x10b6aqq x1yrsyyn"]')
    nComentarios = 0
    Compartidos = 0
    if len(comentariosYcompartidos) == 2:
        nComentarios = comentariosYcompartidos[0].text
        Compartidos = comentariosYcompartidos[1].text
    elif len(comentariosYcompartidos) == 0:
        nComentarios = 0
        Compartidos = 0
    else:
        textoComentarios = post.find_elements(By.XPATH, './/span[text()="Ver más comentarios"]')
        hayComentarios = len(textoComentarios) > 0
        if hayComentarios: nComentarios = comentariosYcompartidos[0].text
        else: Compartidos = comentariosYcompartidos[0].text

    print(textoPost)
    print("Reacciones: ", reaccionesPost)
    print("Número de Comentarios: ", nComentarios)
    print("Número de Compartidos: ", Compartidos)

"""
window.scrollTo(0, {i})

El 0 es la coordenada horizontal a la cual queremos movernos
La "i" es la coordenada vertical a la cual queremos movernos
"""