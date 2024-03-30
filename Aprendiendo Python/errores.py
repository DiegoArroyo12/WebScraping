cadena = "Hola"
try:
    x = int(cadena)
except Exception as e:
    print("Ha habido un error", e)
print("He llegado al final")

try:
    x = "Hola Mundo"
    print(x)
    print(x, z)
except:
    print("Ha ocurrido un error")
finally:
    print("END")