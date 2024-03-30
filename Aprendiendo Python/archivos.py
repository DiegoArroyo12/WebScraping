"""
r => leer
a => agregar
w => escribir
"""
f = open("Aprendiendo Python/archivo2.txt", "w")

#print( f.readlines() )

"""
Leer un archivo 'r'

for line in f:
    line = line.strip()
    line = line.split(',')
    print(line)
"""
"""
Agregar a un archivo 'a'
f.write("Manzana,10,10")
"""
"""
Crear un nuevo archivo 'w'
"""
f.write("Hola Mundo!")