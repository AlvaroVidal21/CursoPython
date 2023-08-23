## Introducción
Crear una función que te pida un número y devolver los números primos que hay hasta llegar a ese número.

## Resolución

Para ello debemos crear dos funciones:
- Función #1: Este va a evaluar si un número es primo o no, para saber si un número es primo debemos saber si es divisible solo entre 1 y el mismo número. Para ello, se dividirá el número en cuestión a partir de 2 y un número menos del número en cuestión `num - 1`
```Python
def es_primo(num): 
    for n in range(2, num-1): # [1]
        if num%n == 0 : return False
	return True # [2]
```
[1] Evaluamos todas las divisiones a partir de 2 y un número menos del número en cuestión, si es divisible, se concluye que **no es primo**.
[2] Al no ser divisible con ninguno de los números evaluados, concluimos que **es primo**.

- Función #2: Este se encargar de llamar a la `función #1` las veces que sea necesarias y extraer los números primos que contenga.
```Python
def primos_until(num):
    primos = list() # Aquí se almacenará todos los números primos
    for numero in range (2, num+1): # [1]
        valor = es_primo(numero) # Evaluamos número por número si es primo

        if valor == True : primos.append(numero) # [2]

    return primos
```

[1] Usamos ` num+1 ` para que en caso el número proporcionado es primo sea incluido en la lista.
[2] Si es primo entonces agregamos a la lista con `append`.

## Aplicación
```Python
lista_primos = primos_until(21)
print(lista_primos)
```

**Output**
```Python
[2, 3, 5, 7, 11, 13, 17, 19]
```