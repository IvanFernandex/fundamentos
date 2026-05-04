import string

"""Escribir un programa que lea un archivo de texto (por ejemplo, un capítulo de una obra literaria de
dominio público descargado de Project Gutenberg) y produzca un informe con:
(a) Cantidad total de caracteres, líneas y palabras del texto.

(b) La cantidad de apariciones de cada palabra distinta (normalizando a minúsculas y eliminando
signos de puntuación), presentada en orden descendente de frecuencia. Para palabras con igual
frecuencia, ordenar alfabéticamente.

(c) Las 20 palabras más frecuentes con su rango (posición 1 a 20) y frecuencia, para contrastar con la
Ley de Zipf.

(d) Escribir el informe completo en un archivo de salida resultados.txt.

def normalizar(palabra): # minúscula, sin puntuación

def buscar_palabra(tabla, palabra): # búsqueda binaria → índice o -1

def insertar_ordenado(tabla, palabra): # insert en posición correcta

def actualizar_frecuencia(tabla, palabra): # buscar + incrementar o insertar

def merge_sort_por_frecuencia(tabla): # estable, desc. por freq, asc. por palabra

def leer_y_contar(ruta): # lectura línea a línea

def escribir_informe(ruta, estadisticas, tabla_freq): # escritura del informe"""

def normalizar(palabra):
    # Eliminar signos de puntuación y convertir a minúsculas
    """Descripcion: Dado una palabra, esta función la normaliza eliminando signos de puntuación y convirtiéndola a minúsculas.
    Pre: palabra debe ser una cadena de texto.
    Post: Devuelve la palabra normalizada, sin signos de puntuación y en minúsculas."""
    return palabra.lower().strip(string.punctuation)

def buscar_palabra(tabla, palabra):
    """Descripcion: Realiza una búsqueda binaria en una tabla ordenada de palabras para encontrar la posición de una palabra específica.
    Pre: tabla debe ser una lista de tuplas (palabra, aparaciones) ordenada, palabra debe ser una cadena de texto.
    Post: Devuelve el índice de la palabra en la tabla si se encuentra, o -1 si no se encuentra."""
    izquierda = 0
    derecha = len(tabla) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if tabla[medio][0] == palabra:
            return medio
        elif tabla[medio][0] < palabra:
            izquierda = medio + 1
        else:
            derecha = medio - 1 
    return -1

def insertar_ordenado(tabla, palabra):
    """Descripcion: Inserta una palabra en una tabla ordenada de palabras mantieniendo el orden alfabético.
    Pre: tabla debe ser una lista de tuplas (palabra, aparaciones) ordenada, palabra debe ser una cadena de texto.
    Post: La palabra se inserta en la tabla en la posición correcta para mantener el orden alfabético."""
    i = 0
    while i < len(tabla) and tabla[i][0] < palabra:
        i += 1
    tabla.insert(i, (palabra, 1))

def actualizar_frecuencia(tabla :tuple, palabra: str) -> tuple:
    """Descripcion: Actualiza la freceuencia de una palabra en una lista de tuplas (palabra, aparaciones). Si la palabra no existe, se inserta en la tabla.
    Pre: tabla debe ser una lista de tuplas (palabra, aparaciones) ordenada, palabra debe ser una cadena de texto.
    Post: Si la palabra existe en la tabla, su frecuencia se incrementa en 1. Si no existe, se inserta con una frecuencia inicial de 1."""
    indice = buscar_palabra(tabla, palabra)
    if indice != -1: # se encontro la palabra, se incrementa su precuencia
        palabra_actual, frecuencia = tabla[indice]
        tabla[indice] = (palabra_actual, frecuencia + 1)
    else: # no se encontro la palabra, se inserta en la tabla
        insertar_ordenado(tabla, palabra)

def fusionar_frecuencia(izq, der):
    resultado = []
    i = 0
    j = 0
    while i < len(izq) and j < len(der):
        # Orden principal: frecuencia DESC
        if izq[i][1] > der[j][1]:
            resultado.append(izq[i])
            i += 1
        elif izq[i][1] < der[j][1]:
            resultado.append(der[j])
            j += 1
        else:
            # Empate → orden alfabético ASC
            if izq[i][0] <= der[j][0]:
                resultado.append(izq[i])
                i += 1
            else:
                resultado.append(der[j])
                j += 1
    # copiar resto
    while i < len(izq):
        resultado.append(izq[i])
        i += 1
    while j < len(der):
        resultado.append(der[j])
        j += 1
    return resultado

def merge_sort_por_frecuencia(tabla):
    """Descripcion: Ordena una tabla de palabras por frecuencia en orden descendente, y en caso de empate, por orden alfabético ascendente utilizando el algoritmo merge sort.
    Pre: tabla debe ser una lista de tuplas (palabra, aparaciones).
    Post: Devuelve una nueva lista de tuplas ordenada por frecuencia en orden descendente, y en caso de empate, por orden alfabético ascendente."""
    n = len(tabla)
    # Caso base: lista de 0 o 1 elementos ya está ordenada
    if n <= 1:
        return tabla[:]  # retornar una copia (no modificar la original)
    # Dividir: partir por la mitad
    medio = n >> 1     # equivalente a n // 2, pero más eficiente
    izq = merge_sort_por_frecuencia(tabla[:medio])
    der = merge_sort_por_frecuencia(tabla[medio:])
    # Combinar: fusionar las dos mitades ordenadas por frecuencia
    return fusionar_frecuencia(izq, der)

def leer_y_contar(ruta):
    """Descripcion: Lee un archivo de texto línea por línea, contando el número total de caracteres, líneas y palabras, y actualizando la frecuencia de cada palabra en una tabla.
    Pre: ruta debe ser una cadena de texto que representa la ruta al archivo a leer.
    Post: Devuelve una tupla con las estadísticas (total_caracteres, total_lineas, total_palabras) y una tabla de frecuencias de palabras."""
    total_caracteres = 0
    total_lineas = 0
    total_palabras = 0
    tabla_frecuencia = []

    with open(ruta, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            total_lineas += 1
            total_caracteres += len(linea)
            palabras = linea.split()
            total_palabras += len(palabras)
            for palabra in palabras:
                palabra_normalizada = normalizar(palabra)
                if palabra_normalizada: # evitar palabras vacías
                    actualizar_frecuencia(tabla_frecuencia, palabra_normalizada)
    return (total_caracteres, total_lineas, total_palabras), tabla_frecuencia

def escribir_informe(ruta, estadisticas, tabla_freq):
    """Descripcion: Escribe un informe completo en un archivo de salida con las estadísticas del texto y la frecuencia de palabras.
    Pre: ruta debe ser una cadena de texto que representa la ruta al archivo a escribir, estadisticas debe ser una tupla con las estadísticas (total_caracteres, total_lineas, total_palabras), tabla_freq debe ser una lista de tuplas (palabra, aparaciones) ordenada por frecuencia.
    Post: El informe completo se escribe en el archivo especificado por ruta."""
    with open(ruta, 'w', encoding='utf-8') as archivo:
        total_caracteres, total_lineas, total_palabras = estadisticas
        archivo.write(f"Cantidad total de caracteres: {total_caracteres}\n")
        archivo.write(f"Cantidad total de líneas: {total_lineas}\n")
        archivo.write(f"Cantidad total de palabras: {total_palabras}\n\n")
        archivo.write("Frecuencia de cada palabra distinta:\n")
        for palabra, frecuencia in tabla_freq:
            archivo.write(f"{palabra}: {frecuencia}\n")
        archivo.write("\nLas 20 palabras más frecuentes:\n")
        for i in range(min(20, len(tabla_freq))):
            palabra, frecuencia = tabla_freq[i]
            archivo.write(f"{i+1}. {palabra}: {frecuencia}\n")

def main():
    ruta_entrada = 'Ulpidio Vega - Fontanarrosa.txt'  # Cambia esto por la ruta de tu archivo de texto
    ruta_salida = 'resultados.txt'
    
    estadisticas, tabla_frecuencia = leer_y_contar(ruta_entrada)
    tabla_frecuencia_ordenada = merge_sort_por_frecuencia(tabla_frecuencia)
    escribir_informe(ruta_salida, estadisticas, tabla_frecuencia_ordenada)
main()
