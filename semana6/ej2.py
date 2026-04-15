import random
random.seed(42)
import time
from ej1 import ordenamiento_seleccion, ordenamiento_insercion, ordenamiento_burbuja
"""Implementar las funciones fusionar(izq, der) y merge_sort(datos) siguiendo el diseño de
la clase teórica. La función merge_sort retorna una nueva lista ordenada (no modifica la original).

A continuación, escribir un programa que:
(a) Genere listas pseudoaleatorias de tamaños n ∈ {100, 500, 1000, 5000} con random.seed(42) para
cada tamaño.

(b) Para cada n, mida el tiempo de ejecución de selección, inserción, burbuja y merge sort usando
time.perf_counter(). Repetir 3 veces y promediar.

(c) Presente una tabla de resultados y calcule el ratio Selección/MergeSort para cada n.

(d) Analice: ¿El ratio crece cuando n se duplica? ¿Qué relación tiene con O(n²)/O(n log n) = O(n/log
n)?
Orientaciones para la resolución:
Análisis: El objetivo es verificar empíricamente que merge sort escala mejor que los cuadráticos. El ratio
O(n²)/O(n log n) = O(n/log n) crece con n: para n = 100, n/log₂(n) ≈ 15; para n = 5000, ≈ 408.

Diseño: Estructura modular recomendada: una función medir_ordenamiento(funcion, datos,
repeticiones) que retorna el tiempo promedio. Para los algoritmos in-place, pasar datos.copy() en cada
repetición. Para merge sort, como retorna una nueva lista, pasar la original directamente."""

def fusionar(izq, der):
    '''Fusiona dos listas ordenadas en una sola lista ordenada.
    
    Precondición: izq y der están ordenadas en forma no decreciente.
    Poscondición: retorna una nueva lista con todos los elementos
                 de izq y der, ordenados. No modifica las originales.
    Complejidad: O(n) donde n = len(izq) + len(der).
    '''
    resultado = []
    i = 0
    j = 0

    # Fase 1: comparar y copiar el menor de ambas listas
    while i < len(izq) and j < len(der):
        if izq[i] <= der[j]:     # <= para estabilidad
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1

    # Fase 2: copiar los restantes de la lista que no se agotó
    while i < len(izq):
        resultado.append(izq[i])
        i += 1
    while j < len(der):
        resultado.append(der[j])
        j += 1

    return resultado 

def merge_sort(datos):
    '''Ordena la lista datos usando el algoritmo merge sort.
    
    Precondición: datos es una lista de elementos comparables.
    Poscondición: retorna una NUEVA lista con los mismos elementos, ordenados.
    Complejidad: O(n log n) en todos los casos.
    Memoria auxiliar: O(n).
    Estabilidad: estable.
    '''
    n = len(datos)

    # Caso base: lista de 0 o 1 elementos ya está ordenada
    if n <= 1:
        return datos[:]  # retornar una copia (no modificar la original)

    # Dividir: partir por la mitad
    medio = n >> 1     # equivalente a n // 2, pero más eficiente
    izq = merge_sort(datos[:medio])
    der = merge_sort(datos[medio:])

    # Combinar: fusionar las dos mitades ordenadas
    return fusionar(izq, der)

def generar_lista_aleatoria(cantidad):
    '''Descripcion: Genera una lista de enteros pseudoaleatorias en el rango [1, cantidad*10].
    Pre: Cantidad debe ser un entero positivo.
    Post: Devuelve una lista de longitud cantidad con enteros aleatorios.'''
    return random.sample(range(1, cantidad * 10), cantidad)

def medir_ordenamiento(funcion, datos, repeticiones=3):
    '''Descripción: Mide el tiempo promedio de ejecución de una función de ordenamiento.
    Precondición: funcion es una función que ordena una lista in-place o retorna una nueva lista ordenada.datos es la lista a ordenar (no se modifica).repeticiones es un entero positivo.
    Postcondición: Retorna el tiempo promedio en segundos que tarda funcion en ordenar datos.'''

    tiempo_total = 0.0
    for repeticion in range(repeticiones):
        datos_ordenados = datos.copy()  # para in-place, pasar una copia; para merge_sort, no afecta
        incio = time.perf_counter()
        funcion(datos_ordenados)  # llamar a la función de ordenamiento
        fin = time.perf_counter()
        tiempo_total += (fin - incio)
    return tiempo_total / repeticiones

def main():
    tamanios = [100, 500, 1000, 5000]
    # Imprimir la tabla
    print("Tamaño\tSelección\tInserción\tBurbuja\t  Merge Sort\tRatio(Selección/Merge)")
    print("-"*75)
    for n in tamanios:
        datos = generar_lista_aleatoria(n)
        tiempo_seleccion = medir_ordenamiento(ordenamiento_seleccion, datos)
        tiempo_insercion = medir_ordenamiento(ordenamiento_insercion, datos)
        tiempo_burbuja = medir_ordenamiento(ordenamiento_burbuja, datos)
        tiempo_merge = medir_ordenamiento(merge_sort, datos)
        ratio = tiempo_seleccion / tiempo_merge if tiempo_merge > 0 else float('inf')
        # Imprimir los resultados dicho tamaño n con los tiempos en 6 decimales y el ratio con 2 decimales
        print(f"{n}\t{tiempo_seleccion:.6f}\t{tiempo_insercion:.6f}\t{tiempo_burbuja:.6f}\t{tiempo_merge:.6f}\t{ratio:.2f}")
main()