def ejemplo(a, b, c):
    return a+b+c, a-b-c, a*b*c

radio = 5
area = 3.14 * 5 * 2
print(area)

area = 3.14 \
    *5*2
print(area)

nombre = "HOLA"
print(nombre[0]+nombre[1])
print(nombre[0], nombre[1])
print(nombre[-1], nombre[-2], nombre[-3], nombre[-4])

for i in nombre:
    print(i)

print()
for i in range(1, 5):
    print(nombre[-i])

print()
print(nombre[0:2])
print(nombre[:3])
print(nombre[3:])

"""Empiezas en 0, llegas al 3, y lees cada 2"""
print(nombre[0:3:2])

print("radio",type(radio))
print("nombre",type(nombre))

print()
radio = "5"
print("radio redeclarado",type(radio))
print("radio casteado",type(float(radio)))

nComplejo = 1+2j
print(nComplejo.real)
print(nComplejo.imag)

reSuma, reResta, reMulti = ejemplo(1, 2, 3)

print(reSuma, reResta, reMulti)
print(ejemplo(1, 2, 3))

print()
def diferentesParam(arg1, arg2="tardes", arg3="Alberto"):
    print(arg1, arg2, arg3)

diferentesParam("Buenas")
diferentesParam("Buenas", "Noches")
diferentesParam("Buenas", "noches", "David")

n = 5
print(n)

def cambiaGlobal():
    """Es como si fuese "por referencia", aunque suene algo diferente. Todo lo del main por defecto es global"""
    global n
    n = 7

cambiaGlobal()
print(n)