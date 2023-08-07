
# Data
notas = [20, 20, 13, 14]
alumnos = ['Sherlock', 'Mycroft', 'John', 'Irene']


# Bucle for - zip
def for_zip():   
    for nota, alumno in zip(notas, alumnos):
        print(f'La nota de {alumno} es: {nota}')


# Bucle for - enumerate
def for_enumerate():
    for indice, alumno in enumerate(alumnos):
        print(f'El alumno {alumno} tiene el indice {indice}')



def go():
    for_enumerate()
if __name__ == '__main__':
    go()