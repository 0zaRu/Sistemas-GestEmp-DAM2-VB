def impresion(tablero):
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
    
    print("\n(1H, 2V --> EJ: 23)")

def nuevoMovimiento(nMovimiento, tablero):
    h, v = input("Introduce la jugada: ")
    x, y = int(h), int(v)
    
    if x < 1 or y < 1 or x > 3 or y > 3:
        return False, tablero 
    
    if nMovimiento%2==0:
        tablero[x-1][y-1] = "X"
    else:
        tablero[x-1][y-1] = "O"
    
    return True, tablero


def comprueba3Enraya(tablero):
    return True        
    

tablero = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
impresion(tablero)

victoria = False
i = 0

while not victoria:
    i+=1
    valido, tablero = nuevoMovimiento(i, tablero)
    
    if valido is True:
        impresion(tablero)
    else:
        print("El rango de valores introducido no es correcto...")
        i -= 1
    
    if i >= 5:
        victoria = comprueba3Enraya(tablero)
        if victoria:
            if i%2 == 0:
                print("\nEnhorabuena!, ha ganado el jugador X\n"\
                        "====================================\n")
            else:
                print("\nEnhorabuena!, ha ganado el jugador O\n"\
                        "====================================\n")    