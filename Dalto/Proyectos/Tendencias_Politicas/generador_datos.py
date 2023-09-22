# Generador de datos

import random

def generador_datos(numero_encuestas):
    encuentas = []

    for _ in range (numero_encuestas):
        pregunta = f'Pregunta {_ + 1}'
        rp_si = random.randint(30,70)
        rp_no = 100 - rp_si
        resultados = {
            "Si" : rp_si,
            "No" : rp_no
        }

        encuentas.append({
            "pregunta": pregunta,
            "resultados": resultados
        })

    return encuentas
    

