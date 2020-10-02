def bucle_While():
    #Opcion 
    LIMITE = 1000
    contador = 0
    potencia_2= 2 ** contador

    while potencia_2 < LIMITE:

        print('2 elevado a ' + str(contador) + ' es igual a: ' + str(potencia_2))
        contador = contador + 1 
        potencia_2 = 2 ** contador

    contador2 = 0
    potencia2_2= 2 ** contador2

    while contador2 < 100:
        print('2 elevado a ' + str(contador2) + ' es igual a: ' + str(potencia2_2))
        contador2 += 1 
        potencia2_2 = 2 ** contador2





def run():
    bucle_While()
    
    


if __name__ == '__main__':
    run()