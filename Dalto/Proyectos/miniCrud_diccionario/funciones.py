

# Función para crear un nuevo alumno

def new_alumno():
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    especialidad = input("Especialidad: ")


    alumno_nuevo = {
        "nombre": nombre,
        "edad": edad,
        "especialidad": especialidad
    }

    return alumno_nuevo


# Función para ingresar un nuevo alumno al diccionario

def set_alumno(diccionario_alumnos):
    alumno = new_alumno()
    id_alumno = 'Alumno-' + str(len(diccionario_alumnos) + 1)
    diccionario_alumnos[id_alumno] = alumno
    



