asignaturas = {'mates': {'Alumno0': {'nombre': 'juan', 'apellido': 'hernandez', 'edad': '17', 'movil': '001122330'},
                         'Alumno1': {'nombre': 'MARIA', 'apellido': 'GUTIERREZ', 'edad': '17', 'movil': '123456789'},
                         'Alumno2': {'nombre': 'Elena', 'apellido': 'jimenezz', 'edad': '18', 'movil': '789456123'}},
               'lengua': {'Alumno0': {'nombre': 'juan', 'apellido': 'hernandez', 'edad': '17', 'movil': '001122330'},
                          'Alumno1': {'nombre': 'MARIA', 'apellido': 'GUTIERREZ', 'edad': '17', 'movil': '123456789'},
                          'Alumno2': {'nombre': 'Elena', 'apellido': 'jimenezz', 'edad': '18', 'movil': '789456123'}}}

for a in asignaturas:
	print(a)
	for b in asignaturas[a]:
	    print("\t  "+b)
     
     
for a in asignaturas:
    print(a)
    for b in asignaturas[a]:
        print("\t", b)
        for n, v in asignaturas[a][b].items():
            print("\t\t",n,":",v)


cierto = ["S", "s"]
if(input("Quiere seguir? S|N: ") in cierto):
    print("Sigo")
else:
    print("Me salgo")