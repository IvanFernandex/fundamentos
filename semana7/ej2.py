"""
(a) Explicar en un comentario de varias líneas por qué agregar_elemento modifica la
lista original pero intentar_reemplazar no.

(b) Escribir una versión sin efecto secundario de agregar_elemento llamada
agregar_elemento_puro(lista, elemento) que retorne una nueva lista sin
modificar la original. Documentar la ausencia de efecto secundario en la docstring.

(c) Escribir una función extender_si_corta(datos, minimo, valor_relleno)
que, si la lista datos tiene menos de minimo elementos, la extienda hasta alcanzar la longitud minimo. Decidir y documentar si la función tiene o no efecto secundario, y
justificar la decisión."""

def agregar_elemento(lista, elemento):
    """Agrega un elemento al final de la lista.
Precondición: lista es una lista, elemento es cualquier valor.
Postcondición: la lista queda con el elemento agregado al final.
Efecto secundario: modifica la lista recibida.
    """
    lista.append(elemento)
    return lista
def intentar_reemplazar(lista, nueva):
    """Intenta reemplazar la lista por otra.
Precondición: lista y nueva son listas.
Postcondición: retorna nueva; la lista original NO se modifica.
    """
    lista = nueva
    return lista
# === Sección algorítmica ===
# --- Prólogo ---
original = [10, 20, 30]
print(f"Antes: original = {original}, id = {id(original)}")
# --- Resolución ---
resultado1 = agregar_elemento(original, 40)
print(f"Después 1: original = {original}, id = {id(original)}")
print(f" resultado1 is original: {resultado1 is original}")
resultado2 = intentar_reemplazar(original, [99, 98, 97])
print(f"Después 2: original = {original}, id = {id(original)}")
print(f" resultado2 = {resultado2}")
print(f" resultado2 is original: {resultado2 is original}")

"""Resultado esperado:"
original = [10, 20, 30]
resultado1 = agregar_elemento(original, 40)

original --> [10, 20, 30, 40]
resultado1 is original --> True"""

"""
a) agregar_elemento modifica la lista original porque usa append(),
que actúa sobre el mismo objeto (mutable). Como la función recibe
una referencia al objeto, el cambio es visible fuera.

intentar_reemplazar NO modifica la lista original porque hace:
lista = nueva

Esto NO modifica el objeto original, sino que reasigna el nombre
local 'lista' a otro objeto. La variable original sigue apuntando
al objeto inicial.
"""
#b)
def agregar_elemento_puro(lista, elemento):
    """Devuelve una nueva lista con el elemento agregado.

    Precondición: lista es una lista.
    Postcondición: retorna una nueva lista.
    Sin efecto secundario.
    """
    return lista + [elemento]
#c)
def extender_si_corta(datos, minimo, valor_relleno):
    """Extiende la lista hasta alcanzar un mínimo de elementos.

    Precondición: datos es una lista.
    Postcondición: la lista tiene al menos 'minimo' elementos.
    Efecto secundario: modifica la lista original.
    """
    while len(datos) < minimo:
        datos.append(valor_relleno)
    