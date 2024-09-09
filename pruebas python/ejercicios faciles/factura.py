print("Precio de la cocacola light ")
coca = float(input())

print("Precio del subway ")
subway = float(input())

print("Precio del chocolate ")
choco = float(input())

subtotal = coca + subway + choco
iva = subtotal * .16
total = subtotal+iva

print("=======T I C K E T=======")
print("Cocacola light $", coca,)
print("Subway $", subway)
print("Chocolate $", choco)
print("Subtotal $", subtotal)
print("iva $", iva)
print("total $", total)


