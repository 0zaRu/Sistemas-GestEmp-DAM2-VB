import os

def impresion(tablero, turno):
    i = 1
    print("    1   2   3  ")
    print("  -------------")
    for fila in tablero:
        print(i,"|", end="")
        for casilla in fila:
            print(" "+casilla+" |", end="")
    
        print()
        print("  -------------")
        i+=1
        
    if turno%2 == 0:print("\nEs el turno de X")
    else:print("\nEs el turno de O")
    
    print("(1H, 2V --> EJ: 23)")

def nuevoMovimiento(nMovimiento, tablero):
    h, v = input("Introduce la jugada: ")
    x, y = int(h)-1, int(v)-1
    
    if x < 0 or y < 0 or x > 2 or y > 2 or tablero[x][y] != " ":
        return False, tablero 
    
    if nMovimiento%2==0:
        tablero[x][y] = "X"
    else:
        tablero[x][y] = "O"
    
    return True, tablero

def comprueba3Enraya(tablero):
    contX1, contO1, contX2, contO2, contDX1, contDO1, contDX2, contDO2 \
        = 0, 0, 0, 0, 0, 0, 0, 0;

    for i in range(3):
        for j in range(3):
            if tablero[i][j] == "X": contX1+=1
            if tablero[i][j] == "O": contO1+=1
            if tablero[j][i] == "X": contX2+=1
            if tablero[j][i] == "O": contO2+=1
        
        if tablero[i][i] == "X": contDX1+=1
        if tablero[i][i] == "O": contDO1+=1
        if tablero[i][len(tablero)-i-1] == "X": contDX2+=1
        if tablero[i][len(tablero)-i-1] == "O": contDO2+=1
        
        if 3 in [contX1, contO1, contX2, contO2, contDX1, contDO1, contDX2, contDO2]:
            return True
        else:
            contX1, contO1, contX2, contO2 = 0, 0, 0, 0
    
    return False


os.system("cls")
tablero = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
impresion(tablero, 1)

i = 0

while i<9:
    i+=1
    valido, tablero = nuevoMovimiento(i, tablero)
    
    if valido is True:
        os.system("cls")
        impresion(tablero, i+1)
    else:
        print("El rango de valores introducido no es correcto o "\
            "ya hay colocada una ficha...\n\n")
        i -= 1
    
    if comprueba3Enraya(tablero) and i>=5:
        if i%2 == 0:
            print("\nEnhorabuena!, ha ganado el jugador X\n"\
                    "====================================\n")
        else:
            print("\nEnhorabuena!, ha ganado el jugador O\n"\
                    "====================================\n")    
        break;
        
else:
    print("\nEMPATE, NINGUNO DE LOS JUGADORES HA GANADO\n"\
            "==========================================\n")