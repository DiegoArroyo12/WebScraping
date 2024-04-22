"""
Objetivo:
Extraer el nombre, número de reviews y calificación de los recursos de Udemy relacionados con la búsqueda: "Python".

La página de Udemy no carga toda la información al cargar la página en nuestro navegador. 
En realidad, esta información que ven en pantalla, se carga con un requerimiento que se hace posterior a la carga de la página.

La pestaña NETWORKS de Google Chrome permite visualizar absolutamente todos los requerimientos que realiza el navegador dentro de la página en donde nos encontramos.

El requerimiento a la URL principal, me devuelve un HTML vacío.
Una especie de esqueleto.
Esto quiere decir que la información de los cursos se carga de manera dinámica a través de otro requerimiento a otra URL.

SI PUEDO UTILIZAR SCRAPY
Pero no puedo utilizarlo para hacer el requerimiento a la URL de Udemy donde yo ve la interfaz. 
También tengo que realizar el requerimiento a la URL del API pero desde Scrapy.
"""
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://www.udemy.com/courses/search/?src=ukw&q=python" # Es un encabezado que le dice al servidor de donde esta viniendo el requerimiento.
}

# Hacemos la paginación con un for y concatenando las páginas ya que el orden no importa
for i in range(1, 4):
    urlApi = 'https://www.udemy.com/api-2.0/search-courses/?src=ukw&q=python&skip_price=true&p=' + str(i)

    response = requests.get(urlApi, headers=headers)

    # print(response) 200
    data = response.json()

    cursos = data["courses"]

    for curso in cursos:
        titulo = curso["title"]
        reviews = curso["num_reviews"]
        calificacion = curso["rating"]
        print(f"Titulo: {titulo}\n Comentarios: {reviews}\n Calificación: {calificacion}\n")