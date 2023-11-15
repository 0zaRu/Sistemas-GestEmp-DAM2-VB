determinantes = {
    "articulos":{
        "determinados":["el", "las", "los", "las"],
        "indeterminados":["un", "una", "unos", "unas"]
    },
    "posesivos":["mi", "tu", "su", "nuestro/a", "vuestro/a"],
    "demostrativos":["este", "ese", "aquel"],
    "indefinidos":["algún", "bastante", "cada", "cierto", "cualquier", "demás",\
                   "demasiado", "más", "mismo", "mucho", "ningún", "otro",\
                    "poco", "sendos", "todo", "varios"],
    "numerales":{
        "cardinales":["un", "dos", "tres", "cuatro"],
        "ordinales":["primero", "segundo", "tercero", "cuarto"]
    },
    "interrogativos y exclamativos":["qué", "cuánto"],
    "relativo-posesivo":["cuyo"]
}

for a in determinantes:
    print(a)
    if type(determinantes[a]) == dict:
        for b in determinantes[a]:
            print("\t", b)
            for valor in determinantes[a][b]:
                print("\t\t",valor)
    else:
        for valor in determinantes[a]:
            print("\t\t",valor)