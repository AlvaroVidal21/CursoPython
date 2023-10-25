# import package.sicario as sicario

import package.sicario as sicario


def indetificar():
    personaje = input('Cuál es tu nombre: ')
    return personaje



def main():
    personaje = indetificar()
    print(f'El personaje es: {personaje}')
    sicario.identificar_objetivo(personaje)



if __name__ == '__main__':
    main()
