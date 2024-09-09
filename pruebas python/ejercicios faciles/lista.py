mi_lista = [10, 8, 7, 14, 'hola', False]
mi_lista.append('jacinto') #inserta un nuevo elemento al final de la lista
mi_lista.insert(0,'coma') #inserta un elemento en la posicion que le indiques
mi_lista.remove('jacinto') #elimina al elemento que le digas
eliminado = mi_lista.pop(0) #Elimina y muestra a quien elimino
#mi_lista.clear() elimina la lista
mi_lista.reverse() #acomoda la lista en reversa

for elemento in mi_lista: #sirve para acomodar la lista y usar sus elementos
    print(elemento)

