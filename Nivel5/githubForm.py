import requests
from lxml import html

# requests: Hacer requerimientos y mantener una sesión
# Parsear el árbol HTML

encabezados = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

loginFormUrl = 'https://github.com/login'

session = requests.Session() # Me va a mantener la sesión UNA VEZ QUE ME HAYA LOGEADO.

loginForm = session.get(loginFormUrl, headers=encabezados)

parser = html.fromstring(loginForm.text)
token = parser.xpath('//input[@name="authenticity_token"]/@value') # Extrae el atributo 'value'

loginUrl = 'https://github.com/session'

loginData = { # Esto solo funciona para requerimientos POST no para los GET
    "login": "DiegoArroyo12",
    "password": "Contraseña",
    "commit": "Sign in",
    # Cuando vemos en la sección Networks todos estos datos, el 'authenticity_token' que se muestra ahí ya no es válido
    # por ello debemos extraer el que se muestra en el input oculto.
    "authenticity_token": token
}

session.post(
    loginUrl,
    loginData,
    headers=encabezados,
)

# Hasta aquí solo nos hemos logeado, procederemos a hacer una extracción

url = 'https://github.com/DiegoArroyo12?tab=repositories'
# Seguiremos utilizando el session para hacer los requerimientos
respuesta = session.get(
    url, headers=encabezados
)

parser = html.fromstring(respuesta.text)
respositorios = parser.xpath('//h3[@class="wb-break-all"]/a/text()')

for repositorio in respositorios:
    print(repositorio)

"""
    WebScraping

    SQL

    DesarrolloWEB

    FreeLancer

    House

    31916Diego

    PreprocesamientoDeDatosPython

    EDD_1310

    JavaExplorer

    ManejoDeBasesDeDatosConPython

    ProgramacionOrientadaAObjetosConPython

    EstructurasDeDatosEnPython

    Introduccion-a-la-Programacion-con-Python

    Diego
"""