"""Enunciado
Implementar tres funciones de ordenamiento in-place en Python:
ordenamiento_seleccion(datos), ordenamiento_insercion(datos) y
ordenamiento_burbuja(datos). Cada función recibe una lista mutable de enteros y la ordena in- place en forma no decreciente. El ordenamiento por burbuja debe incluir la optimización de parada temprana (bandera de intercambio).
A continuación, escribir un programa que:

(a) Genere una lista de n = 20 enteros pseudoaleatorios en el rango [1, 100] con random.seed(42). Mostrar la lista original.

(b) Para cada algoritmo, crear una copia de la lista original (datos.copy()), ordenarla e imprimir el resultado. Verificar que las tres funciones producen la misma lista ordenada.

(c) Agregar un contador de comparaciones y un contador de intercambios (o desplazamientos, en el caso de inserción) a cada función. Informar ambos contadores para cada algoritmo y comparar con las predicciones teóricas."""

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
    
def ordenamiento_insercion(datos, contar=False):
    '''Ordena la lista datos in-place usando inserción directa.
    
    Precondición: datos es una lista de elementos comparables.
    Poscondición: datos queda ordenada en forma no decreciente.
    Complejidad: O(n²) peor caso, O(n) mejor caso (ya ordenada).
    Estabilidad: estable.
    '''
    cant_comparaciones = 0
    cant_desplazamientos = 0

    n = len(datos)
    for i in range(1, n):
        clave = datos[i]
        j = i - 1
        while j >= 0 and datos[j] > clave:
            cant_comparaciones += 1
            datos[j + 1] = datos[j]  # desplazar a la derecha
            cant_desplazamientos += 1
            j -= 1
        # cuenta la comparación que hace salir del while (si no fue por j < 0)
        if j >= 0:
            cant_comparaciones += 1
        datos[j + 1] = clave  # insertar en el hueco
    return (datos, cant_comparaciones, cant_desplazamientos) if contar else datos

def ordenamiento_burbuja(datos, contar=False):
    '''Ordena la lista datos in-place usando burbuja con parada temprana.
    
    Precondición: datos es una lista de elementos comparables.
    Poscondición: datos queda ordenada en forma no decreciente.
    Complejidad: O(n²) peor caso, O(n) mejor caso (con optimización).
    Estabilidad: estable.
    '''
    largo_secuencia = len(datos)
    i = 0
    hubo_intercambio = True
    cant_comparaciones = 0
    cant_intercambios = 0
    while i < largo_secuencia - 1 and hubo_intercambio:
        hubo_intercambio = False
        cant_comparaciones += 1
        for j in range(largo_secuencia - 1 - i):
            if datos[j] > datos[j + 1]:
                datos[j], datos[j + 1] = datos[j + 1], datos[j]
                hubo_intercambio = True
                cant_intercambios += 1
        i += 1
    # Inspección post-bucle:
    # Si salió por hubo_intercambio == False: la pasada no hizo swaps → ya está ordenado
    # Si salió por i == n-1: se completaron todas las pasadas → ordenado por correctitud
    return (datos, cant_comparaciones, cant_intercambios) if contar else datos