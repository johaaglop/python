def cel_a_fahre(grados_cel):
    return (grados_cel * 9/5) + 32
conver = float(input("Ingrese la temperatura en Celsius: "))
resultado = cel_a_fahre(conver)
print(resultado, "Grados Fahrenheit")