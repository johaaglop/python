mi_tupla = (6, 'gato', 9, 'jirafa', 9.7)

print(mi_tupla[1]) #muestra el valor contenido en la posicion deseada
print(mi_tupla.count(9)) #no dice cuantos elementos hay del valor pedido
print(mi_tupla.index('jirafa')) #nos devuelve la posicion actual del elemento

#la unica diferencia con una lista es que no se puede modifica a menos que cambiemos su composicion de tupla a lista 

mi_tupla = list(mi_tupla) #aqui ya es lista y ya se pueden agregar elemento
print(type(mi_tupla))

#puedes regresarla a ser una tupla de nuevo
mi_tupla = tuple(mi_tupla)
print(type(mi_tupla))