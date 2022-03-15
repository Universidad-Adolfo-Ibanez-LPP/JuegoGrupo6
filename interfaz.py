def guiones(pais,aciertos):

    lista = []
    for i in list(pais):
        if i in aciertos:
            lista.append(i)
        else:
            lista.append("_")

    return(lista)


def fallado(errores):
    return "Letras erroneas:",errores


