
def es_primo(num):
    for n in range(2, num-1): # Evaluamos todas las divisiones a partir de 2 y un número menos del número en cuestión, si es divisible, se concluye que no es primo
        if num%n == 0 : return False
            
    return True # al no ser divisible con ninguno de los números evaluados, concluimos que es primo


def primos_until(num):
    primos = list() # Aquí se almacenará todos los números primos
    
    for numero in range (2, num+1): # Usamos num+1 para que en caso el número proporcionado es primo sea incluido en la lista
        valor = es_primo(numero)

        if valor == True : primos.append(numero)

    return primos


def main():
    lista_primos = primos_until(19)
    print(lista_primos)


if __name__ == '__main__':
    main()