import random
from datetime import datetime, timedelta
"""Código de producto: algunos productos se venden más que otros. Definir 10 productos «estrella» con
peso 5 y 40 productos regulares con peso 1, y usar random.choices con esos pesos"""

def generar_catalogo():
    """Descripcion: Genera un catálogo de productos con códigos y precios aleatorios.
    Pre: -
    Post: Devuelve una lista de tuplas (codigo, precio) con 50 productos, donde el código es una cadena en formato 'PXXXX' y el precio es un número decimal entre 50 y 5000."""
    random.seed(42) # para reproducibilidad
    catalogo = []
    for i in range(1, 51):
        codigo = f'P{i:04d}'
        precio = round(random.uniform(50, 5000), 2)
        catalogo.append((codigo, precio))
    return catalogo

def buscar_producto(catalogo, codigo):
    """Descripcion: Busca un producto por su código en un catálogo ordenado alfabéticamente.
    Pre: catalogo debe ser una lista de tuplas (codigo, precio) ordenada alfabéticamente por codigo, codigo debe ser una cadena de texto.
    Post: Devuelve el índice del producto si se encuentra, o -1 si no se encuentra."""
    izquierda = 0
    derecha = len(catalogo) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if catalogo[medio][0] == codigo:
            return medio
        elif catalogo[medio][0] < codigo:
            izquierda = medio + 1
        else:
            derecha = medio - 1 
    return -1

def generar_archivo_ventas(ruta):
    random.seed(42)
    catalogo = generar_catalogo()
    # productos estrella
    codigos = [c[0] for c in catalogo]
    pesos = [5 if i < 10 else 1 for i in range(50)]
    fecha_base = datetime(2024,3,1)
    ticket_id = 1
    with open(ruta, 'w') as ventas:
        for dia in range(30):
            dia_actual = (fecha_base + timedelta(days=dia)).strftime("%Y-%m-%d")
            tickets_dia = random.randint(8, 25)
            for ticket in range(tickets_dia):
                ventas.write(f"TICKET {ticket_id} | {dia_actual}\n")
                items = random.choices(range(1,9),weights=[30,25,18,12,7,4,2,2],k=1)[0]
                for item in range(items):
                    codigo = random.choices(codigos, weights=pesos, k=1)[0]
                    precio = buscar_producto(catalogo, codigo)
                    cantidad = random.choices(range(1,11),weights=[35,25,15,10,5,4,3,1,1,1],k=1)[0]
                    ventas.write(f"{codigo} | {precio:.2f} | {cantidad}\n")
                ticket_id += 1