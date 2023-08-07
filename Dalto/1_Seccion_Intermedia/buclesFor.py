

def go():
    # Bucle for - zip
    notas = [20, 20, 13, 14]
    alumnos = ['Sherlock', 'Mycroft', 'John', 'Irene']

    for nota, alumno in zip(notas, alumnos):
        print(f'La nota de {alumno} es: {nota}')




if __name__ == '__main__':
    go()