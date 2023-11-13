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


tablero = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

impresion(tablero)

