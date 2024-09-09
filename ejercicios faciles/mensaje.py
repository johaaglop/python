fila = int(input("Cuantas filas quiere: "))
colum_na = int(input("Cuantas columnas: "))
sim_bolo = input("Ingrese un símbolo: ")
#bucles anidados
for i in range(fila):
    for j in range(colum_na):
        print(sim_bolo, end="")
    print()

