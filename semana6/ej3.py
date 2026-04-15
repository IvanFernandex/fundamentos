import random
import sys
sys.setrecursionlimit(10000) #Para evitar RecursionError en quick_sort con n=5000
from ej1 import ordenamiento_seleccion, ordenamiento_insercion, ordenamiento_burbuja
from ej2 import fusionar, merge_sort, medir_ordenamiento
random.seed(42) #Establecer semilla

"""Problema 3: Quick sort y laboratorio de medición de tiempos
Enunciado
Implementar la función quick_sort(datos) en su versión simplificada (no in-place), siguiendo la
implementación de la sección 7.3 del documento teórico.

A continuación, diseñar y ejecutar un experimento completo que compare los cinco algoritmos (selección,
inserción, burbuja, merge sort, quick sort) en tres escenarios:

Escenario A — Datos aleatorios: lista de n enteros generados con random.sample(range(1, 10 * n),
n).

Escenario B — Datos ya ordenados: la misma lista del Escenario A, pero ordenada previamente con
sorted().

Escenario C — Datos en orden inverso: la lista del Escenario A ordenada con sorted(reverse=True).

Para cada escenario y n ∈ {500, 1000, 2000, 5000}, medir tiempos y presentar una tabla. Analizar
especialmente:
• ¿Qué le pasa a inserción en el Escenario B (mejor caso)?
• ¿Qué le pasa a quick sort en el Escenario B con pivote = último (peor caso)? ¿Y si se elige pivote
aleatorio?
• ¿Cuál algoritmo gana en cada escenario?

Orientaciones para la resolución

Análisis: El Escenario B revela las diferencias adaptativas: inserción es O(n), burbuja con optimización es
O(n), selección sigue siendo O(n²), y quick sort con pivote último degrada a O(n²). Merge sort es O(n log
n) en todos los casos.

Diseño: Para quick sort con pivote aleatorio, modificar la función reemplazando pivote = datos[n
- 1] por idx = random.randint(0, n - 1) y luego intercambiar datos[idx] con datos[n
- 1] antes de particionar. Incluir ambas versiones en la tabla del Escenario B."""

def quick_sort(datos):
    '''Ordena la lista datos usando quick sort (versión simplificada).
    
    Precondición: datos es una lista de elementos comparables.
    Poscondición: retorna una NUEVA lista con los mismos elementos, ordenados.
    Complejidad: O(n log n) caso promedio, O(n²) peor caso.
    Nota: esta versión NO es in-place (crea listas auxiliares).
          La versión in-place clásica se estudiará en la Semana 11.
    '''
    n = len(datos)
    if n <= 1:
        return datos[:]

    pivote = datos[n - 1]
    menores = []
    mayores = []
    for i in range(n - 1):
        if datos[i] <= pivote:
            menores.append(datos[i])
        else:
            mayores.append(datos[i])

    return quick_sort(menores) + [pivote] + quick_sort(mayores)

def quick_sort_aleatorio(datos):
    '''Ordena la lista datos usando quick sort con pivote aleatorio (versión simplificada).
    
    Precondición: datos es una lista de elementos comparables.
    Poscondición: retorna una NUEVA lista con los mismos elementos, ordenados.
    Complejidad: O(n log n) caso promedio, O(n²) peor caso.
    Nota: esta versión NO es in-place (crea listas auxiliares).
          La versión in-place clásica se estudiará en la Semana 11.
    '''
    n = len(datos)
    if n <= 1:
        return datos[:]
    idx = random.randint(0, n - 1)
    datos[idx], datos[n - 1] = datos[n - 1], datos[idx]  # intercambiar pivote aleatorio con el último
    pivote = datos[n - 1]
    menores = []
    mayores = []
    for i in range(n - 1):
        if datos[i] <= pivote:
            menores.append(datos[i])
        else:
            mayores.append(datos[i])
    return quick_sort_aleatorio(menores) + [pivote] + quick_sort_aleatorio(mayores)

def main():
    print("=====ESCENARIO A - DATOS ALEATORIOS=====\n")
    tamanios = [500, 1000, 2000, 5000]
    print("Tamaño\tSelección\tInserción\tBurbuja\tMerge Sort\tQuick Sort")
    print("-"*75)
    for n in tamanios:
        datos = random.sample(range(1, n * 10), n)
        tiempo_seleccion = medir_ordenamiento(ordenamiento_seleccion, datos)
        tiempo_insercion = medir_ordenamiento(ordenamiento_insercion, datos)
        tiempo_burbuja = medir_ordenamiento(ordenamiento_burbuja, datos)
        tiempo_merge = medir_ordenamiento(merge_sort, datos)
        tiempo_quick = medir_ordenamiento(quick_sort, datos)
        print(f"{n}\t{tiempo_seleccion:.6f}\t{tiempo_insercion:.6f}\t{tiempo_burbuja:.6f}\t{tiempo_merge:.6f}\t{tiempo_quick:.6f}")
    print("\n=====ESCENARIO B - DATOS YA ORDENADOS======\n")
    print("Tamaño\tSelección\tInserción\tBurbuja\tMerge Sort\tQuick Sort\tQuick Sort Aleatorio")
    print("-"*75)
    for n in tamanios:
        datos = random.sample(range(1, n * 10), n)
        datos_ordenados = sorted(datos)
        tiempo_seleccion = medir_ordenamiento(ordenamiento_seleccion, datos_ordenados)
        tiempo_insercion = medir_ordenamiento(ordenamiento_insercion, datos_ordenados)
        tiempo_burbuja = medir_ordenamiento(ordenamiento_burbuja, datos_ordenados)
        tiempo_merge = medir_ordenamiento(merge_sort, datos_ordenados)
        tiempo_quick = medir_ordenamiento(quick_sort, datos_ordenados)
        tiempo_quick_aleatorio = medir_ordenamiento(quick_sort_aleatorio, datos_ordenados)
        print(f"{n}\t{tiempo_seleccion:.6f}\t{tiempo_insercion:.6f}\t{tiempo_burbuja:.6f}\t{tiempo_merge:.6f}\t{tiempo_quick:.6f}\t{tiempo_quick_aleatorio:.6f}")
    print("\n=====ESCENARIO C - DATOS EN ORDEN INVERSO======\n")
    print("Tamaño\tSelección\tInserción\tBurbuja\tMerge Sort\tQuick Sort")
    print("-"*75)
    for n in tamanios:
        datos = random.sample(range(1, n * 10), n)
        datos_inversos = sorted(datos, reverse=True)
        tiempo_seleccion = medir_ordenamiento(ordenamiento_seleccion, datos_inversos)
        tiempo_insercion = medir_ordenamiento(ordenamiento_insercion, datos_inversos)
        tiempo_burbuja = medir_ordenamiento(ordenamiento_burbuja, datos_inversos)
        tiempo_merge = medir_ordenamiento(merge_sort, datos_inversos)
        tiempo_quick = medir_ordenamiento(quick_sort, datos_inversos)
        print(f"{n}\t{tiempo_seleccion:.6f}\t{tiempo_insercion:.6f}\t{tiempo_burbuja:.6f}\t{tiempo_merge:.6f}\t{tiempo_quick:.6f}")
main()