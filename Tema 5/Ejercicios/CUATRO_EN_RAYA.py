import os

def impresion(tablero, turno):
    os.system("cls")

    print("\t1  2  3  4  5  6")
    print("\t----------------")
    for fila in tablero:
        print("\t", end="")
        for casilla in fila:
            print(casilla+"  ", end="")
        print()

    print("\t----------------")

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

tablero = [[".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", "."]]
impresion(tablero, 1)

i = 1
while any(valor == "." for valor in tablero[0]):
    if i%2 == 0: jugador = "X"
    else :       jugador = "O"

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