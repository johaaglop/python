#Funcion para verificar si un numero es par o impar
def es_par(numero):
    if numero % 2 == 0:
        print("Es par")
    else:
        print("es impar")
    
num = int(input("Ingrese el número entero que desea verificar si es par o impar: "))
es_par(num)