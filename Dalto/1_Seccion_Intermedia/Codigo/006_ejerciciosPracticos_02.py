# 1 profesor -> el que más edad tiene
# 1 asistente -> el que menos edad tiene

# Ingresar los nombres y edades de los alumnos (dentro de ellos está el profesor y el asistente) y 
# ordenar de mayor a menor



alumnos = list()


def obtener_alumnos(cantidad_de_alumnos):
    for alumno in range(cantidad_de_alumnos):
        nombre_alumno = input('Cuál es el nombre del alumno: ')
        edad_alumno = int(input('Cuál es la edad del alumno: '))
        alumno_input = (nombre_alumno, edad_alumno)
        alumnos.append(alumno_input)

    alumnos.sort(key= lambda x:x[1]) # x[1] x es la tupla ("alumno", edad), entonces x[1] es la edad, usando lambda pedimos que nos ordenen por la edad. El sort va a ordenar de MENOR -> MAYOR

    # El asistente el el el primero en la lista ordenada
    asistente = alumnos[0][0] # Esto para obtener solo el nombre del asistente

    # El profesor el el último de la lista, dado que es el que tiene mayor edad
    profesor = alumnos[-1][0] 

    return asistente, profesor
 

def main():
    asistente, profesor = obtener_alumnos(3)
    print(f'las personas en la clase son {alumnos}')
    print(f'El asistente es: {asistente}')
    print(f'El profesor es: {profesor}')
  



if __name__ == '__main__':
    main()