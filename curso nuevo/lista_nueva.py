comida = ['Pizza', 'Hamburguesa', 'Tacos', 'Nachos']
comida[1] ='Sushi' #remplaza elemento segun posicion

comida.append('Gelatina')
comida.remove('Tacos')
comida.pop()
comida.insert(0,"Gelatina")
comida.sort()
#comida.clear() borra la lista
for x in comida:
    print(x)

