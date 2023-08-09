# Continue y Break

## Introducción

Cuando trabajamos con estructuras de control como bucles `for` o `while`, a menudo queremos modificar el flujo del programa en función de ciertas condiciones. Aquí es donde entran en juego las instrucciones `continue` y `break`.

- **`continue`**: Esta instrucción se usa para pasar a la siguiente iteración del bucle, omitiendo el resto del código dentro de la iteración actual. Es útil cuando deseamos saltar ciertas iteraciones basadas en una condición, sin interrumpir por completo el bucle.
    
- **`break`**: Por otro lado, `break` se utiliza para salir inmediatamente de un bucle, independientemente de cuántas iteraciones aún queden por realizar. Se usa cuando alcanzamos una condición que requiere terminar completamente el bucle.

## Continue: Filtrado de datos defectuosos

Supongamos que estás trabajando en un proyecto de arquitectura de datos empresariales y estás procesando grandes cantidades de datos de sensores en una fábrica. Para garantizar la integridad de los datos, deseas filtrar aquellos que sean defectuosos o anómalos.

```Python
# Data
datos_sensor = [10, 25, -5, 30, -2, 15, 40]

def filtar_datos_defectuosos(data):
    datos_limpios = []
    for d in data:
        if d < 0:
            print(f'Dato defectuoso encontrado {d}')
            continue # Filtra el dato defectuoso
        datos_limpios.append(d)
    return datos_limpios

def main():
    data_limpiada = filtar_datos_defectuosos(datos_sensor)
    print(f'Los datos limpios encontrados son {data_limpiada}')

if __name__ == '__main__':
    main()
```

**Output**
```Python
Dato defectuoso encontrado -5
Dato defectuoso encontrado -2
Los datos limpios encontrados son [10, 25, 30, 15, 40]
```

## Break: Búsqueda eficiente de Datos

Supongamos que eres parte de un equipo que administra y analiza grandes volúmenes de datos en una empresa. Tu tarea es desarrollar un proceso que permita encontrar rápidamente un dato específico en un conjunto de datos masivo. Veamos cómo utilizar la instrucción `break` para lograr esto de manera eficiente.

```Python
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
    
def main():
    indice_objetivo = buscar_dato_efectivo(datos_empresa, 90)
    print(f'El indice objetivo es {indice_objetivo}')
if __name__ == '__main__':
    main()
```

**Output**
```Python
El dato 90 fue encontrado en el indice 3
El indice objetivo es 3
```