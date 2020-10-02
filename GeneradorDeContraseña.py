import random


def generar_contrasena():
    mayuscula = [
        'A','S','D','F','G','H','J','K','L','Ñ',
        'Q','W','E','R','T','Y','U','I','O','P',
        'Z','X','C','V','B','N','M'
    ]
    minusculas = [
        'a','s','d','f','g','h','j','k','l','ñ',
        'q','w','e','r','t','y','u','i','o','p',
        'z','x','c','v','b','n','m'

    ]
    simbolos = ['¿','!','#','$','%','&','/','¡','?',' ']
    numeros = ['1','2','3','4','5','6','7','8','9','0']

    caracteres = mayuscula + minusculas + simbolos + numeros
    contrasena= []
    for i in range(16):
        #choice es un metodo propio de random donde selecciona aleatoriamente un calor de lista
        caracter_random= random.choice(caracteres)
        contrasena.append(caracter_random)
    contrasena= ''.join(contrasena)
    return contrasena



def run():
    contrasena = generar_contrasena()
    print('tu nueva contraseña es:  '+ contrasena)


if __name__=='__main__':
    run()