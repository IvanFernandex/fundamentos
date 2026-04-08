import random
"""Enunciado
Implementar dos funciones de búsqueda en Python: busqueda_lineal(datos, clave) y
busqueda_binaria(datos, clave). Ambas reciben una secuencia y una clave, y retornan el
índice de la clave en la secuencia o −1 si no se encuentra. La búsqueda binaria debe documentar
como precondición que la secuencia está ordenada.
A continuación, escribir un programa que:
Fundamentos de Programación y Algoritmos y Programación I — Semana 5 — Problemas de Programación
Página 2
(a) Genere una lista ordenada de n enteros distintos usando random.sample(range(1, 10 *
n), n) seguido de sort(), con n = 1000. Fijar la semilla con random.seed(42).
(b) Para cada función de búsqueda, busque 10 claves: 5 presentes en la lista (elegidas con
random.sample(datos, 5)) y 5 ausentes (enteros negativos). Verificar que ambas funciones
retornan los mismos resultados.
(c) Informar para cada búsqueda: la clave buscada, el índice retornado y la cantidad de
comparaciones realizadas (agregar un contador dentro de cada función)"""


def busqueda_lineal(datos, clave, contar=False):
    '''
    SECCIÓN DECLARATIVA
    Descripción: Buscar la posición de 'clave' en la secuencia 'datos'.
        Recorre la secuencia elemento a elemento hasta encontrar la
        clave o agotar todos los elementos.
    Precondición: datos es una secuencia indexable; clave es comparable
        con los elementos de datos mediante ==.
    Postcondición: retorna el índice i tal que datos[i] == clave,
        o -1 si clave no pertenece a datos.
    '''

    # --- SECCIÓN ALGORÍTMICA ---
    # Prólogo: obtener el tamaño de la secuencia
    n = len(datos)
    # Resolución: recorrer hasta encontrar o agotar
    contador = 0
    i = 0
    while i < n and datos[i] != clave:
        i += 1
        contador += 1
    # Epílogo: inspección post-bucle
    if i < n:
        return (i, contador) if contar else i        # encontrado
    else:
        return (-1, contador) if contar else -1      # no encontrado
    
def busqueda_binaria(datos, clave, contar=False):
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
            return (medio, comparaciones) if contar else medio             # encontrado
        elif clave < datos[medio]:
            der = medio - 1        # descartar mitad derecha
        else:
            izq = medio + 1        # descartar mitad izquierda
    # Epílogo: la región quedó vacía (izq > der)
    return (-1, comparaciones) if contar else -1    

def generar_listas():
    random.seed(42)
    n = 1000
    datos = random.sample(range(1, 10 * n), n)
    return sorted(datos)

def generar_claves(datos):
    claves_presentes = random.sample(datos, 5)
    claves_ausentes = [-i for i in range(1, 6)]
    claves_totales = claves_presentes + claves_ausentes
    return claves_totales

def main():
    datos = generar_listas()
    claves = generar_claves(datos)
    #Hacer el programa sin utilizar contar=true
    print("--- Búsqueda Lineal ---")
    for clave in claves:
        indice = busqueda_lineal(datos, clave)
        print(f"Índice: {indice}")

    print("\n--- Búsqueda Binaria ---")
    for clave in claves:
        indice = busqueda_binaria(datos, clave)
        print(f"Índice: {indice}")

main()