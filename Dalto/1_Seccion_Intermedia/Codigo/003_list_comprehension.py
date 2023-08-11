# Ejercicio
# crea una lista que contenga los nombres de los países cuyas longitudes sean iguales o superiores a 10 caracteres.


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




