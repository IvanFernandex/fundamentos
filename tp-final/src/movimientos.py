import validaciones as val
import archivos as arch
import struct

ENTRADAS = "E"
SALIDAS = "S"
APERTURA = "A"

def registrar_movimiento(productos, indice):
    """Descripcion: Registra un movimiento de entrada o salida de mercaderia.
    - Se rechaza si la cantidad excede el stock disponible.
    - Si la salida es valida pero deja el stock por debajo del minimo, el movimiento se registra y se emite una advertencia. El producto quedara visible en el reporte de productos a reponer.
    Pre: productos e indice son los diccionarios cargados en memoria.
    Post: Si el movimiento es valido, el stock queda actualizado en el archivo maestro, en el diccionario de productos, y el movimiento queda en el historial.
    Si es invalido, no se modifica nada y se informa al usuario y ademas si el stock queda por debajo del minimo tambien se informa en el momento de registrar el movimiento."""
    # Prologo
    if not productos:
        print("El inventario esta vacio. No hay movimientos para mostrar.")
    else:
        codigo = val.leer_codigo()
        codigo_str = str(codigo)
    
        if codigo_str not in productos:
            print(f"El producto con codigo {codigo} no existe en el inventario.")
        else:
            tipo = val.ingresar_movimiento()
            cantidad = val.pedir_cantidad()
            fecha = val.pedir_fecha()
    
            # Resolucion
            stock_previo = productos[codigo_str]["stock"]
            stock_minimo = productos[codigo_str]["stock_minimo"]
    
            if tipo == SALIDAS and cantidad > stock_previo: #salida que supera el stock,
                print(f"Error: La cantidad solicitada, excede el stock disponible en este momento.")
            else: 
                if tipo == SALIDAS:
                    nuevo_stock = stock_previo - cantidad
                else:
                    nuevo_stock = stock_previo + cantidad
    
                productos[codigo_str]["stock"] = nuevo_stock
    
                arch.actualizar_producto(codigo, productos[codigo_str], indice)
                arch.guardar_movimiento(codigo, tipo, cantidad, fecha)
    
                # Epilogo
                print(f"Movimiento registrado correctamente.")
    
                if nuevo_stock < stock_minimo:
                    print(f"El producto requiere reposicion, stock debajo del minimo!!.")

def mostrar_movimientos(productos):
    """Descripcion: Muestra el historial de movimientos de un producto dado su codigo,
       recorriendo el archivo de movimientos de forma secuencial.
       Incluye el movimiento de apertura tipo 'A' como primer registro historico.
    Pre: productos es el diccionario cargado en memoria. El archivo MOVIMIENTOS existe.
    Post: Imprime todos los movimientos del producto (apertura, entradas y salidas validas), o informa que no hay registros."""
    # Prologo
    if not productos:
        print("El inventario esta vacio. No hay movimientos para mostrar.")
    else:
        codigo = val.leer_codigo()
        codigo_str = str(codigo)
        if codigo_str not in productos:
            print(f"El producto con codigo {codigo} no existe en el inventario.")
        else:
            # Resolucion: recorremos el archivo filtrando por codigo.
            historial = []
            with open(arch.MOVIMIENTOS, "rb") as archivo:
                registro = archivo.read(arch.TAMANO_MOVIMIENTOS)
                while registro:
                    cod, tipo, cantidad, fecha = struct.unpack(arch.FORMATO_MOVIMIENTOS, registro)
                    cod = cod.decode("utf-8").strip("\x00")
                    if cod == codigo_str:
                        tipo  = tipo.decode("utf-8").strip("\x00")
                        fecha = fecha.decode("utf-8").strip("\x00")
                        historial.append((tipo, cantidad, fecha))
                    registro = archivo.read(arch.TAMANO_MOVIMIENTOS)

            # Epilogo
            descripcion = productos[codigo_str]["descripcion"]
            print(f"\nHistorial de movimientos del producto {descripcion}:")

            if not historial:
                print("No hay movimientos registrados para este producto.")
            else:
                for tipo, cantidad, fecha in historial:
                    print(f"TIPO MOVIMIENTO: {tipo} | CANTIDAD: {cantidad} | FECHA: {fecha}")
#=============================================================================
# PRUEBAS DE MODULO
# Producto de prueba: codigo=1, stock=50, stock_minimo=10
#=============================================================================

if __name__ == "__main__":
    import os
    # Limpiamos archivos para un entorno reproducible.
    for f in (arch.INVENTARIO, arch.MOVIMIENTOS):
        if os.path.exists(f):
            os.remove(f)

    arch.inicializar_archivos()
    productos, indice = arch.cargar_productos()

    # Damos de alta un producto de prueba.
    print("Damos de alta un producto de prueba.")
    print("Ingresa: codigo=1, descripcion='Tornillo', stock=50, stock_minimo=10, precio=1.5, fecha=2024-06-01")
    from productos import alta_producto
    alta_producto(productos, indice)

    print("\n=== Pruebas del modulo movimientos.py ===\n")

    print("Prueba 1 | Entrada valida")
    print("Ingresa: codigo=1, tipo=E, cantidad=20, fecha=2024-06-02")
    print("Esperado: stock 50 -> 70, sin advertencia")
    registrar_movimiento(productos, indice)
    print(f"Stock en memoria: {productos['1']['stock']}\n")

    print("Prueba 2 | Salida que no cruza el minimo")
    print("Ingresa: codigo=1, tipo=S, cantidad=15, fecha=2024-06-03")
    print("Esperado: stock 70 -> 55, sin advertencia (55 > 10)")
    registrar_movimiento(productos, indice)
    print(f"Stock en memoria: {productos['1']['stock']}\n")

    print("Prueba 3 | Salida que deja el stock por debajo del minimo")
    print("Ingresa: codigo=1, tipo=S, cantidad=50, fecha=2024-06-04")
    print("Esperado: stock 55 -> 5, movimiento REGISTRADO con ADVERTENCIA (5 < 10)")
    registrar_movimiento(productos, indice)
    print(f"Stock en memoria: {productos['1']['stock']}\n")

    print("Prueba 4 | Salida rechazada por exceder el stock")
    print("Ingresa: codigo=1, tipo=S, cantidad=999, fecha=2024-06-05")
    print("Esperado: rechazada (999 > 5), stock permanece en 5")
    registrar_movimiento(productos, indice)
    print(f"Stock en memoria: {productos['1']['stock']}\n")

    print("Prueba 5 | Codigo inexistente")
    print("Ingresa: codigo=9999")
    print("Esperado: producto no encontrado")
    registrar_movimiento(productos, indice)
    print()

    print("Prueba 6 | Historial del producto")
    print("Ingresa: codigo=1")
    print("Esperado: Apertura:50, Entrada:20, Salida:15, Salida:50")
    print("La prueba 4 fue rechazada y NO aparece. La prueba 3 SI aparece (advertencia, no rechazo).")
    mostrar_movimientos(productos)

    print("\n=== Fin de las pruebas ===")