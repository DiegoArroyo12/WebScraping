cadena = "Hola Mundo"

print( len(cadena) )
print( cadena[0] )

for c in cadena:
    print( c )

print( cadena.lower() )

print( cadena.capitalize() )

print( cadena.startswith("Hola") )

print( cadena.endswith("Hola") )

print( cadena.isalnum() )

frutas = "Durazno, Manzanas, Papaya"

print( frutas.split(",") )

lista = frutas.split(",")
cadena2 = "-".join(lista)

print(cadena2)