from os import system

def almacenaDic(fichero_log):
    def decFuncRecorrido(funcion):
        def decorador(diccionario):
            with open(fichero_log, 'a') as opened_file:
                output = funcion(diccionario)
                opened_file.write(f"{output}\n")
                return "Fichero escrito correctamente"
        return decorador
    return decFuncRecorrido


@almacenaDic('ficherosalida.log')
def recorreDiccionario(asignaturas):
    resultado = ""

    for a in asignaturas:
        resultado += a + "\n"
        for b in asignaturas[a]:
            resultado += "\t" + b + "\n"
            for n, v in asignaturas[a][b].items():
                resultado += "\t\t" + n + ": " + str(v) + "\n"

    return resultado

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