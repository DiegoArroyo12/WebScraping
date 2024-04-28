#import requests
from bs4 import BeautifulSoup
import cloudscraper # Esta librería es muy similar a requests, pero por detrás setea una serie de headers y otra serie de mecanismos para poder sobrepasar las páginas que nos bloquean 

encabezados = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}

url = 'https://www.zonaprop.com.ar/cocheras-alquiler-capital-federal.html'

#session = requests.Session()
scraper = cloudscraper.create_scraper() # Setea los headers y más
response = scraper.get(url)

soup = BeautifulSoup(response.text, features="lxml")

anuncios = soup.find_all('div', {"data-qa": "posting PROPERTY"})

for anuncio in anuncios:
    titulo = anuncio.find('h2').text
    print(titulo)

"""
Belgrano, Capital Federal
Tribunales, Capital Federal
Villa Crespo, Capital Federal
Palermo Soho, Palermo
Palermo Soho, Palermo
Recoleta, Capital Federal
Parque Rivadavia, Caballito
Belgrano C, Belgrano
San Nicolás, Capital Federal
Recoleta, Capital Federal
Belgrano, Capital Federal
Palermo Hollywood, Palermo
Palermo, Capital Federal
Almagro, Capital Federal
Villa Luro, Capital Federal
Barracas, Capital Federal
Villa Urquiza, Capital Federal
Recoleta, Capital Federal
San Nicolás, Capital Federal
Monserrat, Capital Federal
"""