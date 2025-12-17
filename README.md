# Sistema Experto de Transporte 

## Objetivo del proyecto
Desarrollar un sistema lógico basado en las reglas dadas, que recomiende un medio de transporte según condiciones de: distancia, clima, y disponibilidad de transporte público.

## Descripción de la base de conocimiento
Los hechos se representan como un diccionario de Python con tres atributos:
- `"distancia"`: `"corta" | "media" | "larga"`
- `"clima"`: `"bueno" | "malo"`
- `"transporte_pub"`: `True | False`

## Casos utilizados y explicación
Se utilizaron 3 casos de ejemplo:
- distancia `corta`, clima `bueno`, transporte `False`
- distancia `media`, clima `malo`, transporte `True`
- distancia `larga`, clima `Any`, transporte `Any`
- Esto con el proposito de ver si correctamente se reparten a recomendar diferentes opciones, lo cuál si lo hacen.

## Instrucciones para ejecutar el proyecto
Ejecutar `sistema.py`
o en terminal correr: `python sistema.py`.
