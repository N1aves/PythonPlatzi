#Las tuplas son valores estaticos, 
# a diferencia de las listas que son dinamicas y ocupan mas espacio en memoria.

#Para crear una tupla se usa parentecis seprado por comas cada valor
>>>tupla= (1,2,3,4,5)
>>> tupla
(1, 2, 3, 4, 5)
>>>
#Los valores de la tupla no se pueden modificar o cambiar, 
#Las tuplas son INMUTABLES (No pueden cambiar, igual como un String)
#Las tuplas funcionan mas rapido en ciclos
>>> for numero in tupla:
...     print(numero)
...
1
2
3
4
5
>>>