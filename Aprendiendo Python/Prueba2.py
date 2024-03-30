edadLeonardo = 24
tipo = "Niño"
if edadLeonardo > 12 and edadLeonardo <= 21:
    tipo = "Adolescente"
elif edadLeonardo > 21 and edadLeonardo <= 65:
    tipo = "Adulto"
else:
    tipo = "Adulto Mayor"

print(tipo)

print("Programa 1")
x = 24
y = "A"
if x > 0 and x < 24:
    y = y + "B"
elif x >= 24 and x < 45:
    y = y + "C"
elif x >= 45 and x < 60:
    y = y + "D"
else:
    y = "Z"

print(y)

print("Programa 2")

x = 24
y = "A"
if x > 0 and x <= 24:
    y = y + "B"
if x >= 24 and x < 45:
    y = y + "C"
if x >= 45 and x < 60:
    y = y + "D"
else:
    y += "Z"

print(y)

print('Problema 3')
from random import randint
temperatura = randint(0, 40)
if temperatura <= 18:
    print("Clima Tropical")
if temperatura >= 18:
    print('Que calor!')
if temperatura == 18:
    print('Templado')
else:
    print('Frio o Calor')

print("Problema 4")
d = [0, 1, 2, 3, 4, 5, 6]
e = d
e[-1] = 50
d[2] = 40
print(d)

print('Problema 5')
l = [10, 30, 50, 70]
l += l[-1:-3]
print(l)

print('Problema 6')
cadena = "anita lava la tina"
tmp = []
for c in cadena:
    tmp.append(c)
tmp.reverse()
nuevaCadena = "".join(tmp)
print(nuevaCadena)