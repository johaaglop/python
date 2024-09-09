
print("==============M E N U=================")
    print("1) Cocacola light $15.70 ")
    print("2) Subway de jamón con queso $75.50 ")
    print("3) Chocolate Carlos V $16.90 ")
    print("4. Salir")

opcion = int(input("Que desea ordenar: "))
    
    match opcion:
        case 1:
            print("Cuantas Cocacolas desea ordenar: ")
            cant_coca = (input)
        case 2:
            print("Cuantos Subways desea ordenar: ")
            cant_sub = (input)
        case 3: 
            print("Cuantos chocolates desea ordenar: ")
            cant_cho = (input)
        case 4:
            print("Adios, vuelva pronto!")
        case _:
            print("Opcion no valida")
            
      

'''
coca = 15.70
subway = 75.50
choco = 16.90
subtotal = total_cho + total_coca + total_sub
iva = subtotal * .16
total = subtotal+iva

print("=======T I C K E T=======")
print("Cocacola light $", coca, "cantidad ", cant_coca, "total $", total_coca)
print("Subway $", subway, "cantidad ", cant_sub, "total $", total_sub)
print("Chocolate $", choco, "cantidad ", cant_cho, "total $", total_cho)
print("Subtotal $", subtotal)
print("iva $", iva)
print("total $", total)
'''

