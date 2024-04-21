# Para saber si una página carga de forma dinámica
Nos apoyamos de la pestaña de networks 

- Si vemos que el link no cambia con respecto al link que nos muestra el primer elemento que nos sale en el network, podemos deducir que la página no carga dinámicamente, comprobamos metiendonos al primer link y si tienen contenido similar entonces lo comprobaremos y podemos utilizar request o scrapy.
- Si vemos que el link no cambia con respecto al link que nos muestra el primer elemento que nos sale en el network, pero si entramos al primer link y el contenido no es similar al de la página semilla, entonces no podremos ocupar request o scrapy, tendremos que ocupar Selenium.
- Si vemos que el link no cambia con respecto al link que nos muestra el primer elemento que nos sale en el network, y si abrimos el primer link e intentamos interactuar con los elementos de la página, como por ejemplo un combobox, y está sin información, entonces no podemos utilizar request o scrapy, tendremos que ocupar Selenium.

## Ya que Request y Scrapy extraen la información de los primeros requerimientos del network podemos saber si es que podemos hacer WEBSCRAPING con estas herramientas o tendremos que utilizar en su defecto Selenium.

# Proxies en Selenium
Similar a como hicimos en Scrapy, también es posible utilizar proxies en Selenium. El concepto es el mismo. Todos los requerimientos pasan primero por un Proxy antes de ir a la página web.

Pueden encontrar un ejemplo en el cual he implementado el uso de Proxies en Zyte con la extracción de Mercado Libre aquí: https://github.com/lkuffo/web-scraping/blob/master/NIVEL%203/selenium_proxy.py

Y un tutorial completo aquí: https://www.zyte.com/blog/how-to-use-selenium-with-zyte-smart-proxy-manager/

Esta es una práctica a modo de guía debido a que este caso de uso es muy específico.

Los pasos resumidor para hacer que funcione:
1. Obviamente deben tener una cuenta Zyte. Otras herramientas como Zyte funcionan de manera similar.
2. Instalamos la librería necesaria que nos provee Zyte: ```pip install zyte-smartproxy-selenium```
3. La importamos: ```from zyte_smartproxy_selenium import webdriver```
    1. Utilizaremos esta importación en ves de: ```from selenium import webdriver```
    2. En efecto, esta librería es un wrapper del webdriver. Lo mismo hacen otras compañías que ofrecen servicio de Web Scraping con proxies.
4. La instanciación del chromedriver queda de la siguiente manera:
```
driver = webdriver.Chrome(
    service = Service(ChromeDriverManager().install()),
    options = opts,
    spm_options = {
        'spm_apikey': 'API_KEY_ZYTE',
        'static_bypass': False,
        'block_ads': True
    }
)
```
Como pueden ver, podemos seguir utilizando ```webdriver-manager```.

Donde dice ```API_KEY_ZYTE```, tenemos que poner nuestro API KEY proporcionado por Zyte.

## Otros detalles interesantes:
- Recuerden que la cantidad de requerimientos que salen a través del navegador es sumamente grande. Incluso pueden llegar a hacerse ~100 requerimientos a diferentes recursos cada vez que cargamos una página. Esto lo podemos ver evidenciado en el panel de **Networks** (cada fila es un requerimiento).

- Zyte nos da la opción de solamente utilizar el Proxy para el primer requerimiento (con la opción ```static_bypass: True```). En el código que les compartí la tengo puesta en ```True```. Teniéndola en True quiere decir que:

    - Su consumo de cuota de Zyte será mayor (cada fila en el panel de networks cuenta como un requerimiento)

    - La extracción será más lenta. Esto es debido a que cada requerimiento hace el doble de viajes (del cliente al proxy, del proxy al servidor, del servidor al proxy, del proxy al cliente).

    - Sin embargo, obviamente de este modo nos encontramos totalmente protegidos detrás del proxy. En lo personal pienso que hacerlo de otra manera implicaría los mismos riesgos que hacerlo sin un proxy. Ya que muchos de los requerimientos adicionales que hacen las páginas dinamicas van a un API que (en la gran mayoría de los casos) vive bajo los mismos mecanismos de defensa del servidor que sirve el primer requerimiento.

- Zyte también nos da la opción de bloquear los requerimientos hechos para obtener anuncios (ads), utilizando el parámetro ``block_ads``. Esto es esencialmente un ad-blocker. Zyte lo hace para evitar hacer requerimientos que traigan información basura y preservar la cuota.

    - Lo he seteado en ``True``. Sin embargo, como se imaginarán algunas páginas bloquean el uso de ad-blockers. En este caso deben setearla a ``False`` para no bloquear los ads.