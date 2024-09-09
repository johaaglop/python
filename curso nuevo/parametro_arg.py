#arg * parametro para aceptar varios valores dentro de una tupla
def suma(*num):
    sumar = 0
    for i in num:
        sumar += i
    return sumar
