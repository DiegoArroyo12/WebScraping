"Scripts"
# 1. Hallar el Tag Script que contiene la información que me interesa.
# 2. como limpiamos el contenido del tag para obtener lo que nos interesa.
import requests
from lxml import html
import json

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

respuesta = requests.get('https://www.gob.pe/busquedas?reason=sheet&sheet=1', headers=headers)
respuesta.encoding = 'UTF-8'

parser = html.fromstring(respuesta.text)

datos = parser.xpath("//script[contains(text(), 'window.initialData')]")

# .find(): Me devuelve la posición (índice) dentro de una cadena de carácteres en la cual se encuentra un caracter dado dentro de una lista.
indiceInicial = datos.find('{')

datos = datos[indiceInicial:]

objeto = json.loads(datos)

resultados = objeto["data"]["attributes"]["results"]

for resultado in resultados:
    print(resultado["content"])