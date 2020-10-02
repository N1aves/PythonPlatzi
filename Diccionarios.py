#Para crear diccionarios se usan llaves
#Para buscar los valores del diccionario los buscaras atraves de
    #INDICES. Los cuales podras nombrar, a diferencia de las listas que van del 0 al inf

   
def ejemplo1():
    mi_diccionario = {
        'llave1':1,
        'llave2':2,
        'llave3':3,
        'llave4':4,
    }
    print(mi_diccionario)
    
    print(mi_diccionario['llave1'])
    print(mi_diccionario['llave2'])
    print(mi_diccionario['llave3'])


def ejemplo2():
    poblacion_paises ={
        'Argentina': 44938712,
        'Brasil': 21014123,
        'colombia': 5033224,
    }
    #.key() es un Metodo de diccionarios que te devuelve las llaves
    for pais in poblacion_paises.keys():
        print(pais)
    #Metodo .values() se usa para devolverte los valores de las llaves
    for pais in poblacion_paises.values():
        print(pais)
    #El metodo .items() devuelve los indices y valores de todo el diccionario
    for pais,poblacion in poblacion_paises.items():
        print(pais+ " tiene "+ str(poblacion)+" habitantes")


def run():
    ejemplo1()
    ejemplo2()
   

if __name__== '__main__':
    run()