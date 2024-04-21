from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
opts.add_argument("--headless") # Hace que no se abra la interfaz del navegador y todo se realice detrás de cámaras

driver = webdriver.Chrome(
    service = Service(ChromeDriverManager().install()), # Esta librería mantiene actualizado el driver manager para no tener que descargarlo siempre
    options=opts
)

driver.get('https://www.airbnb.mx/s/Cuernavaca--Morelos--M%C3%A9xico/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2024-05-01&monthly_length=3&monthly_end_date=2024-08-01&price_filter_input_type=0&channel=EXPLORE&date_picker_type=calendar&query=Cuernavaca%2C%20Mor.&place_id=ChIJra8im0nezYURoZC3ubW8tsk&checkin=2024-05-31&checkout=2024-06-02&adults=12&source=structured_search_input_header&search_type=autocomplete_click')
sleep(3)

resultados = driver.find_elements(By.XPATH, '//div[@data-testid="card-container"]')

casas = open("Nivel3/cuernavaca.txt", "w")

for titulo in resultados:
    try:
        casa = titulo.find_element(By.XPATH, './/div[@data-testid="listing-card-title"]').text
        precio = titulo.find_element(By.XPATH, './/div[@class="_tt122m"]').text
        resultado = f"Nombre: {casa}, Precio: {precio}\n"
        casas.write(resultado)
    except Exception as e:
        casas.write(f"Ocurrió un error al extraer la información {e}\n")