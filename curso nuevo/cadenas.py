#Operador de indice
nombre = 'johana López!'
if nombre[0].islower(): #verifica si es mayuscula
    nombre = nombre.capitalize() #capitalize sirve para transformar a mayuscula

#upper pasa todo a mayusculas
primer_nombre = nombre[0:6].upper() #del 0 al 6 es el numero de caracteres del nombre
print(primer_nombre)

apellido = nombre[7:12].lower() #lower todo a minusculas
print(apellido)
ultimo_caracter = nombre [-1]
print(ultimo_caracter)