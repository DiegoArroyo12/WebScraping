"""
Objetivo:
Extraer los archivos disponibles en esta página.

Estrategia:
1. De cada tag "a" extraemos el atributo "href"
2. El atributo "href"es la URL donde se encuentra el archivo. Por lo tanto, haremos un requerimiento a esta
   Url con requests
3. Con ayuda de manejo de archivos en Python, escribimos el archivo a nuestra PC

Herramientas:
BeautifulSoup: Parseo de la URL semilla para obtener las URLs de los archivos.
requests: Requerimiento de la URL semilla y de cada uno de los archivos.
"""
import requests
from bs4 import BeautifulSoup

encabezados = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}

url = 'https://file-examples.com/index.php/sample-documents-download/sample-xls-download/'

response = requests.get(url, headers=encabezados)
soup = BeautifulSoup(response.text, 'lxml')

# Lista para almacenar las urls de los archivos
urls = []

# Obtenemos los botones para descargar los archivos
descargas = soup.find_all('a', class_="download-button")
for descarga in descargas:
    # De cada botón extraemos el link de descarga de el archivo que estan en la etiqueta "href"
    urls.append(descarga["href"])
print(urls)
i = 0
for url in urls: # Por cada url de los archivos que quiero descargar
    r = requests.get(url, allow_redirects=True)
    nombreArchivo = './NivelFinal/Archivos/' + url.split('/')[-1]
    output = open(nombreArchivo, 'wb')
    output.write(r.content) # Escribir el archivo en mi PC
    output.close()
    i += 1