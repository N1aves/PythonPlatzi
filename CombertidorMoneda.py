menu = """
Bienvenido al conversor de monedas 💰

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos Mexicanos

Elige una opción:
"""
opcion = int(input(menu))

if opcion == 1:
    pesos = input ("Cuantos pesos colombianos tienes?:   ")
    pesos = float (pesos)
    valor_dolar=3875
    dolares= pesos/ valor_dolar
    dolares= round (dolares, 2)
    dolares= str(dolares)
    #Tambien podemos concatenar en la misma definicion de variable!!
    #dolares= str(dolares)+ "Dolares"    
    print("Tienes: "+ dolares + " dolares")
elif opcion == 2:
    pesos = input ("Cuantos pesos argentinos tienes?:   ")
    pesos = float (pesos)
    valor_dolar=65
    dolares= pesos/ valor_dolar
    dolares= round (dolares, 2)
    dolares= str(dolares)
    #Tambien podemos concatenar en la misma definicion de variable!!
    #dolares= str(dolares)+ "Dolares"    
    print("Tienes: "+ dolares + " dolares")
elif opcion ==3:
    pesos = input ("Cuantos pesos mexicanos tienes?:   ")
    pesos = float (pesos)
    valor_dolar=21.8
    dolares= pesos/ valor_dolar
    dolares= round (dolares, 2)
    dolares= str(dolares)
    #Tambien podemos concatenar en la misma definicion de variable!!
    #dolares= str(dolares)+ "Dolares"    
    print("Tienes: "+ dolares + " dolares")
else:
    print("Escribe una opcion valida (1, 2 o 3)")


