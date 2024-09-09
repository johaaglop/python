# break
'''
while True:
    nombre = input("Ingresa tu nombre: ")
    if nombre != "":
        break
print("mucho gusto", nombre)

#continue
telefono = input("Ingresa tu número telefonico: ")

for i in telefono:
    if i == "-":
        continue
    print(i, end="")
'''
#pass imprime los numero del 1 al 20 excepto el 13 de mala suerte
for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i)




