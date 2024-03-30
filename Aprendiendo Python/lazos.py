"""
Lazos ( Bucles )

Son estructuras que me permiten repetir un mismo pedazo de código un cierto número de veces.
En Python existen dos:
For y While

For: Se usa cuando sabes cuántas veces vas a repetir el proceso
While: Se usa cuando no sabes cuántas veces vas a repetir el proceso, cuando se cumpla una condición
"""
from random import randint

x = 0
for i in range(10):
    x += randint(1,5)
    print(x)

x = randint(1, 100)

while x != 5:
    x = randint(1, 100)
    print(x)