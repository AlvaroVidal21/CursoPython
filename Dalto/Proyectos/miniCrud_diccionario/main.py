import funciones as fn

# Global
dict_alumnos = {}
bucle_menu = 0

def agregar_alumnos():
    fn.set_alumno(dict_alumnos)

def mostrar_alumnos():
    print("-" *30)
    print(f'Los alumnos son: {list(dict_alumnos.values())}')
    print("-" *30)

def menu():
    global bucle_menu
    print("-" *30)
    print('''
    1. Agregar alumno
    2. Mostrar alumnos
    3. Salir
    ''')
    print("-" *30)


    opcion = input('Ingrese una opción: ')

    if opcion == '1':
        agregar_alumnos()
    elif opcion == '2':
        mostrar_alumnos()
    elif opcion == '3':
        print('Programa finalizado')
        blucle_menu = 1
        exit()
    else:
        print('Opción no válida')
        menu()

def main():
    while bucle_menu == 0:
        menu()


if __name__ == '__main__':
    main()