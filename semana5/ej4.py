import random
"""Enunciado
Implementar la función busqueda_interpolacion(datos, clave) según el algoritmo
presentado en la clase teórica. La función debe retornar el índice (o −1) y la cantidad de
comparaciones realizadas.
Escribir un programa que compare búsqueda binaria vs. interpolación en tres escenarios con
listas de n = 10.000 elementos:
Escenario A — Distribución uniforme: generar la lista con datos =
sorted(random.sample(range(1, 100001), n)). Buscar 500 claves presentes elegidas al
azar.
Escenario B — Distribución exponencial (sesgada): los valores están concentrados cerca de
cero con cola larga. Generar la lista garantizando n elementos únicos:
vals = set()
while len(vals) < n:
vals.add(int(random.expovariate(1) * 10000))
datos = sorted(vals)
Buscar 500 claves presentes elegidas al azar con random.sample(datos, 500).
Escenario C — Distribución con clusters: 5 grupos de 2000 elementos separados por vacíos.
Generar la lista con exactamente n/5 elementos únicos por cluster:
centros = [5000, 25000, 50000, 75000, 95000]
vals = set()
for c in centros:
cluster = set()
while len(cluster) < n // 5:
cluster.add(random.randint(c - 2500, c + 2500))
vals |= cluster
datos = sorted(vals)
Buscar 500 claves presentes elegidas al azar. Los grandes vacíos entre clusters (~15.000–
20.000 unidades) provocan estimaciones erráticas en la búsqueda por interpolación.
Para cada escenario, informar: promedio de comparaciones por búsqueda para cada algoritmo,
y cuál es más eficiente"""

NO_ENCONTRADO = -1

def busqueda_interpolacion(datos, clave):
    '''
    SECCIÓN DECLARATIVA
    Descripción: Buscar 'clave' en la secuencia ordenada 'datos' usando
        interpolación lineal para estimar la posición.
    Precondición: datos está ordenado de menor a mayor y contiene valores
        numéricos.
    Postcondición: Retorna el indice de la clave si se encuentra, o -1 si no se encuentra ademas de la cantidad de comparaciones realizadas.
    '''
    # --- SECCIÓN ALGORÍTMICA ---
    izq = 0
    der = len(datos) - 1
    comparaciones = 0
    while izq <= der and datos[izq] <= clave <= datos[der]:
        # Evitar división por cero cuando todos los valores son iguales
        comparaciones += 1
        if datos[izq] == datos[der]:
            if datos[izq] == clave:
                return izq,comparaciones
            return NO_ENCONTRADO,comparaciones
        # Estimar posición por interpolación lineal
        pos = izq + (clave - datos[izq]) * (der - izq) // (datos[der] - datos[izq])
        if datos[pos] == clave:
            return pos,comparaciones
        elif datos[pos] < clave:
            izq = pos + 1
        else:
            der = pos - 1

    return NO_ENCONTRADO,comparaciones

def busqueda_binaria(datos, clave):
    '''
    SECCIÓN DECLARATIVA
    Descripción: Buscar la posición de 'clave' en la secuencia ordenada 'datos'
        usando búsqueda binaria (versión iterativa).
    Precondición: datos está ordenado de menor a mayor.
    Postcondición: retorna el índice i tal que datos[i] == clave,
        o -1 si clave no pertenece a datos.
    '''
    # --- SECCIÓN ALGORÍTMICA ---
    # Prólogo: definir la región de búsqueda
    izq = 0
    der = len(datos) - 1
    comparaciones = 0
    # Resolución: dividir la región a la mitad en cada paso
    while izq <= der:
        medio = (izq + der) // 2
        comparaciones += 1

        if datos[medio] == clave:
            return (medio, comparaciones)             # encontrado
        elif clave < datos[medio]:
            der = medio - 1        # descartar mitad derecha
        else:
            izq = medio + 1        # descartar mitad izquierda
    # Epílogo: la región quedó vacía (izq > der)
    return (NO_ENCONTRADO, comparaciones)

#ESCENARIO A - Distribucion uniforme
def generacion_uniforme(n):
    """SECCION DECLARATIVA
    Descripcion: Genera una lista ordenada de n enteros distintos con distribución uniforme.
    Precondición: n es un entero positivo.
    Postcondición: Retorna una lista ordenada de n enteros distintos con distribución uniforme."""
    return sorted(random.sample(range(1, 100001), n))

def generacion_exponencial(n):
    """SECCION DECLARATIVA
    Descripcion: Genera una lista garantizando n elementos unicos con distribución exponencial (sesgada).
    Precondicion: n es un entero positivo.
    Postcondicion: Retrona una lista ordenada de n enteros distintos con distribución exponencial."""
    vals = set()
    while len(vals) < n:
        vals.add(int(random.expovariate(1) * 10000))
    return sorted(vals)

def generacion_clusters(n):
    """SECCION DECLARATIVA
    Descripcion: Genera una lista ordenada de n enteros distintos con distribución de clusters.
    Precondición: n es un entero positivo.
    Postcondición: Retorna una lista ordenada de n enteros distintos con distribución de clusters."""
    centros = [5000, 25000, 50000, 75000, 95000]
    vals = set()
    for c in centros:
        cluster = set()
        while len(cluster) < n // 5:
            cluster.add(random.randint(c - 2500, c + 2500))
        vals |= cluster
    return sorted(vals)

def comparar_algoritmos(datos, claves):
    """SECCION DECLARATIVA
    Descripcion: Compara el rendimiento de búsqueda lineal e interpolación en una lista de datos dada una lista de claves.
    Precondición: datos es una lista ordenada de enteros, claves es una lista de enteros presentes en datos.
    Postcondición: Devuelve el promedio de comparaciones realizadas por cada búsqueda."""
    #1) Prólogo: Inicializar contadores de comparaciones para ambos algoritmos
    total_comparaciones_lineal = 0
    total_comparaciones_interpolacion = 0
    cantidad_claves = len(claves)
    for clave in claves:
        #2) Desarrollo: Buscar cada clave con ambos algoritmos (lineal e interpolación) y acumular el total de comparaciones de cada una.
        indice, comp_binaria = busqueda_binaria(datos, clave)
        indice, comp_interpolacion = busqueda_interpolacion(datos, clave)
        total_comparaciones_lineal += comp_binaria
        total_comparaciones_interpolacion += comp_interpolacion
    #3) Epílogo: Informar el promedio de comparaciones por variante (lineal e interpolación)
    promedio_binaria = total_comparaciones_lineal / cantidad_claves
    promedio_interpolacion = total_comparaciones_interpolacion / cantidad_claves

    return promedio_binaria, promedio_interpolacion

def main():
    random.seed(42) # Semilla para reproducibilidad
    n = 10000
    #Escenario A - Distribucion uniforme
    datos_uniforme = generacion_uniforme(n)
    claves_uniforme = random.sample(datos_uniforme, 500)
    #Escenario B - Distribucion exponencial
    datos_exponencial = generacion_exponencial(n)
    claves_exponencial = random.sample(datos_exponencial, 500)
    #Escenario C - Distribucion con clusters
    datos_clusters = generacion_clusters(n)
    claves_clusters = random.sample(datos_clusters, 500)

    #Comparar algoritmos en cada escenario
    print("=== ESCENARIO A - Distribución uniforme ===")
    promedio_binaria, promedio_interpolacion = comparar_algoritmos(datos_uniforme, claves_uniforme)
    print(f"Promedio de comparaciones - Búsqueda binaria: {promedio_binaria}")
    print(f"Promedio de comparaciones - Búsqueda interpolación: {promedio_interpolacion}")
    print("\n=== ESCENARIO B - Distribución exponencial ===")
    promedio_binaria, promedio_interpolacion = comparar_algoritmos(datos_exponencial, claves_exponencial)
    print(f"Promedio de comparaciones - Búsqueda binaria: {promedio_binaria}")
    print(f"Promedio de comparaciones - Búsqueda interpolación: {promedio_interpolacion}")
    print("\n=== ESCENARIO C - Distribución con clusters ===")
    promedio_binaria, promedio_interpolacion = comparar_algoritmos(datos_clusters, claves_clusters)
    print(f"Promedio de comparaciones - Búsqueda binaria: {promedio_binaria}")
    print(f"Promedio de comparaciones - Búsqueda interpolación: {promedio_interpolacion}")
main()
