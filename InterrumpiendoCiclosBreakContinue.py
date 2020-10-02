def ciclo_for():
    for contador in range (10):
        if contador % 2 != 0:
            continue
        print(contador)

    for i in range (1000):
        print (i)
        if i == 98:
            break
    texto = input('Escribe un texto: ')
    for letra in texto:
        if letra == 'd':
            break
        print(letra)


def ciclo_while():
    i = 0
    cont= 0
    while i < 100:
        i+= 1
        if i==10:
            break
        print(i)
    while cont < 100:
        cont+= 1
        if cont % 2 != 0:
            continue
        print(cont)
    while i < 101:
        i+=1
        if i % 2 != 0:
            continue
        print(i)



def run():
    ciclo_while()


if __name__ == '__main__':
    run()
