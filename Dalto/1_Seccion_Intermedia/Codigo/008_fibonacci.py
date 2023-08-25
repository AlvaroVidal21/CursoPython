
def fibonacci(numero):
    a, b = 0, 1
    fibonacci_lista = list()

    for i in range(numero):
        if b > numero : return fibonacci_lista
        else: 
            fibonacci_lista.append(b)
            a, b = b, a+b


def main():
    resultado = fibonacci(34)
    print(resultado)


if __name__ == '__main__':
    main()