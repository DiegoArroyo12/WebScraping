"""
Conjuntos

No mantienen un orden ( no tienen indices )
no almacenan elementos repetidos
"""
conjunto = {1, 5, 9}

conjunto.add(10)

print(5 in conjunto)

conjunto2 = {1, 5, 10, 2}

print(conjunto.union(conjunto2))

print(conjunto)