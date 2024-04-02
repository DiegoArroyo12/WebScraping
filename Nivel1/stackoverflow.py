import requests
from bs4 import BeautifulSoup

encabezados = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

url = 'https://stackoverflow.com/questions'

respuesta = requests.get(url, headers=encabezados)

soup = BeautifulSoup(respuesta.text) # Parsea el árbol

contenedorPreguntas = soup.find(id='questions') # Busca por el id
listaPreguntas = contenedorPreguntas.find_all('div', class_="s-post-summary") # Busca en todos los hijos y con la clase asignada (Se debe poner class_)
".find(): Me devuelve solamente UN elemento"
".find_all(): Me devuelve TODOS los elementos que concuerden con la búsqueda dentro de una lista"

""" Cuando si hay clases
for pregunta in listaPreguntas: # Iteremos en la lista de preguntas
    textoPregunta = pregunta.find('h3').text # Obtenemos el h3
    descripcionPregunta = pregunta.find(class_= 's-post-summary--content-excerpt').text # Buscamos por el id
    descripcionPregunta = descripcionPregunta.replace('\n', '').replace('\r', '').strip() # Damos formato, quitando los saltos de línea y los espacios
    print(textoPregunta)
    print(descripcionPregunta)

    print()
"""

for pregunta in listaPreguntas: # Iteremos en la lista de preguntas
    elemento_textoPregunta = pregunta.find('h3')
    textoPregunta = elemento_textoPregunta.text

    descripcionPregunta = elemento_textoPregunta.find_next_sibling('div').text # Busca hacia el siguiente elemento (hermano)

    descripcionPregunta = descripcionPregunta.replace('\n', '').replace('\r', '').strip() # Damos formato, quitando los saltos de línea y los espacios
    print(textoPregunta)
    print(descripcionPregunta)

    print()