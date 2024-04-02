import requests
from lxml import html

# User Agents
"Es una cadena de texto con la cual se puede identificar el navegador y el sistema operativo del cliente. Por defecto es: ROBOT"
"Cadena de texto que me identifica hacia un servidor. Indica la versión del navegador que estoy utilizando."
"Si no lo configuramos manualmente, las herramientas que hemos aprendido utilizarán un userAgent por defecto que es fácilmente detectable por mecanismos anti bots"
encabezados = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

url = 'https://www.wikipedia.org/'

respuesta = requests.get(url, headers=encabezados) # Obtiene el HTML de la página

parser = html.fromstring(respuesta.text) # Convierte en un parseador el texto HTML

espanol = parser.get_element_by_id("js-link-box-es") # print(espanol.text_content())

espanol = parser.xpath("//a[@id='js-link-box-es']/strong/text()") # xpath() función

idiomas = parser.xpath("//div[contains(@class, 'central-featured-lang')]//strong/text()") # Ocupamos la función contains() para seleccionar los divs que contengan esa clase 

idiomas = parser.find_class('central-featured-lang') # Busca por clase pero no devuelve el texto en si, hay que ocupar .text_content()

"xpath: No diferencia entre las clases y piensa que aunque haya dos clases para el es solo una"
".find_class: Si diferencia entre las clases"

for idioma in idiomas:
    print(idioma.text_content())