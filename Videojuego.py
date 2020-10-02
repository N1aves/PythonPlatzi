import random
#Primero vamos a importar un Modulo llamado random
def metodo1():
    
    numero_random = random.randint(1,100)
    numero_elegido = int(input('Elige un nuemero de 1 al 100:   '))
    i= 0
    while i < 2:
        if numero_elegido==numero_random:
            i= 2
            print('¡¡¡Felicidades Ganaste!!!') 
        elif numero_random < numero_elegido:
            i=0
            numero_elegido = int(input('Escoge un numero mas pequeño: '  ))
        elif numero_random > numero_elegido:
            i=0
            numero_elegido = int(input('¡Escoge un numero mas Grande:  '))


def metodo2():
    numero_random = random.randint(1,100)
    numero_elegido = int(input('Elige un nuemero de 1 al 100:   '))
    while numero_elegido != numero_random:
        if numero_random < numero_elegido:
            numero_elegido= int(input('¡Escoge un numero mas pequeño:  '))
        else:
            numero_elegido= int(input('¡Escoge un numero mas Grande:  '))
    print('¡Ganaste!')


def run():
    metodo2()


if __name__ == '__main__':
    run()

