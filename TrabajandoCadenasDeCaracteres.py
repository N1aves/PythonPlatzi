>>> nombre = input("¿Cual es tu nombre? ")
¿Cual es tu nombre? gerardo
>>> nombre
'gerardo'
# El METODO .upper() sirve para hacer todos los caracteres en mayuscula
>>> nombre.upper()
'GERARDO'
# El METODO .capitalize() sirve para Hacer  mayuscula el primer caracter
>>> nombre.capitalize()
'Gerardo'
>>> nombre=  nombre.capitalize()
>>> nombre
'Gerardo'
# El METODO .strip() sirve para borrar espacios en inicio y fin
>>> nombre.strip()
'Gerardo'
# El METODO .lower() sirve para Hacer  minuscula todos los  caracter
>>> nombre.lower()
'gerardo'
# El METODO .replace() sirve para remplazar caracteres, 
# el primer parametro busca todos esos caracteres y despues lo remplaza por el segundo parametro

>>> nombre = nombre.replace ('o','a')
>>> nombre
'Gerarda'
>>> nombre = nombre.replace ('a','o')
>>> nombre
'Gerordo'
#Los indices son para buscar el caracter especifico.
>>> nombre [0]
'G'
>>> nombre [1]
'e'
>>> nombre [2]
'r'
>>> nombre [3]
'o'
>>> letra = nombre[0]
>>> letra
'G'
>>> 
>>> nombre = Gerardo
>>> nombre = "Gerardo"
>>> nombre
'Gerardo'
>>> nombre[3].replace('a','o')
'o'
>>> nombre
'Gerardo'
#La funcion len, cuenta los caracteres de una cadena,
#el parametro puede ser una variable tipo cadena o una cadena escrita
# Las funciones como len, print etc; Son funciones ya integradas dentro de un lenguaje

>>> len(nombre)
7
>>> len(letra)
1
>>> len("Bienvenidos al curso de programacion")
36
>>>                                                                  
                                                                             