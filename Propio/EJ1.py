# Definimos las funciones que realizan las operaciones aritméticas
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División entre cero..."
    else:
        return a / b

# Definimos la función que muestra el menú y devuelve la opción elegida
def menu():
    print("----------- Calculadora -----------")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    print("-----------------------------------")
    opcion = int(input("Seleccione una opción: "))
    return opcion

# Definimos la función que simula un switch con un diccionario
def switch(opcion, a, b):
    sw = {
        1: suma(a, b),
        2: resta(a, b),
        3: multiplicacion(a, b),
        4: division(a, b),
        5: "Adiós"
    }
    return sw.get(opcion, "Opción inválida")

# Programa principal
while True:
    # Pedimos los valores de a y b
    a = int(input("Valor de a: "))
    b = int(input("Valor de b: "))
    
    # Mostramos el menú y obtenemos la opción
    opcion = menu()
    
    # Ejecutamos el switch y mostramos el resultado
    resultado = switch(opcion, a, b)
    print(resultado)
    
    # Si la opción es 5, salimos del bucle
    if opcion == 5:
        break
