from os import system

asignaturas = {'mates': {'Alumno0': {'nombre': 'juan', 'apellido': 'hernandez', 'edad': '17', 'movil': '001122330'},
                         'Alumno1': {'nombre': 'MARIA', 'apellido': 'GUTIERREZ', 'edad': '17', 'movil': '123456789'},
                         'Alumno2': {'nombre': 'Elena', 'apellido': 'jimenezz', 'edad': '18', 'movil': '789456123'}},
               'lengua': {'Alumno0': {'nombre': 'juan', 'apellido': 'hernandez', 'edad': '17', 'movil': '001122330'},
                          'Alumno1': {'nombre': 'MARIA', 'apellido': 'GUTIERREZ', 'edad': '17', 'movil': '123456789'},
                          'Alumno2': {'nombre': 'Elena', 'apellido': 'jimenezz', 'edad': '18', 'movil': '789456123'}}}


def recorreDiccionario():
    for a in asignaturas:
        print(a)
        for b in asignaturas[a]:
            print("\t", b)
            for n, v in asignaturas[a][b].items():
                print("\t\t",n,":",v)

def addDiccionario():
    asignaturasExisten = []
    valido = ["S", "s", "si", "SI", "Si", "Vale", "vale", "VALE", "OK", "ok", "Ok", "Y", "y"]

    for a in asignaturas:
        asignaturas.append(a)

    system("cls")
    print("Vamos a introducir los datos de un nuevo alumno: ")
    print("================================================")

    print("Considerando que las asignaturas que existen son: ", asignaturasExisten)

    asigInput = input("\n¿De qué asignatura es el alumno?: ")

    if asigInput in asignaturas:
        pass

    else:
        if input("\nLa asignatura que has escrito no existe, ¿quiere crearla?: ") in valido:
            pass
        else:
            pass



def menu():
    print("MENÚ DE ELECCIÓN:")
    print("=====================================")
    print()
    print("1. Mostrar diccionario de asignaturas")
    print("2. Añadir persona al  diccionario")
    print("3. Vaciar diccionario")
    print("4. Poner diccionario por defecto")
    print("5. Salir del programa")
    print("=====================================")
    print()
    return input("Elige una opción: ")

def rellenaPorDefecto():
    pass



#print(asignaturas)
recorreDiccionario()