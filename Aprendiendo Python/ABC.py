"Variables"
x = 5
variable = 30
_variable = 50
variablee2 = 40

Y = 5
y = 5

m, n = 1, 2

"Tipos de Datos"
x = 4 # int
y = 4.0 # float
variable = "Hola Mundo" # String
variable2 = 'Hola Mundo'
z = True # Booleano
m = False

# Casting: Es la acción de convertir una variable de un tipo a otro tipo de dato.

x = "1"

x = int(x)
x = str(x)
x = float(x)

y = "cadena"

y = int(y) # No se puede porque no es un dígito

x = 1
y = x
y = 2

"Operaciones Entre Variables"
x = 4
y = 5
x + y 
x * y
x / y
x // y
x & y

x = "cadena"
y = "cadena"

z = x + y

print(z)

x = 5

x = x + 1
x += 1

print(x)

"Salidas Por Pantalla"
x = "Hola Mundo"
y = "Hola "

print(x, y, "Chao", 4)

"Librerías"
"""
Es un conjunto de implementaciones ( funciones o pedazos de código ) hechas por alguien más, que me sirven para utilizarlas en mi programa.
Sin perocuparme como estan hechas. SOlo tengo que utilizarlas.

Importar: 
Significa traer un pedazo de código de otro lado ( en este caso, la librería ) hasta mi programa a través de un nombre.
Y, a través de este nombre puedo ejecutar ( o llamr ) a este código.
"""
import random

# Hay que poner el nombre de la librería
random.randint(1, 5)

from random import randint

# No es necesario poner el nombre de la librería pero solo tenemos acceso a el elemento que imoportamos
randint(1, 5)

from random import *

# Tampoco es necesario poner el nombre de la librería pero tenemos acceso a todos los elementos
randint(1, 5)

"Pedir Datos Al Usuario"
x = input("Ingresa un valor numérico: ")
print(x)
# Ingesan los datos siempre como string

"Condicionales"
"""
Operadores Lógicos:
Son operadores que nos dan un resultado a partir de que se cumpla o no una condición.
Es decir, su resultado solamente puede ser VERDADERO o FALSO ( Booleanos ).

- > Mayor que
- < Menor que
- >= Mayor o igual que
- <= Menor o igual que
- == Igaul que 
- != Distinto a 

Estructuras Condicionales
Son estructuras que, dependiendo del valor de una condición determinan si se ejectua o no un pedazo de código.
"""
if (x):
    # Código
    pass
elif (y):
    # Código
    pass
else:
    # Código
    pass

x = 5
y = 4

print( x > y ) # True
print( False or True)
print( True and True)

x = randint(1,5)

if x == 1:
    print("Hola soy el número 1")
elif x == 2:
    print("Hola soy el número 2")
else:
    print("Hola soy algún otro número")

print(x)