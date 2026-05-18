# =============================================================================
# Experimento empirico - Desafio 1
# Compara la implementacion bitmap (este desafio) contra la free list del lab.
#
# Equipo: Fernandez Ivan, Villar Manuel
# =============================================================================

# -----------------------------------------------------------------------------
# Seccion declarativa
# -----------------------------------------------------------------------------
import random
import time
import os

import agenda_bitmap as ab

# Importar la implementacion con free list de la solucion del Problema 3 del lab.
# Si no esta disponible, comentar las lineas correspondientes y reportarlo en el
# informe.
try:
    import agenda_freelist as afl
    FREELIST_DISPONIBLE = True
except ImportError:
    FREELIST_DISPONIBLE = False
    print('Aviso: agenda_freelist.py no encontrado. Solo se medira bitmap.')
    

CANT_ALTAS_INICIALES  = 1000
CANT_BAJAS_ALEATORIAS = 500
CANT_ALTAS_FINALES    = 500


# -----------------------------------------------------------------------------
# Funciones del experimento
# -----------------------------------------------------------------------------
def ejecutar_secuencia_bitmap(ruta):
    """
    Ejecuta la secuencia experimental sobre la implementacion bitmap.
    Devuelve el tiempo total en segundos.

    Precondicion: ruta es un prefijo de una ruta valida, los archivos seran creados (o sobreescritos) por inicializar_archivo.
    Postcondicion: devuelve el tiempo total de ejecucion en segundos (float).
    Efecto secundario: crea/modifica ruta + '.dat' y ruta + '.bitmap'.
    """
    # Prologo:
    ab.inicializar_archivo(ruta)

    # Resolucion
    inicio = time.perf_counter()

    # Altas iniciales
    indices = []
    id_contador = 1
    k = 0
    while k < CANT_ALTAS_INICIALES:
        indice = ab.alta(
            ruta,
            id_contador,
            f'Contacto {id_contador}',
            f'000-{id_contador:04d}',
            f'c{id_contador}@fi.uba.ar',
        )
        indices.append(indice)
        id_contador += 1
        k += 1

    # Bajas aleatorias
    random.seed(42)
    indices_a_borrar = random.sample(indices, CANT_BAJAS_ALEATORIAS)
    j = 0
    while j < len(indices_a_borrar):
        ab.baja(ruta, indices_a_borrar[j])
        j += 1

    # Altas finales (reutilizan los huecos)
    m = 0
    while m < CANT_ALTAS_FINALES:
        ab.alta(
            ruta,
            id_contador,
            f'Nuevo {id_contador}',
            f'111-{id_contador:04d}',
            f'n{id_contador}@fi.uba.ar',
        )
        id_contador += 1
        m += 1

    fin = time.perf_counter()
    tiempo_total = fin - inicio

    # Epilogo
    return tiempo_total


def ejecutar_secuencia_freelist(ruta):
    """
    Ejecuta la misma secuencia experimental sobre la implementacion free list.

    Precondicion: FREELIST_DISPONIBLE es True, ruta es una ruta valida.
    Postcondicion: devuelve el tiempo total de ejecucion en segundos (float).
    Efecto secundario: crea/modifica ruta + '.dat'.
    """
    # Prologo
    afl.inicializar_archivo(ruta)

    # Resolucion
    inicio = time.perf_counter()

    # Altas iniciales
    indices = []
    id_contador = 1
    k = 0
    while k < CANT_ALTAS_INICIALES:
        indice = afl.alta(
            ruta,
            id_contador,
            f'Contacto {id_contador}',
            f'000-{id_contador:04d}',
            f'c{id_contador}@fi.uba.ar',
        )
        indices.append(indice)
        id_contador += 1
        k += 1

    # Bajas
    random.seed(42)
    indices_a_borrar = random.sample(indices, CANT_BAJAS_ALEATORIAS)
    j = 0
    while j < len(indices_a_borrar):
        afl.baja(ruta, indices_a_borrar[j])
        j += 1

    # Altas finales (reutilizan los huecos)
    m = 0
    while m < CANT_ALTAS_FINALES:
        afl.alta(
            ruta,
            id_contador,
            f'Nuevo {id_contador}',
            f'111-{id_contador:04d}',
            f'n{id_contador}@fi.uba.ar',
        )
        id_contador += 1
        m += 1

    fin = time.perf_counter()

    # Epilogo
    return fin - inicio


def tamano_total(prefijo, extensiones):
    """
    Devuelve la suma de tamanios en bytes de los archivos prefijo + ext
    para cada ext en extensiones.

    Precondicion: prefijo es un string, extensiones es una lista de strings (por ejemplo ['.dat', '.bitmap']).
    Postcondicion: devuelve un entero >= 0.
    """
    #---Prologo---
    total = 0
    indice = 0
    #Resolucion:
    while indice < len(extensiones):
        ruta_completa = prefijo + extensiones[indice]
        if os.path.exists(ruta_completa):
            total += os.path.getsize(ruta_completa)
        indice += 1
    #Epilogo
    return total


# -----------------------------------------------------------------------------
# Seccion algoritmica
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    # Prologo
    print('Experimento: bitmap vs. free list')
    print(f'Secuencia: {CANT_ALTAS_INICIALES} altas + {CANT_BAJAS_ALEATORIAS} bajas + {CANT_ALTAS_FINALES} altas')
    print()

    # Resolucion
    # 1) Medir bitmap
    RUTA_BMP = 'exp_bitmap'
    tiempo_bitmap = ejecutar_secuencia_bitmap(RUTA_BMP)
    bytes_bitmap  = tamano_total(RUTA_BMP, ['.dat', '.bitmap'])

    # 2) Si FREELIST_DISPONIBLE, medir free list
    if FREELIST_DISPONIBLE: 
        RUTA_FL = 'exp_freelist.dat'
        tiempo_fl = ejecutar_secuencia_freelist(RUTA_FL)
        bytes_fl  = tamano_total('exp_freelist', ['.dat'])

    # 3) Imprimir tabla comparativa
    print("\t\tBitmap\t\tFree List")    
    print('-' * 60)
    
    if FREELIST_DISPONIBLE:
        tiempo_fl_str = f'{tiempo_fl:.4f}s'
        bytes_fl_str  = f'{bytes_fl:,} bytes'
    else:
        tiempo_fl_str = 'Free list no disponible'
        bytes_fl_str  = 'Free list no disponible'
    
    print(f"Tiempo total\t{tiempo_bitmap:.4f}s\t\t{tiempo_fl_str}") #\t tabula, :, Formatea a miles, .4f formatea a 4 decimales
    print(f"Tamaño en disco\t{bytes_bitmap:,} bytes\t{bytes_fl_str}")
 
    if FREELIST_DISPONIBLE:

        if tiempo_fl > 0:
            factor_tiempo = tiempo_bitmap / tiempo_fl
        else:
            factor_tiempo = float('inf')

        if bytes_fl > 0:
            factor_bytes = bytes_bitmap / bytes_fl
        else:
            factor_bytes = float('inf')
        print()
        print(f'Relacion bitmap/freelist | tiempo: {factor_tiempo:.2f}x  |  disco: {factor_bytes:.2f}x') #x es por "veces mas"
    # Epilogo
    print()
    print('Recordar transcribir los resultados al informe.md')