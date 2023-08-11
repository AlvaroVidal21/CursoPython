
# Data
notas = [20, 20, 13, 14]
alumnos = ['Sherlock', 'Mycroft', 'John', 'Irene']

diccionario = {
    'nombre' : 'Sherlock',
    'edad' : 5,
    'cumpleaños' : '21 de marzo'
}


# Bucle for - zip
def for_zip(lista1, lista2):   
    for l1, l2 in zip(lista1, lista2):
        print(f'La nota de {l1} es: {l2}')


# Bucle for - enumerate
def for_enumerate(lista):
    for indice, l1 in enumerate(lista):
        print(f'El alumno {l1} tiene el indice {indice}')


# Iterar un diccionario
def iterar_keys():
    for llave in diccionario:
        print(llave)

def iterar_values():
    for valor in diccionario.values():
        print(valor)

def iterar_items():
    for llave, valor in diccionario.items():
        print(f'La llave {llave} tiene el valor {valor}')

def go():
    for_enumerate(alumnos)
if __name__ == '__main__':
    go()