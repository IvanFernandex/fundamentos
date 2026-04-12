import random
"""Enunciado
Implementar tres variantes de búsqueda lineal como funciones separadas:
(a) busqueda_lineal(datos, clave) — versión básica, sin reorganización.
(b) busqueda_lineal_mtf(datos, clave) — con heurística Move-to-Front: al encontrar la
clave, moverla a la posición 0.
(c) busqueda_lineal_transpose(datos, clave) — con heurística de Transposición: al
encontrar la clave, intercambiarla con el elemento inmediatamente anterior.
Las tres funciones deben retornar el índice donde se encontró la clave (o −1) y la cantidad de comparaciones realizadas.

A continuación, escribir un programa experimental que:
(a) Cree una lista inicial de 200 elementos distintos: datos = list(range(200)).
(b) Genere una secuencia de 1000 búsquedas donde un subconjunto pequeño de claves se
busca con mucha más frecuencia que el resto, por ejemplo claves_frecuentes =
random.choices(datos, k=5)para un conjunto de 5 claves frecuentes (experimentar
cambiando la cantidad de claves frecuentes). Usar random.choices(claves_frecuentes,
k=700) para las 700 búsquedas frecuentes y random.choices(range(200), k=300) para las
300 restantes. Mezclar ambas listas con random.shuffle.
(c) Ejecutar las 1000 búsquedas con cada variante (sobre copias independientes de la lista
original para las variantes con heurística) y acumular el total de comparaciones de cada una.
(d) Informar: total de comparaciones por variante y porcentaje de reducción respecto de la
búsqueda lineal básica: (1-comp_variante/comp_lineal)*100"""

NO_ENCONTRADO = -1

def busqueda_lineal(datos, clave):
    '''
    SECCIÓN DECLARATIVA
    Descripción: Buscar la posición de 'clave' en la secuencia 'datos'.
        Recorre la secuencia elemento a elemento hasta encontrar la
        clave o agotar todos los elementos.
    Precondición: datos es una secuencia indexable.
    Postcondición: retorna el índice i tal que datos[i] == clave,
        o -1 si clave no pertenece a datos.
    '''

    # --- SECCIÓN ALGORÍTMICA ---
    # Prólogo: obtener el tamaño de la secuencia
    n = len(datos)
    # Resolución: recorrer hasta encontrar o agotar
    comparaciones = 0
    i = 0
    while i < n:
        comparaciones += 1
        if datos[i] == clave:
            return i, comparaciones      # encontrado
        i += 1
    # Epílogo: inspección post-bucle
    return NO_ENCONTRADO, comparaciones          # no encontrado

def busqueda_lineal_mtf(datos, clave):
    """SECCIÓN DECLARATIVA
    Descripción: Buscar la posición de 'clave' en la secuencia 'datos' usando heurística Move-to-Front, al encontrar la clave, moverla a la posición 0.
    Precondiccion: datos sea una seccuencia indexable.
    Postcondición: retorna el índice  y la cantidad de comparaciones realizadas, o -1 si clave no pertenece a datos."""
    #==================================
    #SECCIÓN ALGORÍTMICA
    #==================================
    #1) Prólogo: obtener el tamaño de la secuencia
    tamaño_secuencia = len(datos)
    #2) Resolución: recorrer hasta encontrar o agotar
    comparaciones = 0
    i = 0
    while i < tamaño_secuencia:
        comparaciones += 1
        if datos[i] == clave:
            #Encontrado y aplicamos algoritmo
            encontrado = datos.pop(i) #Removemos el elemento encontrado
            datos.insert(0, encontrado) #Lo insertamos al inicio de la lista
            return (0, comparaciones) #Nueva posicion (0)
        i += 1
    return (NO_ENCONTRADO, comparaciones) #No encontrado
    
def busqueda_lineal_transpose(datos, clave):
    """SECCION DECLARATIVA
    Descripcion: Busqueda lineal con hueristica de transposicion, al encontrar la clave, intercambiarla con el elemento inmediatamente anterior."""
    #==================================
    #SECCIÓN ALGORÍTMICA
    #==================================
    #1) Prólogo: obtener el tamaño de la secuencia y comparaciones
    tamaño_secuencia = len(datos)
    comparaciones = 0
    i = 0
    while i < tamaño_secuencia:
    #2) Resolución: recorrer hasta encontrar o agotar
        comparaciones += 1
        if datos[i] == clave:
            if i > 0:
                #3) Epílogo: Si el elemento encontrado no es el primero, se intercambia con el anterior y retornamos la posicion actualizada, sino se retorna la misma posición (0).
                datos[i], datos[i-1] = datos[i-1], datos[i]
                return (i - 1, comparaciones) #Nueva posicion (i-1)
            else:
                return (i, comparaciones)
        i += 1
    return (NO_ENCONTRADO, comparaciones)
    

#Crear lista de 200 elementos distintos
def generar_lista():
    """SECCION DECLARATIVA
    Descripción: Genera una lista de 200 elementos distintos.
    Postcondición: Retorna una lista de 200 elementos distintos."""
    return list(range(200))
    
def generar_secuencia_busquedas(datos):
    """SECCION DECLARATIVA
    Descricion: Dada una lista de datos, genera una secuencia de 1000 busquedas donde un conjunto de claves se busca con mucha mas frecuencia que el resto.
    Precondición: datos es una lista de elementos distintos.
    Postcondición: Retorna una scuencia de 1000 busquedas con claves frecuentes y no frecuentes."""
    claves_frecuentes = random.choices(datos, k=5)
    busquedas = (random.choices(claves_frecuentes, k=700) + random.choices(datos, k=300))
    random.shuffle(busquedas)
    return busquedas

def ejecutar_busquedas(datos, secuencia_busquedas):
    """SECCION DECLARATIVA
    Descripción: Ejecuta las 1000 búsquedas con cada variante (sobre copias independientes de la lista original para las variantes con heurística) y acumula el total de comparaciones de cada una.
    Precondición: datos es una lista de elementos distintos, secuencia_busquedas es una lista de claves a buscar.
    Postcondición: Retorna una lista con el total de comparaciones por cada variante."""
    #Crear copias independientes de la lista original para cada variante
    datos_lineal = datos.copy()
    datos_mtf = datos.copy()
    datos_trans = datos.copy()

    comparaciones_lineal = 0
    comparaciones_mtf = 0
    comparaciones_trans = 0

    for clave in secuencia_busquedas:
        _, comparaciones = busqueda_lineal(datos_lineal, clave)
        comparaciones_lineal += comparaciones

        _, comparaciones = busqueda_lineal_mtf(datos_mtf, clave)
        comparaciones_mtf += comparaciones

        _, comparaciones = busqueda_lineal_transpose(datos_trans, clave)
        comparaciones_trans += comparaciones

    return comparaciones_lineal, comparaciones_mtf, comparaciones_trans

def main():
    """SECCION DECLARATIVA
    Desscripcion: Programa principal que ejecuta las tres variantes de búsqueda lineal y acumula el total de comparaciones realizadas por cada una.
    """
    random.seed(42)
    #a) Crear una lista inicial de 200 elementos distintos
    datos = generar_lista()
    #b) Generar una secuencia de 1000 búsquedas con claves frecuentes y no frecuentes
    secuencia_busquedas = generar_secuencia_busquedas(datos)
    #c) Ejecutar las 1000 búsquedas con cada variante y acumular el total de comparaciones de cada una
    comp_lineal, comp_mtf, comp_trans = ejecutar_busquedas(
        datos, secuencia_busquedas
    )
    #d) Informar: total de comparaciones por variante y porcentaje de reducción respecto de la búsqueda lineal básica
    print("=== RESULTADOS ===")
    print(f"Lineal básica: {comp_lineal}")
    print(f"Move-to-Front: {comp_mtf}")
    print(f"Transposición: {comp_trans}")

    print("\n=== REDUCCIÓN (%) ===")
    #fórmula de reducción: (1-comp_variante/comp_lineal)*100
    red_mtf = (1 - comp_mtf / comp_lineal) * 100
    red_trans = (1 - comp_trans / comp_lineal) * 100

    print(f"MTF: {red_mtf:.2f}%")
    print(f"Transposición: {red_trans:.2f}%")
main()
    