import os

def impresion(tablero, turno):
    
    i = 1
    print("\t1  2  3  4  5  6")
    print("\t----------------")
    for fila in tablero:
        print("\t", end="")
        for casilla in fila:
            print(casilla+"  ", end="")
        print()
        i+=1

    print("\t----------------")
        
    if turno%2 == 0:print("\n\tEs el turno de X")
    else:print("\n\tEs el turno de O")
    
    print("\tIntroduce el nº de columna:")

def nuevoMovimiento(nMovimiento, tablero):
    try:
        y = int(input("\tIntroduce la jugada: "))-1
        
        if y < 0 or y > 6:
            return False, tablero 
    
        valido = False
            
        if nMovimiento%2==0: jugador = 'X'
        else: jugador = 'O'
        
        for i in range(7):
            if tablero[6-i][y] == '.':
                tablero[6-i][y] = jugador
                valido = True
                break
        
        if valido == False:
            return False, tablero
        
        return True, tablero
    except:
        return False, tablero

def compruebaCasilla(x, y, tablero)
    rangos = [["", "", "", ""], 
              ["", "", "", ""], 
              ["", "", "", ""], 
              ["", "", "", ""], 
              ["", "", "", ""], 
              ["", "", "", ""], 
              ["", "", "", ""], 
              ["", "", "", ""], ]
    
    for i in range(4):
        rangos[0][i] = tablero[x][y+i]      #Comprueba horizontal positiva
        rangos[1][i] = tablero[x][n = if y-i >=0]      #Comprueba horizontal negativa





def comprueba4Enraya(tablero):
    for i in range(6):
        for j in range(7):
            if tablero[i][j] != ".":
                if compruebaCasilla(i, j, tablero):
                    return True
    
    return False




os.system("cls")
tablero = [[".", ".", ".",".", ".", "."], 
           [".", ".", ".",".", ".", "."], 
           [".", ".", ".",".", ".", "."], 
           [".", ".", ".",".", ".", "."], 
           [".", ".", ".",".", ".", "."], 
           [".", ".", ".",".", ".", "."], 
           [".", ".", ".",".", ".", "."]]


impresion(tablero, 1)

i = 0
victoria = False;
while victoria == False:
    i+=1
    valido, tablero = nuevoMovimiento(i, tablero)
    
    if valido is True:
        os.system("cls")
        impresion(tablero, i+1)
    else:
        print("\tRango de valores introducido no es correcto, "\
            "ya hay colocada una ficha o el carácter no es válido ...\n\n")
        i -= 1
    
    """
    if comprueba3Enraya(tablero) and i>=5:
        if i%2 == 0:
            print("\nEnhorabuena!, ha ganado el jugador X\n"\
                    "====================================\n")
        else:
            print("\nEnhorabuena!, ha ganado el jugador O\n"\
                    "====================================\n")    
        break;
    """
        
else:
    print("\nEMPATE, NINGUNO DE LOS JUGADORES HA GANADO\n"\
            "==========================================\n")