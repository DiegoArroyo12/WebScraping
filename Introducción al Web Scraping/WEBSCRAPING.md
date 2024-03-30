# ¿Qué es WEB SCRAPING?
Es la extracción de datos de la Web de una manera automática utilizando programas de computadoras (software).

### Ventajas del WEB SCRAPING
- No dependo de APIs
- Puedo extraer datos de casi cualquier página web

### Desventajas del WEB SCRAPING
- Dependo de la estructura visual de la página web
- Si la página web se actualiza, yo tengo que actualizar mis programas para seguir extrayendo datos de manera correcta
- Las páginas pueden detectar mi actividad de extracción de datos, y pueden prohibirme el acceso

## HTML
Es un lenguaje de marcado que utiliza para el desarrollo de páginas de Internet. Sus siglas significan: HyperText Markup Language

## URL
Secuencia de caracteres que identifica y permite localizar y recuperar una información determinada de internet.

### Protocolo
- HTTP: Inseguro
- HTTPS: Seguro

### Dominio
Es un nombre único que identifica a un subárea de Internet

### Endpoint
Identifica que acción va a realizar el servidor web (/search/usuario)

### Parámetros
Inician después del símbolo (?) y son información adicional que va a utilizar el servidor para responder nuestro requerimiento, se juntan los parámetros con el símbolo (&).

## Nivel 1: Web Scraping estático de una sola página
### Librerías:
- Requests
- Beautiful Soup
- Scrapy

## Nivel 2: Web Scraping estático con varias páginas
### Librerías:
- Scrapy

## Nivel 3: Web Scraping Dinámico
### Librerías:
- Selenium Pyhton

## Nivel 4: Web Scraping de APIs

## Nivel 5: Autenticación, Captchas y iFrames

# Pasos del Web Scraping
- Paso 1: Definir URL semilla
- Paso 2: Realizar un REQUEST a la URL semilla
- Paso 3: Obtener la respuesta del servidor
- Paso 4: Extraer datos del HTML (XPATH)
- Paso 5: Volver al paso 2 con otras URLs

# XPATH
Es un lenguaje que permite construir expresiones que recorren y procesan un documento XML. Cabe recalcar que, un HTML es un documento de tipo XML.

xpather.com

//: Búsqueda en cualquier nivel del documento
/: Búsqueda en el nivel raíz
./: Búsqueda relativa

//h1[@id="titulo" and @class="subtitulo] Búsqueda con atributo

//div[@class="container container-uno"]/li/span

### Funciones de xpath
contains(@class, "elemento") Si en la clase contiene ese elemento
starts-with()
ends-with()
text()

### Obtener información específica de los tags
//h1[contains(text(), "This is")]/text() Devuelve únicamente el texto que contiene el h1 que cumpla con las características especificadas

//h1[contains(text(), "This is")]/@class Devuelve la clase

# devhints.io/xpath

# Ética
Hay que tener cuidado al hacer web scraping, porque podemos tirar servidores y hacer ataques Ddos, al igual que extraer información que no deberías ser pública.

## Dirección IP
Una dirección Ip es un conjunto de números que identifica de forma única a un dispositivo dentro del internet. Todas sus computadoras poseen su propia IP.