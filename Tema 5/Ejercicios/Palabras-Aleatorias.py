#Importo la función random
from random import *

#Creo estas 3 listas para tener un poco de juego de probabilidad,
#separando las consonantes (de forma arbitraria) en probables y no probables
consonantesProbables = ["B", "C", "D", "F", "G", "H", "J", "L", "M", "N", "P", "R", "S", "T", "V"]
consonantesNoProbables = ["K", "Ñ", "Q", "W", "X", "Y", "Z"]
vocales = ["A", "E", "I", "O", "U"]

#Con este método elijo (con 25% de probabilidades para las no probables), la consonante
def consonantes():
    if randint(0, 3) == 3:
        return choice(consonantesNoProbables)
    else:
        return choice(consonantesProbables) 

#Decorador para elegir n palabras como marque arg dentro de una lista de m palabras aleatorias
def miDecorador(arg1, arg2 = 30):
    if arg1 > arg2:
        print("El arg1 (valores elegidos), debe ser menor a arg2 (valores generados)")
        return None;

    def decoraGenerador(function):
        generado = []
        elegido = []
        for i in range(arg2):
            generado.append(function())
        
        for i in range(arg1):
            elegida = choice(generado)
            elegido.append(elegida)
            generado.remove(elegida)

        return elegido
    return decoraGenerador


@miDecorador(10, 30)
def generaPalabra():
    #Establezco un numero de silabas para la palabra
    nSilabas = randint(1, 5)
    palabra = ""
    for i in range(nSilabas):
        #Con este numero decido si la sílaba será de consonante+vocal (50%), si será
        #solo consonante (25%) o si será solo vacal (25%)
        nAleat = randint(0,3)

        #Entro las veces que sale y en las que la palabra solo tiene una sílaba (para que no sea solo una letra)
        if nAleat > 1 or nSilabas == 1: palabra += consonantes()+choice(vocales)
        
        elif nAleat == 1: palabra += consonantes()
        
        else: palabra += choice(vocales)
    
    return palabra


def numerosSinRepetir(cantNumeros = 5, numMin = 1, numMax = 50):
    generados = []
    for i in range(cantNumeros):
        nGen = randint(numMin, numMax)

        if generados.count(nGen) == 0:
            generados.append(nGen)
            yield nGen
        else:
            i = i - 1


print("Palabras generadas y elegidas:")
print("==============================")

for i in generaPalabra:
    print(i)

print("\n\nLos numeros generados no repetidos:")
print("===================================")

cantNumeros = 5
numeros = numerosSinRepetir(cantNumeros, 1, 5)
for i in range(cantNumeros):
    print(next(numeros))