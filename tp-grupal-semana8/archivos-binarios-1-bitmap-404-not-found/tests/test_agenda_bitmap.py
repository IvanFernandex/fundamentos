# =============================================================================
# Tests automatizados - Desafio 1 (bitmap de espacio libre)
#
# NO MODIFICAR este archivo. Estos tests son el criterio objetivo de avance.
# Si algun test falla, revisar la implementacion en agenda_bitmap.py
#
# Ejecutar con:  pytest tests/ -v
# =============================================================================

import os
import sys
import pytest
import tempfile
import random

# Permite importar el modulo del directorio raiz
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import agenda_bitmap as ab


# -----------------------------------------------------------------------------
# Fixtures
# -----------------------------------------------------------------------------
@pytest.fixture
def ruta_temporal(tmp_path):
    """Devuelve un prefijo de ruta dentro de un directorio temporal."""
    return str(tmp_path / 'agenda_test')


# -----------------------------------------------------------------------------
# Tests de las funciones auxiliares de bitmap
# -----------------------------------------------------------------------------
class TestBitmapAuxiliares:

    def test_bitmap_recien_creado_todo_libre(self):
        bitmap = bytearray(b'\xff\xff')                 # 16 bits en 1
        for k in range(16):
            assert ab.bit_libre(bitmap, k) == True

    def test_bitmap_todo_ocupado(self):
        bitmap = bytearray(b'\x00\x00')                 # 16 bits en 0
        for k in range(16):
            assert ab.bit_libre(bitmap, k) == False

    def test_marcar_libre(self):
        bitmap = bytearray(b'\x00')                     # todo ocupado
        ab.marcar_libre(bitmap, 3)
        assert ab.bit_libre(bitmap, 3) == True
        for k in [0, 1, 2, 4, 5, 6, 7]:
            assert ab.bit_libre(bitmap, k) == False

    def test_marcar_ocupado(self):
        bitmap = bytearray(b'\xff')                     # todo libre
        ab.marcar_ocupado(bitmap, 3)
        assert ab.bit_libre(bitmap, 3) == False
        for k in [0, 1, 2, 4, 5, 6, 7]:
            assert ab.bit_libre(bitmap, k) == True

    def test_marcar_libre_idempotente(self):
        bitmap = bytearray(b'\x00')
        ab.marcar_libre(bitmap, 3)
        ab.marcar_libre(bitmap, 3)
        assert ab.bit_libre(bitmap, 3) == True

    def test_buscar_primer_libre_sin_libres(self):
        bitmap = bytearray(b'\x00')                     # todo ocupado
        assert ab.buscar_primer_libre(bitmap, 8) == -1

    def test_buscar_primer_libre_primero(self):
        bitmap = bytearray(b'\xff')                     # todo libre
        assert ab.buscar_primer_libre(bitmap, 8) == 0

    def test_buscar_primer_libre_intermedio(self):
        bitmap = bytearray(b'\x00')                     # todo ocupado
        ab.marcar_libre(bitmap, 5)
        assert ab.buscar_primer_libre(bitmap, 8) == 5


# -----------------------------------------------------------------------------
# Tests del ciclo basico de operaciones
# -----------------------------------------------------------------------------
class TestCicloBasico:

    def test_inicializar_crea_archivos(self, ruta_temporal):
        ab.inicializar_archivo(ruta_temporal)
        assert os.path.exists(ruta_temporal + '.dat')
        assert os.path.exists(ruta_temporal + '.bitmap')

    def test_alta_devuelve_indice_cero(self, ruta_temporal):
        ab.inicializar_archivo(ruta_temporal)
        k = ab.alta(ruta_temporal, 1, 'Ada', '4567', 'ada@fi.uba.ar')
        assert k == 0

    def test_altas_consecutivas_indices_consecutivos(self, ruta_temporal):
        ab.inicializar_archivo(ruta_temporal)
        k0 = ab.alta(ruta_temporal, 1, 'Ada',   '4567', 'ada@fi.uba.ar')
        k1 = ab.alta(ruta_temporal, 2, 'Alan',  '4511', 'alan@fi.uba.ar')
        k2 = ab.alta(ruta_temporal, 3, 'Grace', '4533', 'grace@fi.uba.ar')
        assert (k0, k1, k2) == (0, 1, 2)

    def test_listar_activos_devuelve_todos(self, ruta_temporal):
        ab.inicializar_archivo(ruta_temporal)
        ab.alta(ruta_temporal, 1, 'Ada',   '4567', 'ada@fi.uba.ar')
        ab.alta(ruta_temporal, 2, 'Alan',  '4511', 'alan@fi.uba.ar')
        ab.alta(ruta_temporal, 3, 'Grace', '4533', 'grace@fi.uba.ar')
        activos = ab.listar_activos(ruta_temporal)
        assert len(activos) == 3
        ids = [r[0] for r in activos]
        assert ids == [1, 2, 3]


# -----------------------------------------------------------------------------
# Tests de baja y reuso
# -----------------------------------------------------------------------------
class TestBajaYReuso:

    def test_baja_marca_bit_como_libre(self, ruta_temporal):
        ab.inicializar_archivo(ruta_temporal)
        ab.alta(ruta_temporal, 1, 'Ada',   '4567', 'ada@fi.uba.ar')
        ab.alta(ruta_temporal, 2, 'Alan',  '4511', 'alan@fi.uba.ar')
        ab.alta(ruta_temporal, 3, 'Grace', '4533', 'grace@fi.uba.ar')
        ab.baja(ruta_temporal, 1)
        assert ab.contar_libres(ruta_temporal) == 1

    def test_baja_excluye_de_listar_activos(self, ruta_temporal):
        ab.inicializar_archivo(ruta_temporal)
        ab.alta(ruta_temporal, 1, 'Ada',   '4567', 'ada@fi.uba.ar')
        ab.alta(ruta_temporal, 2, 'Alan',  '4511', 'alan@fi.uba.ar')
        ab.alta(ruta_temporal, 3, 'Grace', '4533', 'grace@fi.uba.ar')
        ab.baja(ruta_temporal, 1)
        activos = ab.listar_activos(ruta_temporal)
        assert len(activos) == 2
        ids = [r[0] for r in activos]
        assert 2 not in ids                                                  # Alan estaba en slot 1
        assert ids == [1, 3]

    def test_alta_reusa_slot_borrado(self, ruta_temporal):
        ab.inicializar_archivo(ruta_temporal)
        ab.alta(ruta_temporal, 1, 'Ada',   '4567', 'ada@fi.uba.ar')
        ab.alta(ruta_temporal, 2, 'Alan',  '4511', 'alan@fi.uba.ar')
        ab.alta(ruta_temporal, 3, 'Grace', '4533', 'grace@fi.uba.ar')
        ab.baja(ruta_temporal, 1)
        nuevo = ab.alta(ruta_temporal, 4, 'Linus', '4598', 'linus@fi.uba.ar')
        assert nuevo == 1                                                    # debe reusar slot 1

    def test_alta_extiende_si_no_hay_libres(self, ruta_temporal):
        ab.inicializar_archivo(ruta_temporal)
        for i in range(8):
            ab.alta(ruta_temporal, i, f'P{i}', '0000', f'p{i}@fi.uba.ar')
        nuevo = ab.alta(ruta_temporal, 99, 'Nuevo', '9999', 'n@fi.uba.ar')
        assert nuevo == 8                                                    # extiende mas alla del primer byte


# -----------------------------------------------------------------------------
# Tests de consistencia y modificacion
# -----------------------------------------------------------------------------
class TestConsistencia:

    def test_consistencia_inicial(self, ruta_temporal):
        ab.inicializar_archivo(ruta_temporal)
        for i in range(5):
            ab.alta(ruta_temporal, i, f'P{i}', '0000', f'p{i}@fi.uba.ar')
        assert ab.verificar_consistencia(ruta_temporal) == True

    def test_consistencia_tras_bajas(self, ruta_temporal):
        ab.inicializar_archivo(ruta_temporal)
        for i in range(5):
            ab.alta(ruta_temporal, i, f'P{i}', '0000', f'p{i}@fi.uba.ar')
        ab.baja(ruta_temporal, 0)
        ab.baja(ruta_temporal, 3)
        assert ab.verificar_consistencia(ruta_temporal) == True

    def test_modificacion_actualiza_email(self, ruta_temporal):
        ab.inicializar_archivo(ruta_temporal)
        ab.alta(ruta_temporal, 1, 'Ada', '4567', 'ada@fi.uba.ar')
        ab.modificacion(ruta_temporal, 0, 'ada@anthropic.com')
        activos = ab.listar_activos(ruta_temporal)
        assert activos[0][3] == 'ada@anthropic.com'

    def test_modificacion_de_borrado_falla(self, ruta_temporal):
        ab.inicializar_archivo(ruta_temporal)
        ab.alta(ruta_temporal, 1, 'Ada', '4567', 'ada@fi.uba.ar')
        ab.baja(ruta_temporal, 0)
        with pytest.raises(ValueError):
            ab.modificacion(ruta_temporal, 0, 'fantasma@fi.uba.ar')


# -----------------------------------------------------------------------------
# Test de robustez con secuencia aleatoria
# -----------------------------------------------------------------------------
class TestSecuenciaLarga:

    def test_secuencia_aleatoria(self, ruta_temporal):
        random.seed(42)
        ab.inicializar_archivo(ruta_temporal)
        ids_vivos = set()

        for i in range(100):
            ab.alta(ruta_temporal, i, f'P{i}', '0000', f'p{i}@fi.uba.ar')
            ids_vivos.add(i)

        for _ in range(30):
            k = random.randint(0, 99)
            ab.baja(ruta_temporal, k)

        for i in range(100, 130):
            ab.alta(ruta_temporal, i, f'P{i}', '0000', f'p{i}@fi.uba.ar')

        assert ab.verificar_consistencia(ruta_temporal) == True
