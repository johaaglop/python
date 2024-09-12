#Suma número indefinido de parametros*
def suma_var(*numeros):
    total = 0
    for num in numeros:
        total += num
    return total

print(suma_var(3,2,4,5,67,9))
