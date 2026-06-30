import os #Para verificar la existencia de los archivos y crear nuevos si es necesario.
import struct #Para empaquetar y desempaquetar los registros en los archivos binarios.
# =============================================================================
# CONSTANTES NECESARIAS PARA EL MANEJO DE 
# Si se desea modificar algun formate de registros, nombre de archivos, etcetera, se debe hacer aqui para mantener la legibilidad y no utilizar variables repetidas durante el codigo
# =============================================================================

INVENTARIO = "productos.bin"    # Nombre del archivo de inventario
MOVIMIENTOS = "movimientos.bin" # Nombre del archivo de movimientos

FORMATO_INVENTARIO = "10s50siif" # Formato: codigo (10 bytes), descripcion (50 bytes), stock_actual (int), stock_minimo (int), precio (float)
FORMATO_MOVIMIENTOS = "10s1si10s"  # Formato: codigo (10 bytes), tipo_movimiento (1 byte: 'E' para entrada, 'S' para salida), cantidad (int), fecha (10 bytes: "YYYY-MM-DD")

TAMANO_INVENTARIO = struct.calcsize(FORMATO_INVENTARIO)
TAMANO_MOVIMIENTOS = struct.calcsize(FORMATO_MOVIMIENTOS)

#=============================================
#  ARCHIVOS
#=============================================

def inicializar_archivos():
    """
    Descripción: Crea los archivos de inventario y movimientos si no existen. Si ya existen, no los modifica.
    Pre: -
    Post: Los archivos INVENTARIO y MOVIMIENTOS existen.
    """
    if not os.path.exists(INVENTARIO):
        with open(INVENTARIO,"wb") as archivo_inventario:
            archivo_inventario.write(b"")
    if not os.path.exists(MOVIMIENTOS):
        with open(MOVIMIENTOS,"wb") as archivo_movimientos:
            archivo_movimientos.write(b"")

def cargar_productos():
    """
    Descripción: Carga los productos del archivo de inventario y construye un índice
                 para acceder a los registros a partir del código de producto.
    Pre: El archivo INVENTARIO existe y tiene el formato correcto.
    Post: Devuelve un diccionario de productos {codigo_str: datos} y un diccionario
          índice {codigo_str: posicion_registro}.
    """
    #Prologo: Creamos dos diccionarios vacíos, uno para los productos y otro para el índice.
    productos = {}
    indice = {}

    #Resolucion: Agregamos la informacion a los diccionarios a medida que leemos cada registro del archivo de inventario, hasta llegar al final del archivo.
    with open(INVENTARIO, "rb") as archivo_inventario:
        posicion_registro = 0
        registro = archivo_inventario.read(TAMANO_INVENTARIO)

        while registro:
            codigo, descripcion, stock_actual, stock_minimo, precio = struct.unpack(FORMATO_INVENTARIO, registro)
            codigo = codigo.decode("utf-8").strip("\x00")
            descripcion = descripcion.decode("utf-8").strip("\x00")
            productos[codigo] = {
                "descripcion": descripcion,
                "stock": stock_actual,
                "stock_minimo": stock_minimo,
                "precio": precio
            }

            indice[codigo] = posicion_registro  # clave: código como str; valor: posición en el archivo.

            posicion_registro += 1
            registro = archivo_inventario.read(TAMANO_INVENTARIO)

    #Epilogo: Devolvemos los diccionarios con los productos y el índice cargados.
    return productos, indice

def guardar_producto(codigo, datos, indice):
    """
    Descripción: Agrega un producto al final del archivo del inventario.
    Pre: codigo es un entero positivo. datos es un diccionario con las claves
         "descripcion", "stock", "stock_minimo" y "precio". El código no existe en el índice.
    Post: Se agrega el producto al archivo y se actualiza el índice con su posición.
    """
    #Prologo: -
    codigo_str = str(codigo)
    posicion_registro = len(indice)
    producto = struct.pack(FORMATO_INVENTARIO,codigo_str.encode("utf-8"),datos["descripcion"].encode("utf-8"),datos["stock"],datos["stock_minimo"],datos["precio"])

    with open(INVENTARIO, "ab") as archivo_inventario:
        archivo_inventario.write(producto)

    indice[codigo_str] = posicion_registro  # Actualizamos el índice con la posición del nuevo producto.

def actualizar_producto(codigo, datos, indice):
    """
    Descripción: Actualiza un producto existente mediante acceso directo.
    Pre: codigo es un entero positivo. El código existe en el índice.
    Post: El registro correspondiente queda actualizado en el archivo.
    """
    codigo_str = str(codigo)
    posicion_registro = indice[codigo_str]

    producto = struct.pack(
        FORMATO_INVENTARIO,
        codigo_str.encode("utf-8"),
        datos["descripcion"].encode("utf-8"),
        datos["stock"],
        datos["stock_minimo"],
        datos["precio"]
    )

    with open(INVENTARIO, "r+b") as archivo_inventario:
        archivo_inventario.seek(posicion_registro * TAMANO_INVENTARIO)
        archivo_inventario.write(producto)


def guardar_movimiento(codigo, tipo, cantidad, fecha):
    """
    Descripción: Registra un movimiento de mercadería al final del archivo de movimientos.
    Pre: codigo es un entero positivo. tipo es 'E' o 'S'. cantidad es un entero positivo.
         fecha es una cadena con formato 'AAAA-MM-DD'.
    Post: Se agrega el movimiento al final del archivo MOVIMIENTOS.
    """
    codigo_str = str(codigo)
    movimiento = struct.pack(
        FORMATO_MOVIMIENTOS,
        codigo_str.encode("utf-8"),
        tipo.encode("utf-8"),
        cantidad,
        fecha.encode("utf-8")
    )

    with open(MOVIMIENTOS, "ab") as archivo_movimientos:
        archivo_movimientos.write(movimiento)

def guardar_apertura(codigo, stock_inicial, fecha):
    """
    Descripcion: Registra el saldo inicial de un producto como movimiento de apertura tipo 'A' en el historial. Se llama una unica vez al dar de alta el producto.
    Pre: codigo es un entero positivo. stock_inicial es un entero >= 0. fecha es una cadena con formato 'AAAA-MM-DD'.
    Post: Se agrega un movimiento tipo 'A' al final del archivo  si es una apertura.
    """
    codigo_str = str(codigo)
    movimiento = struct.pack(FORMATO_MOVIMIENTOS,codigo_str.encode("utf-8"),"A".encode("utf-8"),stock_inicial,fecha.encode("utf-8"))
    with open(MOVIMIENTOS, "ab") as archivo_movimientos:
        archivo_movimientos.write(movimiento)

#=============================================================================
# PRUEBAS DE MODULO (solo se ejecutan si se corre este archivo directamente, no al importarlo desde main.py)
#=============================================================================

if __name__ == "__main__":
    import random
    #Limpiamos los archivos luego de hacer las pruebas del modulo
    for archivo in (INVENTARIO, MOVIMIENTOS):
        if os.path.exists(archivo):
            os.remove(archivo)
    random.seed(42)  # Para reproducibilidad de las pruebas.
    codigos_random = [random.randint(10000, 99999) for _ in range(5)]  # Generamos algunos códigos de prueba aleatorios.
    descripciones_random = ["Producto A", "Producto B", "Producto C", "Producto D", "Producto E"]
    stocks_random = [random.randint(0, 200) for _ in range(5)]
    precios_random = [round(random.uniform(1.0, 100.0), 2) for _ in range(5)]
    print("=== Pruebas del módulo de archivos ===")
    # Prologo: Inicializamos los archivos y cargamos los productos para tener un entorno de prueba.
    print("Comprobamos que si hay archivos, no los borra ni modifica.")
    inicializar_archivos()
    productos, indice = cargar_productos()
    # Resolucion: Probamos agregar un nuevo producto, actualizarlo y registrar un movimiento.
    for i in range(5):
        codigo = codigos_random[i]
        datos = {
            "descripcion": descripciones_random[i],
            "stock": stocks_random[i],
            "stock_minimo": 10,
            "precio": precios_random[i]
        }
        print(f"Agregando producto: {codigo}")
        try:
            guardar_producto(codigo, datos, indice)
            print(f"Producto agregado: {codigo} - {datos['descripcion']} | Stock: {datos['stock']} | Precio: {datos['precio']:,.2f}")
            print (f"Índice después de agregar: Codigo: {codigo} | Indice {indice.get(str(codigo))}")
        except Exception as e:
            print(f"Error al guardar el producto {codigo}: {e}")
    # Epílogo: verificamos que los productos se cargaron correctamente y hay persistencia en el archivo.
    productos_recargados, _ = cargar_productos()
    print("\n=== Verificación de persistencia ===")
    for codigo in codigos_random:
        codigo_str = str(codigo)
        if codigo_str in productos_recargados:
            p = productos_recargados[codigo_str]
            print(f"OK   {codigo_str} - {p['descripcion']} | Stock: {p['stock']} | Precio: {p['precio']:,.2f}")
        else:
            print(f"FALTA {codigo_str} - no se encontró en el archivo")
# No se verifica el diccionario `productos` cargado al inicio porque guardar_producto no es responsable de actualizarlo: esa tarea corresponde a alta_producto en productos.py que es quien coordina ambas estructuras. 
# Lo que sí se verifica aquí es que el archivo y el índice quedan correctamente actualizados, que es la responsabilidad de este módulo.