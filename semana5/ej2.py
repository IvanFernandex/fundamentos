import random
"""Problema 2: Búsqueda binaria recursiva
Enunciado
Implementar una versión recursiva de la búsqueda binaria: busqueda_binaria_rec(datos,
clave, izq, der). La función recibe además los límites de la región de búsqueda y se invoca
recursivamente reduciendo la región a la mitad.
Escribir un programa que:
(a) Reutilice la lista ordenada del Problema 1 (misma semilla, mismo n).
(b) Busque las mismas 10 claves del Problema 1 con la versión recursiva y verifique que los
resultados son idénticos a los de la versión iterativa.
(c) Para tres valores de n (100, 1000, 10000), medir la profundidad máxima de recursión
alcanzada (usar un parámetro nivel que se incrementa en cada llamada) y compararla con
⌈log₂(n)⌉.
Orientaciones para la resolución
Diseño: Dos casos base: (1) izq > der → retornar -1; (2) datos[medio] == clave → retornar
medio. Dos casos recursivos: buscar en la mitad izquierda o derecha. La invocación inicial es
busqueda_binaria_rec(datos, clave, 0, len(datos) - 1).
Evaluación: Para n = 1000, la profundidad máxima debe ser ≤ 10 (ya que ⌈log₂(1000)⌉ = 10). Si
la profundidad es mayor, hay un error en la reducción de la región.
Conexión con la Semana 4 — Cada llamada recursiva apila un nuevo frame en la pila de
ejecución con sus propias copias de izq, der y medio. La profundidad máxima O(log n) implica
un uso de memoria proporcional a log₂(n) frames, lo que para n = 1.000.000 son solo ~20 frames:
un uso muy modesto de la pila."""

def busqueda_binaria_rec(datos, clave, izq, der, nivel=1):
    if izq > der:
        return -1, nivel

    medio = (izq + der) // 2

    if datos[medio] == clave:
        return medio, nivel

    elif clave < datos[medio]:
        return busqueda_binaria_rec(datos, clave, izq, medio - 1, nivel + 1)
    else:
        return busqueda_binaria_rec(datos, clave, medio + 1, der, nivel + 1)

def generar_listas():
    random.seed(42)
    n = 1000
    datos = sorted(random.sample(range(-n, 2*n), n))
    return datos

def generar_claves(datos):
    claves_presentes = random.sample(datos, 5)
    claves_ausentes = [-i for i in range(1, 6)]
    claves_totales = claves_presentes + claves_ausentes
    return claves_totales 

def probar_profundidad(n):
    random.seed(42)
    datos = sorted(random.sample(range(1, 10*n), n))
    claves = random.sample(datos, 5)
    max_profundidad = 0
    for clave in claves:
        _, profundidad = busqueda_binaria_rec(
            datos, clave, 0, len(datos) - 1
        )
        max_profundidad = max(max_profundidad, profundidad)
    print(f"n = {n} → profundidad máxima = {max_profundidad}")

def main():
    #Aca tengo q llamar a las funciones para probar la búsqueda binaria recursiva y medir la profundidad máxima.
    datos = generar_listas()
    claves = generar_claves(datos)
main()
        