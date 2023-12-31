from os import system

def recorreDiccionario(asignaturas):
    for a in asignaturas:
        print(a)
        for b in asignaturas[a]:
            print("\t", b)
            for n, v in asignaturas[a][b].items():
                print("\t\t",n,":",v)

def recargaDiccionario():
    listaNombre = ["Juan", "Maria", "Elena"]
    listaApellido = ["Hernandez", "Gutierrez", "Jimenez"]
    listaEdad = [17, 17, 18]
    listaMovil = ["001122330", "123456789", "789456123"]
    listaAsignaturas = ["mates", "lengua"]

    nuevaAsignatura = {}

    for i in range(2):
        nuevaAsignatura[listaAsignaturas[i]] = {}
        for j in range(3):
            nuevoAlumno = {}
            nuevoAlumno['nombre'] = listaNombre[j]
            nuevoAlumno['apellido'] = listaApellido[j]
            nuevoAlumno['edad'] = str(listaEdad[j])
            nuevoAlumno['movil'] = listaMovil[j]

            nuevaAsignatura[listaAsignaturas[i]]["Alumno"+str(j)] = nuevoAlumno

    return nuevaAsignatura


asignaturas = recargaDiccionario()
recorreDiccionario(asignaturas)