#CONDICIONALES IF ELSE ELIF  ################################################################################
a=6

if a > 5:
    print("Es mayor que 5"); print("Dentro del if")
else:
    print("Es menor que 5"); print("Dentro del else")

if a < 5:
    print("Es menor que 5"); print("Dentro del if")
else:
    print("Es mayor que 5"); print("Dentro del else")

a = 5

if (a < 5):
    print("Es menor que 5"); print("Dentro del if")
elif a == 5 :
    print("Es igual que 5"); print("Dentro del if")
else:
    print("Es mayor que 5"); print("Dentro del else")







#CONDICIONAL SWITCH #######################################################################################
#NO LOS VOY A COPIAR, PERO HAY MUCHOS SWITCH QUE SE SIMULAN CON IF ELIF ELSE, METODOS, O LA MEZCLA DE AMBAS

#es especifico este de lambdas no va o no se usarlo
def opera(operador, a, b):
    return {
        'suma':lambda: a+b,
        'resta':lambda: a-b,
        'multiplica':lambda: a*b,
        'divide':lambda: a/b
    }.get(operador, lambda:None)    

print()
print(opera('suma', 10, 2))
print()

#switch con diccionarios
tabla_switch = {
    '0': '000',
    '1': '001',
    '2': '010',
    '3': '011',
    '4': '100',
    '5': '101',
    '6': '110',
    '7': '111',
}

def usaDiccionario(decimal):
    return tabla_switch.get(decimal)

#input devuelve siempre cadenas, así que habría que hacer castings para almacenarlo de otra forma
print()
#print(usaDiccionario(input("introduce un numero entre 0 y 7: ")))
#lo he comentado para no tenerlo que meter al ejecutar siempre






#BUCLES E ITERADORES ####################################################################################
print()
cadena = 'Cadena prueba'

for i in cadena:
    print("caracter:", i)


#Comprobacion de "iterables" para saber si se puede recorrer de forma habitual o no, x información
print()
from typing import Iterable
lista = [1, 2, 3, 4] 
cadena = "Python" 
numero = 10 
print(isinstance(lista, Iterable)) #True 
print(isinstance(cadena, Iterable)) #True 
print(isinstance(numero, Iterable)) #False

#Hacer las cosas iterables
print()
lista = [5, 6, 3, 2]
it = iter(lista)
print(it) #<list_iterator object at 0x...>
print(type(it)) #<class 'list_iterator'>


#utilizar función next
print()
lista = [5, 6, 7]
it1 = iter(lista)
it2 = iter(lista)
print(next(it1)) #5
print(next(it1)) #6
print(next(it1)) #7
# print(next(it1))   daría error, porque se sale del tamaño de la lista
print(next(it2)) #5





##############################################################################
#Bucle for
#bucles anidados (recorrer matrices)
#en este caso, tenemos hasta dimensione diferentes, y podemos recorrerlo igual con las comprobaciones suficientes
print()
lista = [[[56, 34, 62], 34, 1], [12, 4, 5], [9, 4, 3]]

for i in lista:
    print("i vale:",i)
    for j in i:
        print("\tj vale:",j)
        if type(j) == list:
            for k in j:
                print("\t\tk vale:",k)
    print()


#recorrido con salto 
print()
texto = "Python"
for i in texto[::-1]:
    print(i) #n,o,h,t,y,P


print()
texto = "Python"
for i in texto[::2]:
    print(i) #P,t,o

#recorrido de numeros enteros
print()
a = range(5)

for i in a:
    print(i)

print()
for i in range(4, 8):
    print(i)

#puedo hacer un factorial solo aplicando el metodo sum a un rango
print()
print(sum(a)) #son 4 vueltas y no 5, porque es del 0 al 4, así que da 10

#puedo hacer cosas muy raras:
print()
print(sum(i for i in range(10)))







##############################################################################
#WHILE
print()
x = 5 
while x > 0: 
    x -= 1
    print(x) 

#en este caso, el while será siempre i cuando queden elementos (pop los saca desde "arriba")
print()
x = ["Uno", "Dos", "Tres"] 
while x: 
    print("popeado: ["+x.pop(0)+"]\trestante: ", x, end=" ") 
    print()


# WHILE ELSE que cojones
print()
x = 5
while x > 0: 
    x -=1 
    print(x, end=" ") #4,3,2,1,0 

else: 
    print()
    print("El bucle ha finalizado")


# más bucles anidados
z = 7 
x = 1 
while z > 0: 
    print(' ' * z + '*' * x + ' ' * z) 
    x+=2 
    z-=1
