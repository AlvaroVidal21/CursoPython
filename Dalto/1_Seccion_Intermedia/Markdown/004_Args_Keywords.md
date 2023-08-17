# *Args en una función y los Keywords arguments

## Args
Permite a una función aceptar un número variable de argumentos posicionales. Los argumentos pasados se recopilan en una tupla dentro de la función, lo que facilita su manipulación.

### Aplicación
```Python
def calculate_average(*args):
    num_values = len(args)
    if num_values == 0:
        return None

    total_sum = sum(args)
    average = total_sum / num_values
    
    return average

  
def main():
    average_products = calculate_average(121, 250, 96, 15, 5)
    print(average_products)


if __name__ == '__main__':

    main()
```

**Output**
`97.4`

## Keywords arguments
Permiten pasar valores a una función utilizando los nombres de los parámetros como palabras clave. Esto no solo hace que tu código sea más legible, sino que también te da la libertad de pasar los argumentos en el orden que prefieras, especialmente útil cuando lidias con funciones que tienen múltiples parámetros.

```Python
# Keywords arguments
def report_product(name, quantity, country = "unknow"):
    print(f'Product: {name}')
    print(f'Quantity: {quantity}')
    print(f'Country: {country}')

def main():
    report_product(quantity=200, name="GadgetX", country="Perú")
    print("*" * 40)
    report_product(quantity=400, name="BookX")


if __name__ == '__main__':
    main()

```
**Output**

```Python
Product: GadgetX
Quantity: 200
Country: Perú
****************************************
Product: BookX
Quantity: 400
Country: unknow
```
