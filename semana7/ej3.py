"""Enunciado:
Retomar la función ordenamiento_seleccion(datos) de la Semana 6 y la función ordenar_sin_modificar(datos) de la Sección 6.3 del documento teórico de esta semana. 
Escribir un programa que:
(a) Genere una lista de 10 enteros pseudoaleatorios en [1, 50] con random.seed(42).
(b) Invoque ordenamiento_seleccion sobre una copia de la lista. Imprimir el id() antes y después. Verificar que el id no cambia (mismo objeto, modificado in-place).
(c) Invoque ordenar_sin_modificar pasando la lista original. Imprimir el id() de la lista original y del resultado. Verificar que los id son diferentes y que la lista original no se modificó.
(d) Comparar con el comportamiento de sorted() (built-in) y .sort() (método de lista).
(e) Escribir una tabla comparativa como comentario multilínea al final del programa."""

import random

def ordenamiento_seleccion(datos, contar=False):
    largo_secuencia = len(datos)
    cant_comparaciones = 0
    cant_intercambios = 0

    for elemento in range(largo_secuencia -1):
        pos_min = elemento
        for i in range(elemento + 1, largo_secuencia):
            cant_comparaciones += 1
            if datos[i] < datos[pos_min]:
                pos_min = i
        if pos_min != elemento:
            datos[elemento], datos[pos_min] = datos[pos_min], datos[elemento]
            cant_intercambios += 1
    return (datos, cant_comparaciones, cant_intercambios) if contar else datos

def ordenar_sin_modificar(datos):
    """Devuelve una nueva lista con los datos ordenados.

    Precondición: datos es una lista de elementos comparables.
    Postcondición: retorna una nueva lista ordenada; la original NO se modifica.
    """
    copia = datos[:]     # Copia superficial: trabajamos sobre la copia
                         # Ordenamiento por selección sobre la copia
    for i in range(len(copia) - 1):
        pos_min = i
        for j in range(i + 1, len(copia)):
            if copia[j] < copia[pos_min]:
                pos_min = j
        copia[i], copia[pos_min] = copia[pos_min], copia[i]
    return copia
#a)
def generar_lista_aleatoria():
    random.seed(42)
    datos = random.sample(range(1,51),10)
    return datos

#b)
def experimento_ordenamiento_seleccion(datos):
    print("===EXPERIMENTO ordenamiento_seleccion ===")
    print("Lista original:", datos)
    print("id(datos) antes:", id(datos))
    ordenamiento_seleccion(datos)
    print("Lista después:", datos)
    print("id(datos) después:", id(datos))
    return datos

def main():
    datos = generar_lista_aleatoria()
    experimento_ordenamiento_seleccion(datos)
    copia_ordenada = ordenar_sin_modificar(datos)
    print("\n===EXPERIMENTO ordenar_sin_modificar ===")
    print("Lista original:", datos)
    print("id(datos) original:", id(datos))
    print("Lista ordenada:", copia_ordenada)
    print("id(copia_ordenada):", id(copia_ordenada))
    # Comparar con sorted() y .sort()
    print("\n===EXPERIMENTO sorted() ===")
    sorted_lista = sorted(datos)
    print("Lista original:", datos)
    print("Lista ordenada con sorted():", sorted_lista)
    print("id(datos) original:", id(datos))
    print("id(sorted_lista):", id(sorted_lista))
    print("\n===EXPERIMENTO .sort() ===")
    lista_sort = datos[:]  # Copia para no modificar la original
    print("Lista antes de .sort():", lista_sort)
    print("id(lista_sort) antes:", id(lista_sort))
    lista_sort.sort()
    print("Lista después de .sort():", lista_sort)
    print("id(lista_sort) después:", id(lista_sort))

