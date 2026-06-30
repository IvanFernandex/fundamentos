def ordernar_por_descripcion(productos):
    """Descripcion: Ordena los productos por su descripcion en orden alfabetico aplicando el algoritmo de ordenamiento por insercion.
    Pre: Productos es una lista temporal de productos obtenida a partir de un diccionario. Cada elemento es un diccionario que contiene, como minimo, la clave 'descripcion'.
    Post: Devuelve la lista de productos ordenada alfabeticamente por descripcion. La comparacion es case-insensitive.
    """
    for i in range(1, len(productos)):
        actual = productos[i]
        j = i - 1
        while j >= 0 and productos[j]['descripcion'].lower() > actual['descripcion'].lower():
            productos[j + 1] = productos[j]
            j -= 1
        productos[j + 1] = actual
    return productos

#=============================================================================
# PRUEBAS DE MODULO (solo se ejecutan si se corre este archivo directamente, no al importarlo desde main.py)
#=============================================================================

if __name__ == "__main__":
    print("=== Pruebas del módulo ordenamientos ===\n")

    print("=== PRUEBA 1: Lista desordenada ===")
    productos = [
        {"descripcion": "Mouse"},
        {"descripcion": "Auriculares"},
        {"descripcion": "Teclado"}
    ]

    print("Antes:\n",productos)
    ordernar_por_descripcion(productos)

    print("Después:\n",productos)
    print()

    print("=== PRUEBA 2: Lista ya ordenada ===")
    productos = [
        {"descripcion": "Auriculares"},
        {"descripcion": "Mouse"},
        {"descripcion": "Teclado"}
    ]

    print("Antes:\n",productos)
    ordernar_por_descripcion(productos)

    print("Después:\n",productos)
    print()
    print("=== PRUEBA 3: Un único producto ===")
    productos = [
        {"descripcion": "Teclado"}
    ]

    print("Antes:\n",productos)
    ordernar_por_descripcion(productos)

    print("Después:\n",productos)
    print()

    print("=== PRUEBA 4: Lista vacía ===")
    productos = []

    print("Antes:\n",productos)
    ordernar_por_descripcion(productos)

    print("Después:\n",productos)
    print()

    print("=== PRUEBA 5: Productos con más datos ===")
    productos = [
        {"codigo": "3", "descripcion": "Teclado", "stock": 10},
        {"codigo": "1", "descripcion": "Auriculares", "stock": 5},
        {"codigo": "2", "descripcion": "Mouse", "stock": 8}
    ]

    print("Antes:\n",productos)
    ordernar_por_descripcion(productos)
    print("Después:\n",productos)