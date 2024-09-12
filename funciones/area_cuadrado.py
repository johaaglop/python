#área de un cuadrado
def area_cu (base, altura):
    """
    Calcula el área de un cuadrado
    :arg
    :param base(float): La base del cuadrado
    :param altura(float): La altura del cuadrado
    :return: float: el área del cuadrado
    """
    return base * altura / 2

base = (float(input("Ingrese la base del cuadrado: ")))
altura = (float(input("Ingrese la altura del cuadrado: ")))
print(f"La base {base}, por la altura {altura}, del cuadrado entre 2, es igual al área del cuadrado: {area_cu(base, altura)}")