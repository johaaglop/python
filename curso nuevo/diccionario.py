#Estados y su capital
capital = {'Colima': 'Colima',
           'Michoacan': 'Morelia',
           'Coahuila': 'Saltillo',
           'Hidalgo': 'Pachuca',
           'Jalisco': 'Guadalajara',
           'Nayarit': 'Tepic',
           'Cursos': ['Python','C++','JS'], #tambien puedes agregar listas a los dicc
           'Edad': 33 #tambien valores numericos
}
capital.update({'Nuevo León': 'Monterrey'}) #agrega elementos al diccionario
capital.pop('Colima') #Elimina elementos del diccionario, con clear puedes borrar
#print(capital.get('Argentina')) .get sirva para verificar si existe el valor en la lista
#print(capital.keys()) #verificar las llaves
#print(capital.values()) #verificar los valores que contienen las llaves
#print(capital.items()) #muestra el diccionario completo

for key,value in capital.items(): #imprimir llaves y valor con for
    print(key,',',value)
