import validaciones as val
import archivos as arch
import ordenamientos as orde

def alta_producto(productos, indices):
    """Descripcion: Permite al usuario ingresar un nuevo producto al inventario, solicitando su codigo, descripcion, stock actual, stock minimo y precio. Valida que el codigo no exista previamente en el inventario.
    Pre: El diccionario de productos y el diccionario de indices están cargados con los datos actuales del inventario.
    Post: Agrega un nuevo producto al archivo de inventario y actualiza los diccionarios de productos e índices."""
    codigo = val.leer_codigo()
    codigo_str = str(codigo)
    if codigo_str in productos:
        print(f"El código {codigo} ya existe en el inventario. No se puede agregar el producto.")
    else:
        descripcion = val.pedir_descripcion()
        stock_actual = val.pedir_stock()
        stock_minimo = val.pedir_stock_minimo()
        precio = val.pedir_precio()
        fecha = val.pedir_fecha()
        datos = {
            "descripcion": descripcion,
            "stock": stock_actual,
            "stock_minimo": stock_minimo,
            "precio": precio
        }
        # Guardar el nuevo producto en el archivo y actualizamos los diccionarios.
        arch.guardar_producto(codigo, datos, indices)
        arch.guardar_apertura(codigo, stock_actual, fecha)
        productos[codigo_str] = datos
        print(f"Producto con código {codigo} agregado exitosamente al inventario.")

def convertir_dic_lista(diccionario):
    """Descripcion: Convierte un diccionario de productos en una lista temporal de productos, donde cada elemento es un diccionario que contiene, como minimo, la clave 'descripcion'.
    Pre: El diccionario de productos contiene cargado los datos del inventario.
    Post: Devuelve una lista de productos obtenida a partir del diccionario, donde cada elemento es un diccionario que contiene, como minimo, la clave 'descripcion'."""
    lista_productos = []
    for codigo, datos in diccionario.items():
        producto = {
            "codigo": codigo,
            "descripcion": datos["descripcion"],
            "stock": datos["stock"],
            "stock_minimo": datos["stock_minimo"],
            "precio": datos["precio"]
        }
        lista_productos.append(producto)
    return lista_productos

def mostrar_inventario(productos):
    """Descripcion: Muestra el inventario completo de productos, ordenados por su descripcion en orden alfabetico.
    Pre: Productos contiene cargado los datos del inventario.
    Post: Imprime en pantalla la lista de productos ordenada por descripcion, mostrando su codigo, descripcion, stock actual, stock minimo y precio. Si el inventario esta vacio, se informa al usuario."""
    lista_productos = convertir_dic_lista(productos)
    lista_ordenada = orde.ordernar_por_descripcion(lista_productos)
    print("\nInventario completo de productos:")
    if not lista_ordenada:
        print("El inventario esta vacio.")
    else:
        for producto in lista_ordenada:
            print(f"Código: {producto['codigo']}, Descripción: {producto['descripcion']}, Stock Actual: {producto['stock']}, Stock Mínimo: {producto['stock_minimo']}, Precio: {producto['precio']}")

def mostrar_productos_a_reponer(productos):
    """Descripcion: Muestra los productos cuyo stock actual es menor al stock minimo.
    Pre: productos es el diccionario cargado en memoria.
    Post: Imprime la lista de productos a reponer, o informa que no hay ninguno.
    La condicion de reposicion es stock < stock_minimo."""
    # Prologo
    hay_reposicion = False
    # Resolucion
    print("\nProductos a reponer stock debajo del minimo:")
    for codigo, datos in productos.items():  #productos.items() devuelve una tupla (codigo, datos) por cada producto en el diccionario.
        if datos["stock"] < datos["stock_minimo"]:
            print(f"Codigo: {codigo} | Descripcion: {datos['descripcion']} | Stock: {datos['stock']} | Minimo: {datos['stock_minimo']}")
            hay_reposicion = True
    # Epilogo
    if not hay_reposicion:
        print("  No hay productos que reponer.")

#=============================================================================
# PRUEBAS DE MODULO (solo se ejecutan si se corre este archivo directamente, no al importarlo desde main.py)
#=============================================================================

if __name__ == "__main__":
    import os
    import random
    #Limpiamos los archivos luego de hacer las pruebas del modulo
    for archivo in (arch.INVENTARIO, arch.MOVIMIENTOS):
        if os.path.exists(archivo):
            os.remove(archivo)
    arch.inicializar_archivos()
 
    print("=== Pruebas del modulo productos ===\n")
    productos = {}
    indices   = {}
 
    print("=== PRUEBA 1: Alta de producto ===")
    print("Ingresa: codigo=1, descripcion='Tornillo', stock=50, stock_minimo=10, precio=1.5, fecha=2024-06-01")
    alta_producto(productos, indices)
    print(f"Productos en memoria: {productos}\n")
 
    print("=== PRUEBA 2: Mostrar inventario ===")
    mostrar_inventario(productos)
    print()
 
    print("=== PRUEBA 3: Alta con stock igual al minimo ===")
    print("Ingresa: codigo=2, descripcion='Arandela', stock=10, stock_minimo=10, precio=0.5, fecha=2024-06-01")
    alta_producto(productos, indices)
    mostrar_inventario(productos)
    print()
 
    print("=== PRUEBA 4: Alta con stock bajo el minimo ===")
    print("Ingresa: codigo=3, descripcion='Clavo', stock=5, stock_minimo=20, precio=0.2, fecha=2024-06-01")
    alta_producto(productos, indices)
    mostrar_inventario(productos)
    print()
 
    print("=== PRUEBA 5: Productos a reponer ===")
    print("Resultado esperado: solo Clavo.")
    mostrar_productos_a_reponer(productos)
    print()
 
    print("=== PRUEBA 6: Alta con codigo existente ===")
    print("Ingresa: codigo=1")
    alta_producto(productos, indices)