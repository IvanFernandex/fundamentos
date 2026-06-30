import datetime
MOVIMIENTOS = ["E", "S"]

def ingresar_opcion_valida():
    """Descripcion: Pide al usuario que ingrese una opcion valida entre 1 y 6.
    Pre: -
    Post: Devuelve la opcion ingresada por el usuario."""
    opcion = input("Ingrese una opcion entre 1 y 6 : ")
    valido = False

    while not valido:
        if opcion.isdigit():
            opcion = int(opcion)
            if 0 < opcion <= 6:
                valido = True
            else:
                opcion = input("Opcion invalida. Ingrese una opcion entre 1 y 6 : ")
        else:
            opcion = input("Opcion invalida, debe ser un numero. Ingrese una opcion entre 1 y 6 : ")
    return opcion

def leer_codigo():
    """Descripcion: Pide al usuario que ingrese un codigo valido, solo numeros enteros positivos.
    Pre: -
    Post: Devuelve el codigo ingresado por el usuario."""
    codigo = input("Ingrese el codigo del producto : ")
    valido = False

    while not valido:
        if codigo.isdigit():
            valido = True
            codigo = int(codigo)
        else:
            codigo = input("Opcion invalida, solo se admiten numeros. Ingrese el codigo del producto : ")
    return codigo


def pedir_stock():
    """Descripcion: Pide al usuario que ingrese un stock valido, solo numeros enteros positivos.
    Pre: -
    Post: Devuelve el stock ingresado por el usuario."""
    stock = input("Ingrese el stock del producto : ")
    valido = False
    while not valido:
        if stock.isdigit():
            stock = int(stock)
            if stock > 0:
                valido = True
            else:
                stock = input("Stock invalido. Ingrese el stock del producto : ")
        else:
            stock = input("Stock invalido, solo se admiten numeros. Ingrese el stock del producto : ")
    return stock

def pedir_stock_minimo():
    """Descripcion: Pide al usuario que ingrese un stock minimo valido, solo numeros enteros positivos.
    Pre: -
    Post: Devuelve el stock minimo ingresado por el usuario."""
    stock_minimo = input("Ingrese el stock minimo del producto : ")
    valido = False
    while not valido:
        if stock_minimo.isdigit():
            stock_minimo = int(stock_minimo)
            if stock_minimo > 0:
                valido = True
            else:
                stock_minimo = input("Stock minimo invalido. Ingrese el stock minimo del producto : ")
        else:
            stock_minimo = input("Stock minimo invalido, solo se admiten numeros. Ingrese el stock minimo del producto : ")
    return stock_minimo

def pedir_cantidad():
    """Descripcion: Pide al usuario que ingrese una cantidad valida, solo numeros enteros positivos.
    Pre: -
    Post: Devuelve la cantidad ingresada por el usuario."""
    cantidad = input("Ingrese la cantidad: ")
    valido = False
    while not valido:
        if cantidad.isdigit():
            cantidad = int(cantidad)
            if cantidad > 0:
                valido = True
            else:
                cantidad = input("Error, debe ser mayor a 0. Ingrese la cantidad: ")
        else:
            cantidad = input("Error, debe ser solo numeros. Ingrese la cantidad: ")
    return cantidad

def pedir_descripcion():
    """Descripcion: Pide al usuario que ingrese una descripcion del producto valida.
    Pre: -
    Post: Devuelve la descripcion ingresada por el usuario."""
    descripcion = input("Ingrese la descripcion del producto : ")
    valido = False
    while not valido:
        if descripcion == "":
            descripcion = input("Error, descripcion vacía. Ingrese la descripcion del producto : ")
        else:
            valido = True
    descripcion = descripcion.strip().capitalize() # Elimina espacios en blanco al inicio y al final de la descripcion y pone en mayuscula la primera letra.
    return descripcion

def pedir_precio():
    """Descripcion: Pide al usuario que ingrese un precio valido (flotantes).
    Pre: -
    Post: Devuelve el precio ingresado por el usuario."""
    precio = input("Ingrese el precio del producto : ")
    valido = False
    while not valido:
        try:
            precio = float(precio)
            if precio > 0:
                valido = True
            else:
                precio = input("Error, el precio debe ser mayor a cero. Ingrese el precio del producto : ")
        except ValueError:
            precio = input("Error, debe ser un numero. Ingrese el precio del producto : ")
    return precio

def ingresar_movimiento():
    """Descripcion: Pide al usuario que ingrese un tipo de movimiento valido E/S, puede ingresarse en minuscula.
    Pre: -
    Post: Devuelve el tipo de movimiento ingresado por el usuario."""
    movimiento = input("Ingrese el tipo de movimiento: ")
    valido = False
    while not valido:
        if movimiento.upper() not in MOVIMIENTOS:
            movimiento = input("Movimiento invalido, debe ser E o S. Ingrese el tipo de movimiento: ")
        else:
            valido = True

    return movimiento.upper()


def pedir_fecha():
    """Pide al usuario que ingrese una fecha en formato YYYY-MM-DD y valida su formato.
    Pre: -
    Post: Devuelve la fecha ingresada por el usuario en formato YYYY-MM-DD.
    """
    fecha = input("Ingrese la fecha del movimiento (YYYY-MM-DD): ")
    valido = False
    while not valido:
        try:
            datetime.datetime.strptime(fecha,"%Y-%m-%d").date()  # Verifica que la fecha ingresada tenga el formato correcto sea una fecha válida.
            valido = True
            return fecha
        except ValueError:
            fecha = input("Formato invalido. Ingrese la fecha del movimiento (YYYY-MM-DD): ")
    return fecha

# =============================================================================
# PRUEBAS DE MODULO (solo se ejecutan si se corre este archivo directamente, no al importarlo desde main.py)
# =============================================================================

if __name__ == "__main__":
    print("=== Pruebas del módulo validaciones.py ===")
    # -------------------------------------------------------------------------
    # ingresar_opcion_valida
    # -------------------------------------------------------------------------
    print("==Pruebas para opciones validas entre 1 y 6===\n")
    print("Ingresa 'abc' y luego '3'")
    resultado = ingresar_opcion_valida()
    print(f"Resultado: {resultado}\n")  
    print("Ingresa '0' y luego '7' y luego '6'")
    resultado = ingresar_opcion_valida()
    print(f"Resultado: {resultado}\n")  
    # -------------------------------------------------------------------------
    # leer_codigo
    # -------------------------------------------------------------------------
    print("==Pruebas para codigos validos===\n")
    print("Ingresa 'abc' y luego '123'")
    resultado = leer_codigo()
    print(f"Resultado: {resultado}\n")  
    print("Ingresa '42'")
    resultado = leer_codigo()
    print(f"Resultado: {resultado}\n")  
    # -------------------------------------------------------------------------
    # pedir_stock
    # -------------------------------------------------------------------------
    print("==Pruebas para stock===\n")
    print("Ingresa 'abc' y luego '0'")
    resultado = pedir_stock()
    print(f"Resultado: {resultado}\n")  
    print("Ingresa '50'")
    resultado = pedir_stock()
    print(f"Resultado: {resultado}\n")  
    # -------------------------------------------------------------------------
    # pedir_cantidad
    # -------------------------------------------------------------------------
    print("==Pruebas para cantidad===\n")
    print("Ingresa '0' y luego '10'")
    resultado = pedir_cantidad()
    print(f"Resultado: {resultado}\n")  
    print("Ingresa 'abc' y luego '5'")
    resultado = pedir_cantidad()
    print(f"Resultado: {resultado}\n")  
    # -------------------------------------------------------------------------
    # pedir_descripcion
    # -------------------------------------------------------------------------
    print("==Pruebas para descripcion===\n")
    print("Ingresa '' (vacío) y luego 'Tornillo M6' M6'")
    resultado = pedir_descripcion()
    print(f"Resultado: '{resultado}'\n")    
    print("Ingresa 'Clavo''")
    resultado = pedir_descripcion()
    print(f"Resultado: '{resultado}'\n")    
    # -------------------------------------------------------------------------
    # ingresar_movimiento
    # -------------------------------------------------------------------------
    print("==Pruebas para movimiento (E/S)===\n")
    print("Ingresa 'X' y luego 'e'' (en mayúscula)")
    resultado = ingresar_movimiento()
    print(f"Resultado: '{resultado}'\n")    
    print("Ingresa 's'' (en mayúscula)")
    resultado = ingresar_movimiento()
    print(f"Resultado: '{resultado}'\n")    
    # -------------------------------------------------------------------------
    # pedir_fecha
    # -------------------------------------------------------------------------
    print("==Pruebas para fecha (formato YYYY-MM-DD)===\n")
    print("Ingresa '01-13-2024' y luego '2024-06-01'-06-01'")
    resultado = pedir_fecha()
    print(f"Resultado: '{resultado}'\n")    
    print("Ingresa '2024-02-30' y luego '2024-02-28'-02-28'")
    resultado = pedir_fecha()
    print(f"Resultado: '{resultado}'\n")    
    print("=== Fin de las pruebas ===") 