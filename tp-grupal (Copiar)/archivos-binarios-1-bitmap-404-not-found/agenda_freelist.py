import struct
import os

FORMATO_CABECERA = '<4sii'                        # magic, cantidad, cabeza_libre
TAM_CABECERA     = struct.calcsize(FORMATO_CABECERA)  # 12
MAGIC            = b'AGD1'

FORMATO_REG  = '<Bi i32s16s40s'                  # activo, siguiente_libre, id, nombre, telefono, email
TAM_REGISTRO = struct.calcsize(FORMATO_REG)       # 97

ACTIVO    = 1
BORRADO   = 0
FIN_LISTA = -1


# -----------------------------------------------------------------------------
# Funciones — cabecera
# -----------------------------------------------------------------------------
def inicializar_archivo(ruta):
    """
    Crea un archivo nuevo con la cabecera vacia (sin registros).

    Precondicion: ruta es un path valido en el sistema de archivos.
    Postcondicion: el archivo tiene TAM_CABECERA bytes y ningun registro.
    """
    with open(ruta, 'wb') as archivo:
        cab = struct.pack(FORMATO_CABECERA, MAGIC, 0, FIN_LISTA)
        archivo.write(cab)


def leer_cabecera(archivo):
    """
    Lee la cabecera del archivo y devuelve sus campos.

    Precondicion: archivo esta abierto en modo 'rb' o 'r+b'.
    Postcondicion: devuelve (magic, cantidad, cabeza_libre); el cursor
                   queda al final de la cabecera.
    """
    archivo.seek(0)
    datos = archivo.read(TAM_CABECERA)
    return struct.unpack(FORMATO_CABECERA, datos)


def escribir_cabecera(archivo, cantidad, cabeza_libre):
    """
    Actualiza la cabecera del archivo con los valores dados.

    Precondicion: archivo esta abierto en modo 'r+b'.
    Postcondicion: la cabecera queda actualizada; cursor al final de la cabecera.
    """
    archivo.seek(0)
    archivo.write(struct.pack(FORMATO_CABECERA, MAGIC, cantidad, cabeza_libre))


# -----------------------------------------------------------------------------
# Funciones — registros
# -----------------------------------------------------------------------------
def offset_de(k):
    """Devuelve el offset fisico del registro k-esimo dentro del archivo."""
    return TAM_CABECERA + k * TAM_REGISTRO


def leer_registro(archivo, k):
    """
    Lee el registro k-esimo y lo devuelve como tupla.

    Precondicion: 0 <= k < cantidad de registros; archivo abierto en 'rb' o 'r+b'.
    Postcondicion: devuelve (activo, siguiente, id, nombre, telefono, email).
    """
    archivo.seek(offset_de(k))
    datos = archivo.read(TAM_REGISTRO)
    activo, sig, id_, nom, tel, mail = struct.unpack(FORMATO_REG, datos)
    nombre   = nom.rstrip(b'\x00').decode('utf-8')
    telefono = tel.rstrip(b'\x00').decode('utf-8')
    email    = mail.rstrip(b'\x00').decode('utf-8')
    return activo, sig, id_, nombre, telefono, email


def escribir_registro(archivo, k, activo, siguiente, id_, nombre, telefono, email):
    """
    Escribe un registro completo en la posicion k-esima.

    Precondicion: archivo abierto en 'r+b'; 0 <= k <= cantidad (permite append).
    Postcondicion: los TAM_REGISTRO bytes que comienzan en offset_de(k)
                   quedan con los nuevos valores.
    """
    datos = struct.pack(
        FORMATO_REG,
        activo,
        siguiente,
        id_,
        nombre.encode('utf-8'),
        telefono.encode('utf-8'),
        email.encode('utf-8'),
    )
    archivo.seek(offset_de(k))
    archivo.write(datos)


# -----------------------------------------------------------------------------
# Operaciones ABM
# -----------------------------------------------------------------------------
def alta(ruta, id_, nombre, telefono, email):
    """
    Da de alta un nuevo contacto, reutilizando un registro libre si lo hay.

    Politica: si hay registros libres en la free list, reutiliza el primero
    (cabeza); si no, agrega al final del archivo.

    Precondicion: ruta apunta a un archivo valido inicializado con
                  inicializar_archivo. id_ es int, los demas son str.
    Postcondicion: el contacto queda en el archivo; devuelve el indice k
                   donde quedo almacenado.
    Efecto secundario: actualiza el archivo (registro + cabecera).
    """
    with open(ruta, 'r+b') as archivo:
        _, cantidad, cabeza_libre = leer_cabecera(archivo)

        if cabeza_libre != FIN_LISTA:
            # Reutilizar el registro libre en la cabeza de la free list
            k = cabeza_libre
            _, siguiente_nuevo, _, _, _, _ = leer_registro(archivo, k)
            escribir_registro(archivo, k, ACTIVO, FIN_LISTA, id_, nombre, telefono, email)
            escribir_cabecera(archivo, cantidad, siguiente_nuevo)
        else:
            # Agregar al final del archivo
            k = cantidad
            escribir_registro(archivo, k, ACTIVO, FIN_LISTA, id_, nombre, telefono, email)
            escribir_cabecera(archivo, cantidad + 1, cabeza_libre)

    return k


def baja(ruta, k):
    """
    Da de baja (logica) el registro k-esimo.

    Precondicion: 0 <= k < cantidad; el registro k esta activo.
    Postcondicion: el registro queda marcado como borrado y enlazado al
                   frente de la free list.
    Efecto secundario: actualiza el archivo (registro k + cabecera).
    """
    with open(ruta, 'r+b') as archivo:
        _, cantidad, cabeza_libre = leer_cabecera(archivo)
        escribir_registro(archivo, k, BORRADO, cabeza_libre, 0, '', '', '')
        escribir_cabecera(archivo, cantidad, k)


def modificacion(ruta, k, id_, nombre, telefono, email):
    """
    Modifica in situ el contenido del registro k-esimo.

    Precondicion: 0 <= k < cantidad; el registro k esta activo.
    Postcondicion: los campos del registro k-esimo quedan actualizados;
                   activo y siguiente_libre no cambian.
    Efecto secundario: actualiza el archivo (solo el registro k).
    """
    with open(ruta, 'r+b') as archivo:
        escribir_registro(archivo, k, ACTIVO, FIN_LISTA, id_, nombre, telefono, email)


# -----------------------------------------------------------------------------
# Consulta
# -----------------------------------------------------------------------------
def listar_activos(ruta):
    """
    Recorre el archivo y devuelve los contactos activos.

    Precondicion: ruta apunta a un archivo valido.
    Postcondicion: devuelve una lista de tuplas (id, nombre, telefono, email)
                   con los registros cuyo flag activo es ACTIVO, en orden de
                   indice fisico.
    """
    resultado = []
    with open(ruta, 'rb') as archivo:
        _, cantidad, _ = leer_cabecera(archivo)
        k = 0
        while k < cantidad:
            activo, _, id_, nombre, telefono, email = leer_registro(archivo, k)
            if activo == ACTIVO:
                resultado.append((id_, nombre, telefono, email))
            k += 1
    return resultado


if __name__ == '__main__':
    # Prologo
    RUTA = 'agenda_fl.dat'

    # Resolucion: ejemplo de uso pdf
    inicializar_archivo(RUTA)
    alta(RUTA, 1, 'Ada Lovelace',    '4567-1122', 'ada@fi.uba.ar')
    alta(RUTA, 2, 'Alan Turing',     '4511-8890', 'alan@fi.uba.ar')
    alta(RUTA, 3, 'Grace Hopper',    '4533-2214', 'grace@fi.uba.ar')
    baja(RUTA, 1)# borra Alan
    baja(RUTA, 3)                                                     
    nuevo = alta(RUTA, 4, 'Linus Torvalds', '4598-5567', 'linus@fi.uba.ar')

    # Epilogo
    print(f'Linus se escribio en el slot {nuevo} (deberia ser 1, reusado)')
    print(f'Activos: {listar_activos(RUTA)}')