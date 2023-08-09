
# Data para el CONTINUE
datos_sensor = [10, 25, -5, 30, -2, 15, 40]

# Data para el BREAK
datos_empresa = [120, 150, 200, 90, 180, 200, 220]



def buscar_dato_efectivo(data, objetivo):
    indice_objetivo = 0
    for indice, d in enumerate(data):
        if d == objetivo:
            print(f'El dato {objetivo} fue encontrado en el indice {indice}')
            indice_objetivo = indice
            break
    
    return indice_objetivo


def filtar_datos_defectuosos(data):
    datos_limpios = []
    for d in data:
        if d < 0:
            print(f'Dato defectuoso encontrado {d}')
            continue
        datos_limpios.append(d)
    
    return datos_limpios


def main():
    # data_limpiada = filtar_datos_defectuosos(datos_sensor)
    # print(f'Los datos limpios encontrados son {data_limpiada}')

    indice_objetivo = buscar_dato_efectivo(datos_empresa, 90)
    print(f'El indice objetivo es {indice_objetivo}')

if __name__ == '__main__':
    main()