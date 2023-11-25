# chr(27)+"[9;31m"+"X"+chr(27)+"[0;37m"
#recuerda esto cuando se toca un barco

import os
from random import *

nBarcos = {
    "C": [4, 1],
    "T": [3, 2],
    "D": [2, 3],
    "U": [1, 4]
}

class Tablero():
    t = []

    def __init__(self, nTablero = 2, nLineas = 10, nColumnas = 10, valorCasilla = " "):
        tableros = []
        for i in range(nTablero):
            tablero = []
            for j in range(nLineas):
                columna = []
                for k in range(nColumnas):
                    columna.append(valorCasilla)
                tablero.append(columna)
            tableros.append(tablero)
        self.t = tableros

def impresion(tableros, turno):
    #os.system("cls")

    cont = 0
    print("\t     a   b   c   d   e   f   g   h   i   j \t"*2)
    print(("\t   ╔"+("═══╦")*9+"═══╗ \t")*2)
    
    for filaT1, filaT2 in zip(tableros[0], tableros[1]):
        
        print("\t",cont,"║", end="")
        for casilla in filaT1:
            print(" "+casilla+" ║" if casilla != "." else "   ║", end="")
            #print(" "+casilla+" ║", end="")
        
        print("\t\t",cont,"║", end="")
        for casilla in filaT2:
            print(" "+casilla+" ║" if casilla != "." else "   ║", end="")
            #print(" "+casilla+" ║", end="")
    
        print()
        if cont != 9: print(("\t   ╠"+("═══╬"*9)+"═══╣ \t")*2)
        cont+=1
    
    print(("\t   ╚"+("═══╩"*9)+"═══╝ \t")*2)
    print((" ")*27+"JUGADOR 1"+(" ")*47+"JUGADOR 2\n\n")

def rodeaCasilla(t, h, v):
    #tuuve algun idea de hacerlo con dos listas en 2 bucles anidados haciendo los conjuntos
    #de posiblidad de [-1, 0, 1] para h y v pero no me terminó de salir, cuando lo consiga modificaré la entrega

    if h+1 < len(t) and v   < len(t[0]) and t[h+1][v]   == " ": t[h+1][v]   = "."
    if h+1 < len(t) and v+1 < len(t[0]) and t[h+1][v+1] == " ": t[h+1][v+1] = "."
    if h+1 < len(t) and v-1 > 0         and t[h+1][v-1] == " ": t[h+1][v-1] = "."
    if h   < len(t) and v+1 < len(t[0]) and t[h]  [v+1] == " ": t[h]  [v+1] = "."
    if h   < len(t) and v   > 0         and t[h]  [v-1] == " ": t[h]  [v-1] = "."
    if h-1 > 0      and v   < len(t[0]) and t[h-1][v]   == " ": t[h-1][v]   = "."
    if h-1 > 0      and v+1 < len(t[0]) and t[h-1][v+1] == " ": t[h-1][v+1] = "."
    if h-1 > 0      and v   > 0         and t[h-1][v-1] == " ": t[h-1][v-1] = "."

    return t

def gestionaEspacio(t, horizontal, letraBarco, tBarco, pH, pV):
    #primero compruebo que en los espacios se puede poner un barco
    for i in range(tBarco):
        if horizontal:
            if t[pH+i][pV] != " ": return False, t
        if not horizontal:
            if t[pH][pV+i] != " ": return False, t
    
    #luego lo pongo
    for i in range(tBarco):
        if horizontal:
            t[pH+i][pV] = letraBarco

        if not horizontal:
            t[pH][pV+i] = letraBarco

    #rodeo con puntos, filtrando por la letra del barco actual para evitar dar vueltas de más
    for i in range(len(t)):
        for j in range(len(t[0])):
            if t[i][j] not in {" ", "."} and t[i][j] == letraBarco: t = rodeaCasilla(t, i, j)

    return True, t

def generaBarcos(t):
    #recorro el diccionario de barcos
    for n, v in nBarcos.items():        
        pH, pV = -1, -1
        #doy tantas vueltas como barcos haya que poner del tipo en el que estamos
        for cantBarcos in range(v[1]):
            #establezco la orientación del próximo barco
            horizontal = True if randint(0, 1) == 0 else False
            salir = False

            #doy vueltas seleccionando casillas hasta encontrar una válida y colocar el barco
            while not salir:
                pH = randint(0, len(t)-v[0]) if horizontal else randint(0, len(t)-1)
                pV = randint(0, len(t[0])-v[0]) if not horizontal else randint(0, len(t[0])-1)

                salir, t = gestionaEspacio(t, horizontal, n, v[0], pH, pV)
    
    return t

""" METODOS QUE FALTA IMPLEMENTAR
def nuevoMovimiento(tablero, jugador):
    try:
        y = int(input("\n\tEs el turno de "+jugador+".\n\tIntroduce el nº de columna: "))-1
        if y < 0 or y > 6:
            return False, tablero 
        
        for i in range(7):
            if tablero[6-i][y] == ".":
                tablero[6-i][y] = jugador
                return True, tablero
        
    except:
        pass

    return False, tablero

def compruebaCasilla(x, y, tablero):
    rangos = [[".", ".", ".", "."], [".", ".", ".", "."], [".", ".", ".", "."], [".", ".", ".", "."]]
    
    for i in range(4):
        if y+i <= 5: rangos[0][i] = tablero[x][y+i]      #Comprueba vertical creciento
        if x+i <= 6: rangos[1][i] = tablero[x+i][y]      #Comprueba horizontal derecha
        if y+i <= 5 and x+i <= 6: rangos[2][i] = tablero[x+i][y+i] #Comprobar diagonal creciente derecha
        if y+i <= 5 and x-i >= 0: rangos[3][i] = tablero[x-i][y+i] #Comprobar diagonal creciente izquierda
        
    for i in range(4):
        if all(valor == "X" for valor in rangos[i]) or all(valor == "O" for valor in rangos[i]): 
            return True
    
    return False

def comprueba4Enraya(tablero):
    for i in range(7):
        for j in range(6):
            if tablero[i][j] != "." and compruebaCasilla(i, j, tablero):
                return True
    
    return False
"""

t = Tablero(2, 10, 10, " ")

t.t[0] = generaBarcos(t.t[0])
t.t[1] = generaBarcos(t.t[1])

impresion(t.t, 1)


""" JUGABILIDAD QUE FALTA POR IMPLEMENTAR
i = 1
while True:
    if i%2 == 0: jugador = "Jugador 1"
    else :       jugador = "Jugador 2"

    valido, tablero = nuevoMovimiento(tablero, jugador)    

    if valido is True:
        impresion(tablero, i+1)
    else:
        print("\tRango de valores introducido no es correcto, "\
            "ya hay colocada una ficha o el carácter no es válido ...\n\n")
        i -= 1

    if comprueba4Enraya(tablero) and i>=4:
        print("\n\tEnhorabuena!, ha ganado el jugador "+jugador+"\n"\
                "\t====================================\n")
        break
    
    i+=1    
else:
    print("\n\tEMPATE, NINGUNO DE LOS JUGADORES HA GANADO\n"\
            "\t==========================================\n")
            
"""