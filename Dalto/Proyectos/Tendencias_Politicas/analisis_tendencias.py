# analizador.py
import generador_datos

encuentas = generador_datos.generador_datos(1)

def analizar_tendencias(encuestas):
    
    print("Análisis de Tendencias Políticas:")
    
    for encuesta in encuestas:
        pregunta = encuesta["pregunta"]
        resultados = encuesta["resultados"]
        print(f'Pregunta: {pregunta}')
       
        for opcion, porcentaje in resultados.items():
            print(f"{opcion}: {porcentaje}%")
        print("---")
