"""
Diccionarios

Los elementos son pares: Una clave y un valor
Accedo a los valores a través de las claves
El acceso a los elementos es rápido
"""
d = {
    "nombre": "Marco",
    "edad": 19
}

d["apellido"] = "Perez"
del d["edad"]
d["edad"] = 20
d["edad"] += 10
print( d["edad"])
print(d)

for k, v in list(d.items()):
    print(k, v)

d = {
    "nombre": ["Hola Mundo", 19],
    "edad": {
        "edad de papa": 29,
        "nombre2": "alonso"
    }
}

print(d["edad"]["edad de papa"])
print(d["nombre"][0])