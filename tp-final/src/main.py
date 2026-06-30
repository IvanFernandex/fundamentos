import productos as prod
import validaciones as val
import archivos as arch
import movimientos as movi
import os

TITULO = "DOMINIO B - Sistema de gestion de inventario"
SALIDA = 6
OPCION_INVALIDA = 0

def limpiar_pantalla():
    """
    Descripcion: Limpia la consola en Windows, Linux o macOS.
    Pre: -
    Post: Limpia la consola segun el sistema operativo."""
    if os.name == "nt":
        os.system("cls")      # Windows
    else:
        os.system("clear")    # Linux y macOS

def mostrar_menu():
    """
    Descripcion: Imprime el menu de opciones disponibles.
    Pre: -
    Post: Imprime en pantalla el menu de opciones.
    """
    print(f"""
    {TITULO}
    1) Dar alta producto
    2) Registrar movimiento
    3) Listar inventario ordenado
    4) Ver productos a reponer
    5) Consultar historial de movimientos
    6) Salir""")

def main():
    """
    Descripcion: Funcion principal del programa. Inicializa archivos, carga datos
    y ejecuta el ciclo del menu hasta que el usuario elija salir.
    Pre: -
    Post: El programa ejecuta las operaciones seleccionadas por el usuario
    hasta que elige la opcion 6 (Salir).
    """
    arch.inicializar_archivos()
    productos, indices = arch.cargar_productos()

    opcion = OPCION_INVALIDA
    while opcion != SALIDA:
        limpiar_pantalla()
        mostrar_menu()
        opcion = val.ingresar_opcion_valida()
        if opcion == 1:
            prod.alta_producto(productos, indices)
        elif opcion == 2:
            movi.registrar_movimiento(productos, indices)
        elif opcion == 3:
            prod.mostrar_inventario(productos)
        elif opcion == 4:
            prod.mostrar_productos_a_reponer(productos)
        elif opcion == 5:
            movi.mostrar_movimientos(productos)
        if opcion != SALIDA:
            input("Ingrese enter para continuar...")
    print("Saliendo del menú...")

if __name__ == "__main__":
    main()
"""#=============================================================================
# PRUEBAS DE MODULO
# Cubren todos los casos de analisis del diseno.md (casos 1 a 9).
#=============================================================================

if __name__ == "__main__":
    main()
# ELIMINAR COMENTARIOS SI SE DESEA EJECUTAR LAS PRUEBAS DE LOS MODULOS INDIVIDUALMENTE (en lugar de correr main.py).
    # Limpiamos archivos para un entorno reproducible.
    for f in (arch.INVENTARIO, arch.MOVIMIENTOS):
        if os.path.exists(f):
            os.remove(f)

    arch.inicializar_archivos()
    productos, indices = arch.cargar_productos()

    print("=== Pruebas de casos de analisis del diseno.md ===\n")

    # -----------------------------------------------------------------
    # CASO 7 (Extremo): Inventario vacio
    # Se prueba primero porque el inventario empieza vacio.
    # -----------------------------------------------------------------
    print("== CASO 7 | Extremo: Inventario vacio ==")
    print("Esperado: se informa que el inventario esta vacio, sin errores")
    prod.mostrar_inventario(productos)
    print()

    # -----------------------------------------------------------------
    # CASO 1 (Normal): Alta de un producto
    # -----------------------------------------------------------------
    print("== CASO 1 | Normal: Alta de un producto ==")
    print("Ingresa: codigo=1, descripcion='Tornillo', stock=50, stock_minimo=10, precio=1.5, fecha=2024-06-01")
    print("Esperado: producto dado de alta correctamente")
    prod.alta_producto(productos, indices)
    print(f"Productos en memoria: {list(productos.keys())}\n")

    # -----------------------------------------------------------------
    # CASO 9 (Extremo): Alta con codigo ya existente
    # -----------------------------------------------------------------
    print("== CASO 9 | Extremo: Alta con codigo ya existente ==")
    print("Ingresa: codigo=1")
    print("Esperado: se rechaza el alta, codigo ya existe")
    prod.alta_producto(productos, indices)
    print()

    # -----------------------------------------------------------------
    # CASO 2 (Normal): Entrada de mercaderia
    # -----------------------------------------------------------------
    print("== CASO 2 | Normal: Entrada de 10 unidades ==")
    print("Ingresa: codigo=1, tipo=E, cantidad=10, fecha=2024-06-02")
    print("Esperado: stock pasa de 50 a 60, movimiento registrado")
    movi.registrar_movimiento(productos, indices)
    print(f"Stock en memoria: {productos['1']['stock']}\n")

    # -----------------------------------------------------------------
    # CASO 3 (Normal): Salida valida que no cruza el minimo
    # -----------------------------------------------------------------
    print("== CASO 3 | Normal: Salida de 5 unidades (stock=60, minimo=10) ==")
    print("Ingresa: codigo=1, tipo=S, cantidad=5, fecha=2024-06-03")
    print("Esperado: stock pasa de 60 a 55, movimiento registrado, sin advertencia")
    movi.registrar_movimiento(productos, indices)
    print(f"Stock en memoria: {productos['1']['stock']}\n")

    # -----------------------------------------------------------------
    # CASO 4 (Limite): Stock igual al minimo — no aparece en reponer
    # Para esto necesitamos bajar el stock a exactamente 10.
    # -----------------------------------------------------------------
    print("== Preparacion para caso 4: bajamos stock a 10 ==")
    print("Ingresa: codigo=1, tipo=S, cantidad=45, fecha=2024-06-04")
    print("Esperado: stock pasa de 55 a 10")
    movi.registrar_movimiento(productos, indices)
    print(f"Stock en memoria: {productos['1']['stock']}\n")

    print("== CASO 4 | Limite: Stock == minimo, no aparece en reponer ==")
    print("Esperado: producto con codigo 1 NO aparece en reporte (10 no es < 10)")
    prod.mostrar_productos_a_reponer(productos)
    print()

    # -----------------------------------------------------------------
    # CASO 5 (Limite): Stock debajo del minimo — aparece en reponer
    # Bajamos stock de 10 a 9 con una salida de 1.
    # -----------------------------------------------------------------
    print("== Preparacion para caso 5: bajamos stock a 9 ==")
    print("Ingresa: codigo=1, tipo=S, cantidad=1, fecha=2024-06-05")
    print("Esperado: stock pasa de 10 a 9, movimiento registrado con advertencia (9 < 10)")
    movi.registrar_movimiento(productos, indices)
    print(f"Stock en memoria: {productos['1']['stock']}\n")

    print("== CASO 5 | Limite: Stock < minimo, aparece en reponer ==")
    print("Esperado: producto con codigo 1 SI aparece en reporte (9 < 10)")
    prod.mostrar_productos_a_reponer(productos)
    print()

    # -----------------------------------------------------------------
    # CASO 6 (Extremo): Salida mayor al stock disponible
    # -----------------------------------------------------------------
    print("== CASO 6 | Extremo: Salida mayor al stock ==")
    print("Ingresa: codigo=1, tipo=S, cantidad=999, fecha=2024-06-06")
    print("Esperado: operacion rechazada, stock permanece en 9")
    movi.registrar_movimiento(productos, indices)
    print(f"Stock en memoria: {productos['1']['stock']}\n")

    # -----------------------------------------------------------------
    # CASO 8 (Extremo): Consulta de producto inexistente
    # -----------------------------------------------------------------
    print("== CASO 8 | Extremo: Consulta de producto inexistente ==")
    print("Ingresa: codigo=9999")
    print("Esperado: mensaje de producto no encontrado")
    movi.mostrar_movimientos(productos)
    print()

    # -----------------------------------------------------------------
    # VERIFICACION FINAL: Historial del producto 1
    # -----------------------------------------------------------------
    print("== VERIFICACION FINAL: Historial completo del producto 1 ==")
    print("Ingresa: codigo=1")
    print("Esperado: Apertura:50, Entrada:10, Salida:5, Salida:45, Salida:1")
    print("El caso 6 (salida rechazada de 999) NO aparece en el historial.")
    movi.mostrar_movimientos(productos)
    print()

    print("== VERIFICACION FINAL: Inventario ordenado ==")
    prod.mostrar_inventario(productos)

    print("\n=== Fin de las pruebas ===")"""