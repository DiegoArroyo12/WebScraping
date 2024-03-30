"""
Función

Formalmente, es un bloque de código con un nombre asociado, que puede recibir argumentos de entrada. 
Una vez llamada por su nombre, la función ejecuta una serie de sentencias utilizando los parámetros de entrada
y devuelve un valor y/o realiza una tarea.
"""
def suma(lista):
    x = 0
    for i in lista:
        x += i
    return x

print(suma([1,2,3,4,4,55,6]))