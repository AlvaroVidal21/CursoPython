import generador_datos 
import analisis_tendencias


def main():
    numero_encuestas = int(input("Ingrese el número de encuestas a generar: "))

    # Generamos los datos
    encuestas = generador_datos.generador_datos(numero_encuestas)

    # Analizamos los datos generados
    analisis_tendencias.analizar_tendencias(encuestas)


if __name__ == "__main__":
    main()