"""Escribir un programa modular que investigue cuánta memoria ocupan los distintos tipos de
objetos en Python:
(a) Medir y comparar el tamaño en bytes de: un int pequeño (42), un int grande (2**100),
un float (3.14), un bool (True), una cadena corta ("hola") y una cadena larga ("a" * 1000).
(b) Medir el tamaño de listas de enteros para n ∈ {0, 1, 10, 100, 1000}. Calcular el
overhead de la estructura lista y el tamaño total incluyendo los objetos referenciados.
Presentar en tabla formateada.
(c) Comparar el tamaño de una list vs. una tuple con los mismos 100 elementos.
¿Cuánto ahorra la tupla? ¿Por qué?
(d) Medir el efecto de la sobreasignación de CPython: comparar el tamaño de una lista
creada con [1, 2, 3] + [4] vs. una lista a la que se le hizo append(4). Explicar la
diferencia."""
import sys
#a)
def medir_tamanio(objeto, nombre):
    print(f"{nombre:<15} | tipo: {type(objeto).__name__:<15} | tamaño: {sys.getsizeof(objeto)} bytes")  
#b)
def medir_tamano_listas():
    """Descripcion: Mide el tamaño de listas de enteros para n [0, 1, 10, 100, 1000] y calcula el overhead y el tamaño total.
    Pre: -
    Post: Imprime una tabla formateada con el tamaño de las listas, el overhead y el tamaño total.
    """
    print("=== Medición de tamaño de listas de enteros ===")
    for n in [0, 1, 10, 100, 1000]:
        lista = list(range(n))
        tamanio_lista = sys.getsizeof(lista)
        tamanio_elementos = sum(sys.getsizeof(e) for e in lista)
        tamanio_total = tamanio_lista + tamanio_elementos
        print(f"n={n:<5} | Tamaño lista = {tamanio_lista:<5} | elementos = {tamanio_elementos:<5} | Tamaño total = {tamanio_total}")
#c)
def comparar_list_tuple():
    print("=== Lista vs Tupla ===")
    datos = list(range(100))
    tupla = tuple(range(100))
    tam_lista = sys.getsizeof(datos)
    tam_tupla = sys.getsizeof(tupla)
    print("Lista:", tam_lista, "bytes")
    print("Tupla:", tam_tupla, "bytes")

#d)
def comparar_sobreasignacion():
    print("=== Sobreasignación ===")

    lista1 = [1, 2, 3] + [4]
    lista2 = [1, 2, 3]
    lista2.append(4)

    print("lista1 (+):", sys.getsizeof(lista1), "bytes")
    print("lista2 (append):", sys.getsizeof(lista2), "bytes")

def main():
    medir_tamanio(42, "int pequeño")
    medir_tamanio(2**100, "int grande")
    medir_tamanio(3.14, "float")
    medir_tamanio(True, "bool")
    medir_tamanio("hola", "cadena corta")
    medir_tamanio("a" * 1000, "cadena larga")
    medir_tamano_listas()
    comparar_list_tuple()
    comparar_sobreasignacion()
main()