# Definimos la clase Matema
class Matema:
    # Constructor de la clase, recibe los valores de a y b
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    # Método que devuelve la suma de a y b
    def suma(self):
        return self.a + self.b
    
    # Método que devuelve la resta de a y b
    def resta(self):
        return self.a - self.b
    
    # Método que devuelve la multiplicación de a y b
    def multiplicacion(self):
        return self.a * self.b
    
    # Método que devuelve la división de a y b
    def division(self):
        if self.b == 0:
            return "Error: División entre cero..."
        else:
            return self.a / self.b

# Programa principal
# Pedimos los valores de a y b
a = int(input("Valor de a: "))
b = int(input("Valor de b: "))

# Creamos un objeto de la clase Matema con los valores de a y b
m = Matema(a, b)

# Llamamos a los métodos del objeto y guardamos los resultados en variables
s = m.suma()
r = m.resta()
p = m.multiplicacion()
d = m.division()

# Imprimimos los resultados
print(f"La suma es: {s}")
print(f"La resta es: {r}")
print(f"La multiplicación es: {p}")
print(f"La división es: {d}")
