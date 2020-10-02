#Un arreglo es una porción de memoria continua, 
# una estructura de datos estática que no puede modificar
#  su tamaño y cuyos miembros deben ser todos del mismo tipo.

#En Python hay un par de librerías que te dejarán implementar arrays como lo son numpy, array, etc.

#Sin embargo en Python existen las listas, que son una estructura de datos lineal más compleja, 
# si bien su comportamiento será similar al de un array, nunca serán iguales, ya que estas son dinámicas,
#  es decir, su tamaño puede variar tanto como sea necesario y además sus elementos no están sujetos a ser 
# de un mismo tipo, puedes en una misma lista añadir enteros, cadenas, flotantes, diccionarios, tuplas, etc.

#Esta lista es una implementación abstracta similar a una lista ligada,
#  pero de una manera mucho más sencilla de usar, es decir sin tener que definirla uno mismo.

>>> numero = 1
#Listas, se crean con corchetes y separado con comas. 

>>> numeros= [1,2,3,4,5,6,7,8,9]
>>> numeros
[1, 2, 3, 4, 5, 6, 7, 8, 9]
#Se pueden agregar, strings, int, floot etc.
>>> objetos = [1,'Hola',2,'Gera']
>>> objetos
[1, 'Hola', 2, 'Gera']
>>> objetos
[1, 'Hola', 2, 'Gera']
>>> objetos[3
... ]
'Gera'
>>> objetos[3]
'Gera'
>>> objetos[2]
2
>>> objetos[1]
'Hola'
#Metodo .append() Nos funciona para agregar mas valores a una lista.
>>> objetos.append(False)
>>> objetos.append(True)
>>> objetos
[1, 'Hola', 2, 'Gera', False, True]
# Metodo .pop Nos funciona para eliminar contenido en (x) posicion
>>> objetos.pop
<built-in method pop of list object at 0x03266DC8>
>>> objetos.pop(1)
'Hola'
>>> objetos
[1, 2, 'Gera', False, True]
>>>
>>> for elemento in objetos:
...     print(elemento)
...
1
2
Gera
False
True
#Se pueden usar los Slice pen una lista:
>>> objetos[::-1]
[True, False, 'Gera', 2, 1]
>>>
#Tambien podemos concatenar listas:
>>> numeros
[1, 2, 3, 4, 5]
>>> numeros2=[6,7,8,9,0]
>>> numeros2
[6, 7, 8, 9, 0]
>>> lista_final = numeros+numeros2
>>> lista_final
[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
#Tambien podemos multiplicar la misma lista
>>> numeros *5
[1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
>>>
>>>
#Coclusion: Las listas son muy parecidas a los Arreglos, sin embargo, no se comportan de la misma manera como en otros lenguajes, 
#pero una Lista es el equivalente a un arreglo.