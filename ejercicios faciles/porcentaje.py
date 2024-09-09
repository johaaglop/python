print("Ingrese el porcentaje que se desea calcular: ")
porcentaje = float(input())
print("Ingrese el número base: ")
num = float(input())
resultado = porcentaje*num/100

print("El ", porcentaje, "porciento de ", num, "Es ", round(resultado, 2))
