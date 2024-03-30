"""
Listas

Colecciones: Son estructuras donde yo puedo almacenar más de un valor
Sus índices empiezan en 0 y los negativos de -1
"""
numeros = [9, 6, 1, 3, 5]

numeros.append(10)
numeros.remove(6)
numeros.pop(1)

numeros[0] = 10
numeros[0] += 11

print( len(numeros) )
print( numeros.index(10) )
print( 10 in numeros)

numeros.sort()
numeros.reverse()

for i in numeros:
    print(i)

for i in range(len(numeros)):
    print(i)

print( numeros )