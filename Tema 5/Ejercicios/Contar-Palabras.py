from os import system

frase = "Yo creo que la gente, cuando es inteligente y completamente normal,"\
        " no debe pretender el ser rara y extraña, porque llega al absurdo inventado."\
        " Nosotros como personas debemos aprender a no desperdiciar el tiempo que pasamos unidos."


system("cls")

contP, contL, contV, contComa, contP, contMayus, contVerb, contPlur = 2, 0, 0, 0, 0, 0, 0, 0
for c in frase:
    if c == " ": contP += 1
    elif c == ",": contComa += 1
    elif c == ",": contP += 1
    elif c in {"a", "e", "i", "o", "u"}: contV += 1
    
    if c.isupper() and (frase[contL-1].isspace() or contL == 0): contMayus += 1

    contL += 1;

frase.replace(".", "")
frase.replace(",", "")
palabras = frase.split(" ")

for c in palabras:
    if c.endswith("ar") or c.endswith("er") or c.endswith("ir"): contVerb += 1;
    if c.endswith("os"): contPlur += 1;

print("La frase tiene:", contP, "palabras.")
print("La frase tiene:", contL, "caracteres totales.")
print("La frase tiene:", contV, "vocales.")
print("La frase tiene:", contComa, "comas.")
print("La frase tiene:", contP, "puntos.")
print("La frase tiene:", contMayus, "mayúsculas.")
print("La frase tiene:", contVerb, "verbos.")
print("La frase tiene:", contPlur, "palabras en plural.")