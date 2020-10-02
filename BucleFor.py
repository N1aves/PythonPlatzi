def bucle_For():

    for contador in range(1, 10):
        potencia_3 = 3**contador
        print('3 elevado a ' + str(contador) + ' es igual a: ' + str(potencia_3))

    print ('La Tabla del 11 es:')
    for i in range(11):
        print('11 * ' +str(i)+ ' = '+ str(11*i) )


def run():
    bucle_For()


if __name__ ==  '__main__':
    run()