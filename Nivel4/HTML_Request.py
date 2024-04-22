from bs4 import BeautifulSoup
from requests_html import HTMLSession # pip install requests_html

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

url = 'https://footdistrict.com/air-jordan-1-mid-ss-ps-dx4378-400.html'

session = HTMLSession()

resp = session.get(url, headers=headers)
# Ejecuta el código Javascript para llenar la página
resp.html.render()
soup = BeautifulSoup(resp.html.html, features="lxml")

# Procedemos normalmente
contenedor_de_tallas = soup.find('div', class_="swatch-attribute-options")
lista_de_tallas = contenedor_de_tallas.find_all('div', class_="swatch-option")

for div_talla in lista_de_tallas:
    talla = div_talla.text
    print(talla)