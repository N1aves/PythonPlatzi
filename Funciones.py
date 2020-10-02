def imprimir_mensaje():
    print ("Mensaje especial:")
    print ("Estoy aprendiendo a usar funciones")

opcion = int(input("Elige una opción (1,2,3)"))
#if opcion == 1:
#    print ("Hola")
#    print ("Eligiste la opcion 1")
#    print ("adios")
#elif opcion == 2:
#    
#    print ("Hola")
#    print ("Eligiste la opcion 2")
#    print ("adios")
#elif opcion==3:
#    print ("Hola")
#    print ("Eligiste la opcion 3")
#    print ("adios")

#Asi se resolveria con una funcion:
def conversacion(mensaje):
    print ("Hola")
    print (mensaje)
    print ("adios")


if opcion == 1:
    conversacion("Elegiste la opcion 1")
elif opcion == 2:
    
    conversacion("Elegiste la opcion 2")
elif opcion==3:
    
    conversacion("Elegiste la opcion 3")
#Esta es otra forma de resolverlo
def conversacion2(numero):
    numero = str(numero)
    print ("Hola")
    print ("Elegiste la opcion " + numero)
    print ("adios")

if opcion == 1:
    conversacion2(1)
elif opcion == 2:
    
    conversacion2(2)
elif opcion==3:
    
    conversacion2(3)


def suma(a, b):
    print ("Se suman los dos numeros")
    resultado= a + b
    return resultado

sumatoria =  suma(1, 4)
print (sumatoria)