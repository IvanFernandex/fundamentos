import random

"""Integrantes del grupo:
- Ivan Fernandez (Curso 05)
- Martin Chara (Curso 06)
- Juan Pablo Consenza (Curso 06)"""

#Variable global para indicar que no se encontro la clave, para evitar usar -1 directamente en el código y mejorar legibilidad
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
                return (izq,comparaciones)
            return (NO_ENCONTRADO,comparaciones)
        # Estimar posición por interpolación lineal
        pos = izq + (clave - datos[izq]) * (der - izq) // (datos[der] - datos[izq])
        if datos[pos] == clave:
            return (pos,comparaciones)
        elif datos[pos] < clave:
            izq = pos + 1
        else:
            der = pos - 1

    return (NO_ENCONTRADO,comparaciones)

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
    # Epílogo: la región quedó vacía (izq > der), no se encontro
    return (NO_ENCONTRADO, comparaciones)

#ESCENARIO A - Distribucion uniforme
def generacion_uniforme(n):
    """SECCION DECLARATIVA
    Descripcion: Genera una lista ordenada de n enteros distintos con distribución uniforme.
    Precondición: n es un entero positivo.
    Postcondición: Retorna una lista ordenada de n enteros distintos con distribución uniforme."""
    return sorted(random.sample(range(1, 100001), n))

#Escenario B - Distribucion exponencial
def generacion_exponencial(n):
    """SECCION DECLARATIVA
    Descripcion: Genera una lista garantizando n elementos unicos con distribución exponencial (sesgada).
    Precondicion: n es un entero positivo.
    Postcondicion: Retrona una lista ordenada de n enteros distintos con distribución exponencial."""
    vals = set()
    while len(vals) < n:
        vals.add(int(random.expovariate(1) * 10000))
    return sorted(vals)

#Escenario C - Distribucion con clusters
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


def experimento(nombre_escenario, datos_escenario, claves_escenario):
    """SECCION DECLARATIVA
    Descripción: Ejecuta el experimento de comparación entre búsqueda binaria e interpolación para un escenario dado.
    Precondición: nombre_escenario es una cadena descriptiva del escenario, datos_escenario es una lista ordenada de enteros, claves_escenario es una lista de enteros presentes en datos_escenario.
    Postcondición: Imprime el promedio de comparaciones para cada algoritmo y cuál es más eficiente."""
    #================================
    #SECCIÓN ALGORÍTMICA
    #================================
    total_binaria = 0
    total_interpolacion = 0
    #1) Prólogo: inicializar contadores de comparaciones y recorrer cada clave a buscar para ambos algoritmos y acumular el total de comparaciones
    for clave in claves_escenario:
        indice_bin, comparaciones_binarias = busqueda_binaria(datos_escenario, clave)
        indice_inter, comparaciones_interpolacion = busqueda_interpolacion(datos_escenario, clave)

        total_binaria += comparaciones_binarias
        total_interpolacion += comparaciones_interpolacion
    #2) Desarrollo: calcular el promedio de comparaciones para cada algoritmo y determinar cuál es más eficiente
    prom_binaria = total_binaria / len(claves_escenario)
    prom_interpolacion = total_interpolacion / len(claves_escenario)
    #3) Epílogo: imprimir los resultados y cuál algoritmo es más eficiente
    print(f"\nRESULTADOS ESCENARIO {nombre_escenario}:")
    print(f" Binaria: {prom_binaria}")
    print(f" Interpolación: {prom_interpolacion}")

    if prom_binaria < prom_interpolacion:
        print("Mejor --> Binaria")
    else:
        print("Mejor --> Interpolación")

def main():
    random.seed(42) # Estabecer semilla
    n = 10000
    #1) Prólogo: generar los datos y claves para cada escenario
    #Escenario A - Distribucion uniforme
    datos_uniforme = generacion_uniforme(n)
    claves_uniforme = random.sample(datos_uniforme, 500)

    #Escenario B - Distribucion exponencial
    datos_exponencial = generacion_exponencial(n)
    claves_exponencial = random.sample(datos_exponencial, 500)

    #Escenario C - Distribucion con clusters
    datos_clusters = generacion_clusters(n)
    claves_clusters = random.sample(datos_clusters, 500)
    #2) Desarrollo y epílogo: ejecutar el experimento de comparación entre búsqueda binaria e interpolación para cada escenario
    #Comparar algoritmos en cada escenario
    print("=== RESULTADOS ===")
    experimento("A", datos_uniforme, claves_uniforme)
    experimento("B", datos_exponencial, claves_exponencial)
    experimento("C", datos_clusters, claves_clusters)
main()
