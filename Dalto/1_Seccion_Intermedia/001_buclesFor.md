# Bucles for


## Sintaxis
```Python
for elemento in secuencia:  
    # Código a ejecutar dentro del bucle**
```


## Zip()
`zip()` es otra función incorporada que te permite combinar elementos de varias secuencias en un solo iterador durante el bucle for. Esto es útil ==**cuando necesitas recorrer elementos de múltiples listas simultáneamente**==.


```Python
def go():
    # Bucle for - zip
    notas = [20, 20, 13, 14]
    alumnos = ['Sherlock', 'Mycroft', 'John', 'Irene']

    for nota, alumno in zip(notas, alumnos):
        print(f'La nota de {alumno} es: {nota}')


if __name__ == '__main__':
    go()
```


**Ouput**


La nota de Sherlock es: 20
La nota de Mycroft es: 20
La nota de John es: 13
La nota de Irene es: 14


## Enumerate()
`enumerate()` es una función incorporada en Python que permite obtener tanto el valor como el índice de cada elemento en una secuencia durante el bucle for. Esto es útil cuando necesitas acceder al índice de cada elemento mientras iteras.
Nos devuelve ==**tuplas**==.


```Python
# Data
notas = [20, 20, 13, 14]
alumnos = ['Sherlock', 'Mycroft', 'John', 'Irene']

# Bucle for - enumerate
def for_enumerate():
    for indice, alumno in enumerate(alumnos):
        print(f'El alumno {alumno} tiene el indice {indice}')



def go():
    for_enumerate()
if __name__ == '__main__':
    go()
```


**Output**


El alumno Sherlock tiene el indice 0
El alumno Mycroft tiene el indice 1
El alumno John tiene el indice 2
El alumno Irene tiene el indice 3