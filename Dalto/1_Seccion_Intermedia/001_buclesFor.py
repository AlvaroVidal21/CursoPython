
# Data
notas = [20, 20, 13, 14]
alumnos = ['Sherlock', 'Mycroft', 'John', 'Irene']

diccionario = {
    'nombre' : 'Sherlock',
    'edad' : 5,
    'cumpleaños' : '21 de marzo'
}


# Bucle for - zip
def for_zip():   
    for nota, alumno in zip(notas, alumnos):
        print(f'La nota de {alumno} es: {nota}')


# Bucle for - enumerate
def for_enumerate():
    for indice, alumno in enumerate(alumnos):
        print(f'El alumno {alumno} tiene el indice {indice}')


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
    iterar_items()
if __name__ == '__main__':
    go()