d1 ={
    "Nombre":"Sara",
    "Edad": 27,
    "Documento":101010,
    "notas":[10, 6, 5]
}

#podemos buscar directamente con los [] como si fuese un array o con la función .get()
print(d1['Nombre']) #Sara
print(d1.get('Nombre')) #Sara

#también se puede modificar la información
d1['Nombre'] = "Laura"
print(d1)   #{'Nombre': Laura', 'Edad': 27, 'Documento': 1003882}

#podemos recorrerlo con un for
for x in d1:
    print(x)

#ese for anterior solo recorre las claves, porque los diccionarios tienen dos posiciones de información

print()
#este recorre los datos
for x in d1:
    print(d1[x])

print()
#y este lo da todo, apoyandose en el metodo items para poderlos recorrer sin llamar con []
for x, y in d1.items():
    print(x, y)

#aunque podríamos
for x in d1:
    print(d1, d1[x])