"""
Objetivo:
Almacenar los datos dentro de un DataFrame de Pandas y luego escribirlos en un archivo csv.
"""
import requests
import pandas as pd

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://www.udemy.com/courses/search/?src=ukw&q=python"
}
# Este lazo for me ayudará a iterar el parámetro "page" del API
cursosTotales = []
for i in range(1, 2):
    urlApi = 'https://www.udemy.com/api-2.0/search-courses/?src=ukw&q=python&skip_price=true&p=' + str(i)

    response = requests.get(urlApi, headers=headers)

    # print(response) 200
    data = response.json()

    cursos = data["courses"]
    for curso in cursos:
        cursosTotales.append({
            "titulo": curso["title"],
            "comentarios": curso["num_reviews"],
            "calificacion": curso["rating"]
        })

df = pd.DataFrame(cursosTotales)

print(df)

df.to_csv("Nivel4/Cursos_Udemy.csv")