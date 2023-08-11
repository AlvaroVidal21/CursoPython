# List Comprehension

## Definición
Permite crear listas de forma concisa y eficiente. Esto se logra al aplicar una expresión a cada elemento de un iterable

- **Expresión**: Define la operación o cálculo que se realizará en cada elemento del iterable.
- **Elemento**: Es una variable temporal que toma el valor de cada elemento en el iterable durante la iteración.
- **Iterable**: La secuencia de elementos a través de los cuales el bucle iterará.
- **Nueva_lista**: La lista resultante que se crea al aplicar la expresión a cada elemento del iterable.

## Sintaxis
```Python
nueva_lista = [expresión for elemento in iterable]
```
## Aplicaciones

### Crear una lista de cuadrados
```Python
numeros = [1, 2, 3, 4, 5]
cuadrados = [x ** 2 for x in numeros]
# output: [1,4,9,16,25]
```
### Filtrado de pares
```Python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [x for x in numeros if x % 2 == 0]
# output: [2,4,6,8,10]
```



## Ejercicio

Filtra de un diccionario de países a una lista que contenga los nombres de los países cuyas longitudes sean iguales o superiores a 10 caracteres.

```Python
paises_longitud = {
    "Estados Unidos": 13,
    "Alemania": 8,
    "Afganistán": 10,
    "Argentina": 9,
    "Australia": 9,
    "Bélgica": 7,
    "Canadá": 6,
    "Dinamarca": 8,
    "Egipto": 6,
    "España": 6,
    "Mongolia": 8,
    "Portugal": 8,
    "Sudáfrica": 10,
    "Tailandia": 9,
    "Uzbekistán": 10
}

def pais_len_10(list_paises):
    len_10 = [pais for pais in list_paises if len(pais)>=10]
    return len_10



def main():
    paises_len_10 = pais_len_10(paises_longitud)
    print(paises_len_10)


if __name__ == '__main__':
    main()
```

**Output**

```Python
['Estados Unidos', 'Afganistán', 'Uzbekistán']
```