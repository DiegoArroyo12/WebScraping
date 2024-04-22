# API
Una API (Application Programming Interface o Interfaz de Programación de Aplicaciones) es un conjunto de reglas y protocolos que permiten a diferentes aplicaciones comunicarse entre sí. 

En otras palabras, una API define cómo interactuar con un software o servicio para utilizar sus funcionalidades y datos de manera programática.

### Aquí hay algunos puntos clave sobre las APIs:

1. **Comunicación entre sistemas:** Las APIs permiten que dos sistemas informáticos se comuniquen y compartan información de manera eficiente, incluso si están escritos en diferentes lenguajes de programación o se ejecutan en diferentes plataformas.
Estandarización: Las APIs suelen seguir estándares y convenciones que facilitan su uso y comprensión por parte de desarrolladores externos. Esto incluye la documentación detallada de los endpoints, métodos disponibles, parámetros requeridos y formatos de respuesta.

2. **Abstracción de la complejidad:** Las APIs ofrecen una capa de abstracción que oculta la complejidad interna de un sistema o servicio. Esto permite a los desarrolladores interactuar con las funcionalidades y datos sin necesidad de conocer todos los detalles internos de implementación.

3. **Reutilización de código:** Al exponer funcionalidades a través de una API, se facilita la reutilización de código y la integración de diferentes sistemas y servicios, lo que promueve la modularidad y la escalabilidad en el desarrollo de software.
Integración de servicios: Las APIs son fundamentales para la integración de servicios web, el desarrollo de aplicaciones móviles, la automatización de procesos y la creación de ecosistemas de software interoperables.

En resumen, una API proporciona una interfaz estandarizada y controlada para acceder y utilizar funcionalidades y datos de un sistema o servicio de manera programática, lo que facilita la comunicación y la integración entre diferentes aplicaciones y componentes de software.

### Ventajas de la extracción por APIs:
1. No dependo del HTML de la página web.
2. Recibo la información limpia y estructurada en formato JSON.

### Desventajas de la extracción por APIs:
1. No todas las Webs me proveen de un API público documentado.

Una API puede retornar información en diferentes formatos, tales como:
- XML
- JSON

Posteriormente se nos muestran ya procesados en una interfaz gráfica.

La API permite al proveedor proteger sus procedimientos y proteger sus datos.

Utilizan la autenticación ``BASIC AUTH`` y ``OAUTH2``.

# JSON
JSON: JavaScript Object Notation.

Es un formato de texto sencillo para el intercambio de datos. Se trata de un subconjunto de la notación de objetos en JavaScript. Es comúnmente utilizado para transmitir datos en aplicaciones web (Por ejemplo: Enviar algunos datos desde el servidor al cliente así estos datos pueden ser mostrados en páginas web, o viceversa).

Los archivos JSON son muy parecidos a los diccionarios de **Python**.

### Ventajas de JSON:
1. Es muy sencillo de leer y entender.
2. Es un formato compacto.
3. Ser compacto lo hace un formato de transmisión rápida por su peso ligero.
4. Compatibilidad directa con los objetos de JavaScript.

# REST
Es una lógica de restricciones y recomendaciones bajo la cual se construcce una API, se puede decir que es un estilo de arquitectura.

**REST** (**RE**presentational **S**tate **T**ransfer)

# RESTful API
Es una **API** ya implementada utilizando que esta construida con la lógica de **REST**.
Funcionan estrictamente bajo una arquitectura cliente servidor, utilizando **HTTP** como protocolo de comunicación. 

En esta comunicación un cliente puede ser nosotros, utilizando y realizando requerimientos desde una aplicación web o móvil y el servidor es el que realizará nuestros requerimientos y ejecutará las acciones acorde a nuestra petición.

En REST cada procedimiento en nuestra API esta compuesto por 3 requerimientos importantes:
1. Un verbo HTTP
    
    Son identificadores que detectan el objetivo de un requerimiento del cliente.
    - GET:
        
        Se utiliza para los procedimientos que devuelven información al cliente.
    - POST:

        Se utiliza para que el cliente pueda crear recursos dentro del servidor.
    - PUT / PATCH

        Se utiliza para que el cliente pueda editar recursos ya existentes dentro del servidor.
    - DELETE

        Se utiliza para eliminar recursos dentro del servidor.

2. Una dirección URI única (http://mypage.com/api/v1/photo)


3. Datos (Información y Autentificacion del Cliente)

Se dice que REST es **STATELESS** ya que no se necesita guardar información o el estado de peticiones anteriores para poder satisfacer nuevas peticiones, cada petición es independiente de otras.

Sin embargo la arquitectura REST si admite la implementación de caché para guardar las respuestas de peticiones realizadas con anterioridad y de esta forma poder utilizarlas para poder satisfacer nuevas peticiones de los mismos recursos de manera rápida, esto con el método GET.

### **DataFrame:**

Estructura de datos ordenada compuesta por filas y columnas en donde cada columna y cada fila se encuentra identificada por un índice.
Este índice puede ser un número o una cadena de texto.
Cada columna tiene que tener datos del mismo tipo. Se asemeja a una en una BDD o un libro de excel.

## iFrame
Es un tag HTML que me permite insertar un documento HTML dentro de un documento HTML principal.

## TAGS Scripts
Contienen código en lenguaje JavaScript que puede contener información que posteriormente se carga en el DOM.

#### **Codificación (Encoding)**
Convertir un carácter de algún alfabeto de tal forma que un programa lo pueda entender y mostrar.

#### **UTF-8**
Es un formato para codificar caracteres. Soporta la gran mayoría de alfabetos tradicionales de diferentes lenguajes del mundo.