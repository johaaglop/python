#Funcion para calcular área de círculo

import math

def a_circulo(radio):
    return math.pi * radio ** 2

radio = float(input("Escriba el rádio del círculo: "))
resultado = a_circulo(radio)

print(f"El área del círculo con rádio de {radio}, es:", round (resultado, 2))