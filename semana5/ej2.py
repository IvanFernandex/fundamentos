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

def busqueda_binaria_rec(datos, clave, izq, der, nivel=1):
    """SECCIÓN DECLARATIVA
    Descripcion: Buscar la posición de 'clave' en la secuencia ordenada 'datos' usando búsqueda binaria recursiva.
    Precondición: datos está ordenado de menor a mayor, izq y der son índices válidos dentro de datos.
    Postcondición: Retorna el índice i tal que datos[i] == clave, o -1 si clave no pertenece a datos. Además, retorna el nivel de profundidad alcanzado."""
    #Caso base: region vacia
    #SECCION ALGORÍTMICA
    #1) Prologo: verificar caso bases
    if izq > der:
        return -1, nivel

    medio = (izq + der) // 2
    #Caso base: encontrado
    if datos[medio] == clave:
        return medio, nivel
    #2) Epilogo y desarrollo: aumentar nivel y hacer llamada recursiva para mitad izquierda o derecha
    #Aumento de niveles en cada llamada 
    #Caso recursivo: buscar en la mitad izquierda o derecha
    elif clave < datos[medio]:
        return busqueda_binaria_rec(datos, clave, izq, medio - 1, nivel + 1)
    else:
        return busqueda_binaria_rec(datos, clave, medio + 1, der, nivel + 1)
#a) Reutilizar la lista ordenada del Problema 1 (misma semilla, mismo n).
def generar_listas():
    """
    SECCION DECLARATIVA
    Descripción: Genera una lista ordenada de n enteros distintos.
    Precondición: n es un entero positivo.
    Postcondición: Retorna una lista ordenada de n enteros distintos."""
    #SECCION ALGORÍTMICA
    #Prólogo: fijar la semilla para reproducibilidad
    random.seed(42)
    n = 1000
    #Resolución: generar n enteros distintos y ordenarlos
    datos = random.sample(range(1, 10 * n), n)
    #Epílogo: retornar la lista ordenada
    return sorted(datos)
#b) Buscar las mismas 10 claves del Problema 1 con la versión recursiva y verificar que los resultados son idénticos a los de la versión iterativa.
def generar_claves(datos):
    """SECCION DECLARATIVA
    Descripción: Genera una lista de claves para buscar, incluyendo algunas presentes en 'datos' y otras ausentes.
    Precondición: datos es una secuencia de enteros.
    Postcondición: Retorna una lista de claves, con 5 presentes en 'datos' y 5 enteros negativos ausentes."""
    #SECCION ALGORÍTMICA
    #Prólogo: generar claves presentes y ausentes
    claves_presentes = random.sample(datos, 5)
    claves_ausentes = [-i for i in range(1, 6)]
    #Epílogo: combinar y retornar las claves
    claves_totales = claves_presentes + claves_ausentes
    return claves_totales 

def probar_profundidad(n):
    """Sección Declarativa
    Descripción: Para un tamaño n dado, genera una lista ordenada de n enteros
    Precondición: n es un entero positivo.
    Postcondición: Retorna la profundidad máxima alcanzada por n llamadas recursivas de búsqueda binaria para claves presentes en la lista."""
    random.seed(42)
    #genero datos para ciertos n y poder comprobar la profundidad máxima de recursión
    datos = sorted(random.sample(range(1, 10*n), n))
    claves = random.sample(datos, 5)
    max_profundidad = 0
    for clave in claves:
        busqueda, profundidad = busqueda_binaria_rec(datos, clave, 0, len(datos) - 1)
        if profundidad > max_profundidad:
            max_profundidad = profundidad
    return max_profundidad

def main():

    # ==========================================
    # SECCIÓN ALGORÍTMICA
    # ==========================================
    #Aca tengo q llamar a las funciones para probar la búsqueda binaria recursiva y medir la profundidad máxima.
    #1) Prólogo: generar datos y claves
    datos = generar_listas()
    claves = generar_claves(datos)
    for clave in claves:
        #2) Desarrollo: buscar cada clave con ambas funciones y comparar resultados
        busqueda_rec, profundidad = busqueda_binaria_rec(datos, clave, 0, len(datos) - 1)
        busqueda_bin = busqueda_binaria(datos, clave)
        print("-"*30)
        print(f"Clave: {clave}\n Índice-Rec: → {busqueda_rec}, Profundidad: {profundidad}\n Índice-Iter: → {busqueda_bin}")
        print("-"*30)

        if busqueda_rec != busqueda_bin:
            print("Error: los resultados no coinciden.")
    #3) Epílogo: Comprobar profundidad máxima para n = 100, 1000, 10000
    #Comprobar profundidad máxima para n = 100, 1000, 10000
    for n in [100,1000,10000]:
        profundidad = probar_profundidad(n)
        print(f"Profundidad máxima para n={n}: {profundidad}")
main()
        