import requests
from lxml import html
import json

# En esta ocasión no sería tan necesario los encabezados ya que esto es una API
encabezados = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}

# "https://api.github.com/user/repos{?type,page,per_page,sort}"
# {?type,page,per_page,sort} Son las opciones que nos da la API para poder hacer consultas
endpoint = 'https://api.github.com/user/repos?page=1'

usuario = 'DiegoArroyo12'
password = 'Token' # Es necesario usar el Token (dando acceso a los repos) y ya no la contraseña

response = requests.get(endpoint, headers=encabezados, auth=(usuario, password))

repositorios = response.json()

for repositorio in repositorios:
    print(repositorio["name"])