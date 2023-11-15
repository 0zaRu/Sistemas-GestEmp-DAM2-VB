#LISTAS (end e spara reemplazar el caracter final, que suele ser un \n)
#aunque en el end parezca que se va a imprimir un espacio por usar la , es para diferenciar parametros, no anidar, por uso no pone espacio

letras = ["A", "B", "C"]
for i in letras:
    print(i, end="-")

#en este caso es necesario hacer rango, porque len devuelve un entero, entonces lo hacemos de forma tradicional
print()
letras = ["A", "B", "C"]
for i in range(len(letras)):
    print(letras[i], end="")

#otras formas
print()
for i in (0, 1, 2, 3, 4): 
    print(i) #0, 1, 2, 3, 4, 5

print()
#Rango range(inicio, fin, salto)

for i in range(6): 
    print(i, end=" ") #0, 1, 2, 3, 4, 5

print()
for i in range(5, 20, 2):
    print(i, end=" ") #5,7,9,11,13,15,17,19

print()
for i in range (5, 0, -1): 
    print(i, end=" ") #5,4,3,2,1
