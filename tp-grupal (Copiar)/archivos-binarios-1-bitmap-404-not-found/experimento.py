# =============================================================================
# Experimento empirico - Desafio 1
# Compara la implementacion bitmap (este desafio) contra la free list del lab.
#
# Equipo: <COMPLETAR>
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

CANT_ALTAS_INICIALES = 1000
CANT_BAJAS_ALEATORIAS = 500
CANT_ALTAS_FINALES = 500


# -----------------------------------------------------------------------------
# Funciones del experimento
# -----------------------------------------------------------------------------
def ejecutar_secuencia_bitmap(ruta):
    """
    Ejecuta la secuencia experimental sobre la implementacion bitmap.

    Devuelve el tiempo total en segundos.
    """
    # COMPLETAR
    pass


def ejecutar_secuencia_freelist(ruta):
    """
    Ejecuta la misma secuencia experimental sobre la implementacion free list.

    Devuelve el tiempo total en segundos.
    """
    # COMPLETAR (solo si FREELIST_DISPONIBLE)
    pass


def tamano_total(prefijo, extensiones):
    """
    Devuelve la suma de tamaños en bytes de los archivos prefijo + ext
    para cada ext en extensiones.
    """
    # COMPLETAR
    pass


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
    # 2) Si FREELIST_DISPONIBLE, medir free list
    # 3) Imprimir tabla comparativa

    # COMPLETAR

    # Epilogo
    print()
    print('Recordar transcribir los resultados al informe.md')
