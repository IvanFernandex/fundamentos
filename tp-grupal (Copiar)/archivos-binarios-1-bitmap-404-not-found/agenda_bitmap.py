# =============================================================================
# Desafio 1 - Bitmap de espacio libre
# Algoritmos y Programacion I / Fundamentos de Programacion - FIUBA
# Semana 8 - Archivos binarios
#
# Equipo: <COMPLETAR con los nombres de los integrantes>
# =============================================================================

# -----------------------------------------------------------------------------
# Seccion declarativa
# -----------------------------------------------------------------------------
import struct
import os

FORMATO_REG = '<B i 32s 16s 40s'             # activo + id + nombre + telefono + email
TAM_REGISTRO = struct.calcsize(FORMATO_REG)  # fuente unica de verdad: NO hardcodear

ACTIVO = 1                                   # valor del byte 'activo' en registro vivo
LIBRE = 0                                    # valor del byte 'activo' en registro borrado

BITS_POR_BYTE = 8
NO_ENCONTRADO = -1


# -----------------------------------------------------------------------------
# Funciones auxiliares de bitmap
# -----------------------------------------------------------------------------
def bit_libre(bitmap, k):
    """
    Devuelve True si el registro k esta marcado como libre en el bitmap.

    Precondicion: bitmap es un bytearray de longitud suficiente para cubrir
                  al menos k+1 registros.
    Postcondicion: True si el bit k del bitmap es 1, False si es 0.
    """

    indice_byte = k // BITS_POR_BYTE #indice del byte que contiene el bit k
    bit = k % BITS_POR_BYTE #posicion dentro del byte
    return (bitmap[indice_byte] >> bit) & 1 == 1


def marcar_libre(bitmap, k):
    """
    Marca el registro k como libre (bit en 1).

    Precondicion: bitmap es un bytearray con espacio para el registro k.
    Postcondicion: el bit k del bitmap queda en 1.
    Efecto secundario: modifica bitmap in-place.
    """

    indice_byte = k // BITS_POR_BYTE
    bit = k % BITS_POR_BYTE
    bitmap[indice_byte] |= (1 << bit) 


def marcar_ocupado(bitmap, k):
    """
    Marca el registro k como ocupado (bit en 0).

    Precondicion: bitmap es un bytearray con espacio para el registro k.
    Postcondicion: el bit k del bitmap queda en 0.
    Efecto secundario: modifica bitmap in-place.
    """
    indice_byte = k // BITS_POR_BYTE
    bit = k % BITS_POR_BYTE
    bitmap[indice_byte] &= ~(1 << bit) # Utilizamos el operador AND con la negación del bit para ponerlo en 0

def buscar_primer_libre(bitmap, max_registros):
    """
    Busca el menor indice k en [0, max_registros) tal que bit_libre(bitmap, k).

    Precondicion: bitmap es un bytearray, max_registros >= 0.
    Postcondicion: devuelve el menor indice libre, o -1 si no hay ninguno.
    """
    indice_registro = 0

    while indice_registro < max_registros:
        #buscar el bit libre 
        if bit_libre(bitmap, indice_registro):
            return indice_registro
        indice_registro += 1
    return NO_ENCONTRADO #Definido como constante con el valor -1 (Mejora claridad al programa)
# -----------------------------------------------------------------------------
# Operaciones del archivo
# -----------------------------------------------------------------------------
def inicializar_archivo(ruta):
    """
    Crea ambos archivos (datos y bitmap) vacios. Si ya existen los reemplaza.

    Precondicion: ruta es un prefijo valido de path en el sistema de archivos.
    Postcondicion: existen ruta + '.dat' y ruta + '.bitmap' como archivos vacios.
    """
    #Inicializamos los archivo de datos vacios
    with open(ruta + '.dat', 'wb') as archivo_dat:
        archivo_dat.write(b'') 

    with open(ruta + '.bitmap', 'wb') as archivo_bitmap:
        archivo_bitmap.write(b'')

def alta(ruta, id, nombre, telefono, email):
    """
    Agrega un registro al archivo.

    Politica de asignacion: reutiliza el primer registro libre del bitmap si
    existe; si no, agrega al final del archivo y extiende el bitmap.

    Precondicion: ruta apunta a un par de archivos validos creados por
                  inicializar_archivo. id es int, los demas son str.
    Postcondicion: devuelve el indice fisico (k) del registro escrito.
    Efecto secundario: actualiza ruta + '.dat' y ruta + '.bitmap'.
    """
    # COMPLETAR
    pass


def baja(ruta, k):
    """
    Marca el registro k como borrado (bit del bitmap en 1, byte 'activo' en 0).

    Precondicion: 0 <= k < cantidad de registros existentes.
    Postcondicion: el registro queda marcado como libre y disponible para reuso.
    Efecto secundario: actualiza ruta + '.dat' (byte 'activo' del registro k)
                       y ruta + '.bitmap' (bit k).
    """
    # COMPLETAR
    pass


def modificacion(ruta, k, nuevo_email):
    """
    Modifica el email del registro k in situ (sobrescribe los 40 bytes del
    campo email sin tocar el resto del registro).

    Precondicion: el registro k existe y esta activo (bit k del bitmap en 0).
    Postcondicion: el campo email del registro k contiene nuevo_email.
    Efecto secundario: actualiza ruta + '.dat'. Lanza ValueError si el
                       registro k no esta activo.
    """
    # COMPLETAR
    pass


def listar_activos(ruta):
    """
    Recorre el bitmap byte por byte, identifica los registros ocupados y
    devuelve la lista de tuplas (id, nombre, telefono, email) en orden de
    indice fisico.

    Precondicion: ruta apunta a un par de archivos validos.
    Postcondicion: devuelve una lista de tuplas (str ya decodificadas y
                   sin padding de bytes nulos).
    """
    # COMPLETAR
    pass


def contar_libres(ruta):
    """
    Cuenta los bits 1 del bitmap (registros libres).

    Precondicion: ruta apunta a un par de archivos validos.
    Postcondicion: devuelve un entero >= 0 con la cantidad de registros libres.

    Nota: la implementacion debe usar bin(byte).count('1') por byte,
    operando en O(N/8) sin tocar el archivo de datos.
    """
    # COMPLETAR
    pass


# -----------------------------------------------------------------------------
# Verificacion de consistencia
# -----------------------------------------------------------------------------
def verificar_consistencia(ruta):
    """
    Verifica que para cada registro k del archivo principal, el bit k del
    bitmap sea coherente con el byte 'activo' del registro.

    Coherencia: bit del bitmap = 1 (libre)    <=>  byte activo = 0 (LIBRE)
                bit del bitmap = 0 (ocupado)  <=>  byte activo = 1 (ACTIVO)

    Precondicion: ruta apunta a un par de archivos validos.
    Postcondicion: devuelve True si todos los registros son coherentes,
                   False si hay al menos uno inconsistente.
    """
    # COMPLETAR
    pass


# -----------------------------------------------------------------------------
# Seccion algoritmica (solo si se ejecuta como script, no como modulo)
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    # Prologo
    RUTA = 'agenda'

    # Resolucion: ejemplo minimo de uso
    inicializar_archivo(RUTA)
    alta(RUTA, 1, 'Ada Lovelace',    '4567-1122', 'ada@fi.uba.ar')
    alta(RUTA, 2, 'Alan Turing',     '4511-8890', 'alan@fi.uba.ar')
    alta(RUTA, 3, 'Grace Hopper',    '4533-2214', 'grace@fi.uba.ar')
    baja(RUTA, 1)                                                    # borra Alan
    nuevo = alta(RUTA, 4, 'Linus Torvalds', '4598-5567', 'linus@fi.uba.ar')

    # Epilogo
    print(f'Linus se escribio en el slot {nuevo} (deberia ser 1, reusado)')
    print(f'Activos: {listar_activos(RUTA)}')
    print(f'Libres:  {contar_libres(RUTA)}')
    print(f'Consistente: {verificar_consistencia(RUTA)}')
