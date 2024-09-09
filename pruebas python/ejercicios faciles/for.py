'''
sumar los numeros del 1 al 10 con for

suma = 0
for i in range (1, 11):
    suma = suma + i
    
print (f"La suma es {suma}")


numeros pares del 2 al 10

for i in range(2, 11, 2):
    print(i)

Listar 10 numeros y calcular su cuadrado a cada uno

for i in range(1, 11):
    cuadrado = i ** 2
    print(f"El cuadrado de {i} es {cuadrado}")

Decremento del 5 al 1 con for

for i in range(5, 0, -1):
    print(i)

Multiplicar los elementos de una lista por 2 con for


lista1 = [3, 6, 9, 12, 18]

for i in range(len(lista1)):
    print(lista1[i] * 2)

Pedir un numero y mostar tabla de multiplicar de ese numero


numero = int(input("Escribe el número de la tabala de multiplicar deseada: "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} X {i} = {resultado}")

Suma de numeros pares del 1 al 10 


suma_pares = 0
for i in range(1, 11):
    if i  % 2 == 0:
        suma_pares = suma_pares + i

print("La suma de los números pares del 1 al 10 es: ", suma_pares)

'''

numero = int(input("Escribe el número de la tabla de multiplicar deseada: "))

for valor in range(1, 11):
    resultado = numero * valor
    print(f"{numero} X {valor} = {resultado}")