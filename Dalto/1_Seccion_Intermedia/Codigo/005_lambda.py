
notas = [18, 11, 14, 5, 19, 9, 5, 13, 20]


# Función lambda que aumenta en 2 la nota
bonus_notas = map(lambda nota : nota +2, notas)
bonus_notas = list(bonus_notas)


# Función lambda que filtra las notas aprobatorias
notas_aprobatorias = filter (lambda nota : nota>=11, bonus_notas) # No hace falta poner: list(bonus_notas)
notas_aprobatorias = list(notas_aprobatorias)

# Función lambda para filtrar las notas desaprobatorias
notas_desaprobatorias = filter (lambda nota : nota<11, bonus_notas)



def main():
    print(list(bonus_notas))
    print(list(notas_aprobatorias))

          


if __name__ == '__main__':
    main()