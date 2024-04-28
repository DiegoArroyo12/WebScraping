# ÉTICA

En el curso hicimos extracciones muy pequeñas, pero cuando queramos hacer extracciones más grandes como por ejemplo, 6,000 u 10,000 datos o cantidades de esa magnitud, debemos ser cuidadosos y responsables, ya que por nuestra culpa puede colapsar el servidor de la página que estamos extrayendo.

### Si nosotros no ocupamos precauciones como lo son: 
- TIMEOUT:

    Tiempo de espera antes de hacer un nuevo requerimiento.

- SEGMENTAR:

    Dividir en partes más pequeñas un proceso. Es decir si queremos extraer 10,000 datos, podemos divir la extracción en dos días y cada día extraer 5,000 datos aplicando la precaución anterior del `TIMEOUT` en cada extracción.

Si no hacemos estás precauciones podríamos provocar un ataque DDoS a la página, **Distributed Denial of Service** y esto es ilegal.

Incluso si sobre pasamos las cuotas de requerimientos que nos dan las páginas, podemos ser baneados de IP (Identificador de nuestra computadora en Internet).

Si vamos a publicar u ocupar la data extraída, debemos `DAR CRÉDITO` siempre a las páginas de las que hemos extraído la información y cerciorarnos de que es legal publicar la información que hemos extraído.

Cada IP tiene una cuota de requerimientos que puede hacer en un sitio web, por ejemplo, supongamos que la cuota de requerimiento de Mercado libre es de 10 requerimientos por segundo y nosotros haciendo Web Scraping hacemos 10 requerimientos en 1 segundo, seremos baneados. Incluso pueden existir cuotas por día.

# Tips para no ser baneados:

1. Hacer nuestros requerimientos con un TIMEOUT.
2. Limitar la extracción de datos. 
3. Intentar humanizar nuestras extracciones, por ejemplo, el tiempo entre consultas debería ser randomizado. 
4. Intentar no hacer Web Scraping desde nuestras computadoras personales. (Utilizar Máquinas Virtuales)

**Máquina Virtual:**

Es un software que simula un sistema de computación y puede ejecutar programas como si fuese una computadora real. Cada máquina virtual tiene su propia IP.

# User Agents y VPNs

**User Agents:**

Son una cadena de texto con la cual se puede identificar el navegador y el sistema operativo del cliente. Este por default es **ROBOT** y esto hará que nos baneen de el sitio web, por ello debemos asignar una nosotros.

**VPN:** `Virtual Private Network`

Es una tecnología que permite conectar una computadora a una red privada virtual a través del Internet, de manera segura. Sin necesidad de que el cliente y la red esten conectados físicamente. 

Esta cambia nuestra IP, país y hasta proveedor de Internet, haciendo que si un sitio nos banea, solo baneara la IP del VPN y podremos cambiar de VPN y seguir extrayendo información 