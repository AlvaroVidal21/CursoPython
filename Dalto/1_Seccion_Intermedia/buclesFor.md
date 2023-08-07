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
