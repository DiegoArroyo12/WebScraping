import requests

encabezados = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}

# Creamos una session
session = requests.Session()

# Llamamos a la url 'madre'
response = session.get('https://www.bolsadesantiago.com/', headers=encabezados)
print(response)

# Obtener el token CSRF con el API
urlToken =  'https://www.bolsadesantiago.com/api/Securities/csrfToken'
response = session.get(urlToken, headers=encabezados)
print(response)

# Extraemos el valor "csrf" del json extraido
token = response.json()['csrf']
print(token)

# Insertamos el nuevo campo con el token a los encabezados
encabezados['X-Csrf-Token'] = token

# Llamamos al API
urlApi = 'https://www.bolsadesantiago.com/api/Comunes/getHoraMercado'

response = session.post(urlApi, headers=encabezados)
print(response)
print(response.text)

diccionario = response.json()
print(diccionario)