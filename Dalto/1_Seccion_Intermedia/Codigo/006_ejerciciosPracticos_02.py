


dict_alumnos = dict()


def ingresar_alumno():
    contador = 0
    numero_alumnos = int(input("¿Cuántos alumnos hay en salón? "))
    while contador < numero_alumnos:
        alumno = input("Cuál es tu nombre: ")
        edad = int(input("Cuál es tu edad: "))
        dict_alumnos[alumno] = edad
        contador += 1

    
test = {
    "key1" : 5,
    "key2" : 4,
    "key3" : 3
}





def main():
    print(list(test.))



if __name__ == '__main__':
    main()





