import os

def run():
    #Open se usa para acceder a la ruta,
    #  w es para escribir y r solo es para leer

    file = open("/Users/gera_/OneDrive/Documentos/Generador/Practica1.txt", "w")
    #Con write podemos escibir en el archivo y os.linesepp es para dar salto de renglon
    
    file.write("Primera línea" + os.linesep)
    file.write("Segunda línea")
    file.close()


if __name__=='__main__':
    run()



