# AUTENTICACIÓN
Es el proceso de confirmar que alguien es quien dice ser. Este alguien lo hace a través de sus credenciales, o a veces a través de una autenticación de doble factor (confirmación por sms o email).

Va muy de la mano con la extracción de datos a través de APIs.

Al ingresar en una página como por ejemplo Facebook, necesitamos ingresar nuestro usuario y contraseña, posteriormente presionar un botón de "Login" para que la página acceda únicamente a la información que corresponde a ese usuario y esa contraseña. 

Este botón de Login envía esta información al servidor y el servidor, si es que se mandaron bien los datos nos da el acceso únicamente a la información correspondiente a estos datos.

El servidor mantiene el acceso a su información por su sesión.

Manejaremos la autenticación para request con **BASIC AUTH**, aunque existen otros tipos de autenticación más complejos como **OAuth**.

Siempre que queramos intentar autenticarnos en un sitio con Web Scraping debemos estar completamente seguros de que ese sitio no tenga una API pública, como es el ejemplo de X o Facebook, que son sitios que ya proveen acceso a sus sitios e información y con una documentación muy buena de cómo hacer requerimientos a sus APIs y de cómo autenticarse y descargar información.
Es mejor aprender a usar las APIs de los sitios a intertar logearse con técmicas de Web Scraping.

También veremos cómo hacer exrtracción de datos a sitios web que utilizan Captchas.

### Anotaciones
---

#### GitHub Form y API

- Las sesiones dentro de cualquier página web tienen un tiempo limitado. Una vez que acabe la sesión tendré que iniciar sesión nuevamente para tener acceso a mi información. El navegador se encarga (en parte) de mantener las sesiones abiertas dentro de un sitio.

- Como regla general, podemos decir que los inicios de sesión siempre van a ser requerimientos de tipo POST, que envían la información del formulario de inicio de sesión al servidor para que sea validada.

- El atributo NAME dentro de cada tag INPUT indica el nombre de la propiedad con la cual van a viajar los datos al servidor dentro del requerimiento POST.

- Endpoint es la terminología correcta para cuando estamos hablando de APIs

#### Autenticación Scrapy

- Igual tenemos que investigar como se llaman los parámetros donde se ingresa el usuario y la contraseña. En este caso son "login" y "password", pero esto puede variar.

- Scrapy por defecto maneja la sesión una vez que ya la hemos iniciado. Asi como request.Session

# CAPTCHAS
Sus siglas significan: **Completely Automated Public Turing test to tell Computers and Humans Apart**.

En español: Prueba de Turing completamente automatizada para diferenciar computadoras y humanos.

Son pruebas que solamente pueden pasar humanos. Para evitar que los robots (nuestros scripts de extracción) hagan requerimientos de manera desmesurada a una página web.

### Formas de pasar los Captchas:

1. Solución Manual: 

    Lo resolvemos nosotros y posteriormente continuamos con la ejecución normal de nuestra extracción.

2. Solución Automática ($$$): 

    Contratar un solucionador de Captchas (2Captcha)

Actualmente es imposible pasar un Captcha con Requests o Scrapy asi que ocuparemos Selenium.

Los captchas (especialmente reCAPTCHA) tienen mecanismos muy sofisticados para detectar que estamos accediendo desde un navegador automatizado (Selenium).

Resolver un captcha manualmente implica parar nuestro script para resolver el captcha nosotros mismos manualmente. Luego, continuamos la ejecución.

### Pasos para resolver el Captcha con 2Captcha:

1. Inspecciona la página y encuentra el tag que contenga el atributo data-sitekey.
2. Con este valor realiza un requerimiento a nuestro API para resolver el captcha.
3. Te devolveremos un ID para consultarnos si tu captcha ya esta resuelto o no.
4. Espera mientras resolvemos tu captcha.
5. Con el ID llama a nuestro API y te diremos si ya resolvimos tu captcha o no.
6. Te devolveremos un TOKEN que lo tendrás que colocar en el HTML.

Cookies:

Los cookies son información que guarda un navegador al visitar una página. A veces, las páginas utilizan información en los cookies para validar requerimientos subsecuentes. En requests, manteniendo un Session podemos mantener los cookies.