[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/i_JmIVTt)
# Desafío 1 — Bitmap de espacio libre

**Curso:** Algoritmos y Programación I / Fundamentos de Programación — FIUBA
**Semana:** 8 — Archivos binarios
**Tipo:** Desafío extracurricular grupal
**Tamaño de equipo:** 2 personas
**Plazo sugerido:** 1 semana desde la fecha de aceptación

---

## Contexto

En la Sección 5 del documento teórico desarrollamos el manejo del espacio libre en un archivo binario de registros de longitud fija usando una **free list encadenada**. Allí cada registro borrado guarda en su propio cuerpo el índice del siguiente registro libre, formando una lista enlazada cuya cabeza vive en la cabecera del archivo.

Este desafío explora la **alternativa que efectivamente usan los sistemas de archivos reales** (ext4, NTFS, APFS) para gestionar sus bloques: un **bitmap auxiliar** en un archivo separado, donde cada bit indica si el k-ésimo registro del archivo principal está libre (`1`) u ocupado (`0`).

## Objetivo

Reescribir el archivo de agenda de la Sección 5 reemplazando la free list encadenada por un bitmap externo, comparar empíricamente ambas estrategias, y discutir cuándo conviene cada una.

## Consignas

### (a) Diseño del registro

Definir un nuevo formato sin el campo `siguiente_libre` (innecesario porque el bitmap externo cumple esa función). El campo `activo` se mantiene únicamente como redundancia defensiva contra desincronización entre los dos archivos.

```python
FORMATO_REG = '<B i 32s 16s 40s'   # activo + id + nombre + telefono + email
```

### (b) Diseño del bitmap

El bitmap se almacena en un archivo paralelo `agenda.bitmap`. Para un archivo principal de N registros, el bitmap ocupa `(N + 7) // 8` bytes (cada byte cubre 8 registros).

Convención de bits:

- Bit `1` → registro libre / disponible para reuso
- Bit `0` → registro ocupado / con datos válidos

El registro k está en el byte `k // 8` del bitmap, en la posición `k % 8` (bit menos significativo = registro de menor índice dentro del byte).

### (c) Operaciones a implementar

Implementar las siguientes funciones, manteniendo consistencia entre `agenda.dat` y `agenda.bitmap` en cada operación:

- `inicializar_archivo(ruta)` — crea ambos archivos vacíos.
- `alta(ruta, id, nombre, telefono, email)` — busca el primer bit `1` del bitmap, escribe el registro en esa posición, marca el bit como `0`. Si no hay bits libres, agrega al final y extiende el bitmap si es necesario. Devuelve el índice físico del registro.
- `baja(ruta, k)` — marca el bit k como `1`. Opcionalmente actualiza el byte `activo` del registro a `0` (redundancia defensiva).
- `modificacion(ruta, k, nuevo_email)` — actualiza el email del registro k *in situ*, verificando previamente que el bit k sea `0` (registro ocupado).
- `listar_activos(ruta)` — recorre el bitmap byte por byte, identifica los registros ocupados (bits `0`), los lee y devuelve la lista de tuplas.
- `contar_libres(ruta)` — cuenta los bits `1` del bitmap usando `bin(byte).count('1')` para cada byte, en O(N/8) sin tocar el archivo de datos.

### (d) Verificación de consistencia

Implementar `verificar_consistencia(ruta)` que devuelva `True` si para cada registro k del archivo principal, el bit k del bitmap es coherente con el byte `activo` del registro (ambos indican lo mismo). Esta función simula la verificación de integridad que un sistema de archivos real ejecuta tras un cierre abrupto.

### (e) Comparación experimental

Implementar un script `experimento.py` que ejecute la **misma secuencia de operaciones** (1000 altas, 500 bajas aleatorias con `random.seed(42)`, 500 altas más) sobre dos implementaciones:

- La implementación con free list encadenada del Problema 3 del laboratorio (puede tomarse de la solución de clase si está disponible, o reimplementarse).
- La implementación con bitmap de este desafío.

Medir: tiempo total de ejecución (con `time.perf_counter()`) y tamaño final de ambos archivos. Generar una tabla comparativa.

### (f) Discusión

En el archivo `informe.md` (plantilla provista), responder:

1. ¿En qué condiciones es preferible cada implementación?
2. ¿Por qué los sistemas de archivos reales (ext4, NTFS, APFS) eligen mayoritariamente bitmaps en lugar de free lists?
3. ¿Qué ventaja específica tiene `bin(byte).count('1')` sobre recorrer la free list cuando se quiere saber cuántos slots hay disponibles?

## Estructura del repositorio

```
desafio1-bitmap/
├── README.md                    ← este archivo
├── agenda_bitmap.py             ← implementación principal (a completar)
├── experimento.py               ← script de comparación (a completar)
├── informe.md                   ← plantilla del informe (a completar)
├── tests/
│   └── test_agenda_bitmap.py    ← tests automatizados (no modificar)
├── .gitignore
└── requirements.txt
```

## Cómo ejecutar los tests

```bash
pip install -r requirements.txt
pytest tests/ -v
```

Los tests sirven como criterio objetivo de avance: el grupo puede ir validando cada función a medida que la implementa. **Pasar todos los tests es condición necesaria pero no suficiente para una entrega completa** (el informe y la discusión también se evalúan).

## Entrega

La entrega consiste en hacer `git push` al repositorio antes del plazo. El último commit antes del plazo es lo que se evalúa. Los archivos generados por la ejecución del código (`agenda.dat`, `agenda.bitmap`, `__pycache__/`) **no deben commitearse** (el `.gitignore` ya los excluye).

## Convenciones del curso aplicables

- `for` / `range()` para iteraciones determinadas; `while` solo para iteraciones indeterminadas.
- No usar `break`. Si una condición de salida es compuesta, articularla en el `while` o usar inspección posterior al ciclo.
- Docstring dentro de cada función, accesible mediante `help()`.
- Estructura de programa: Declarativa → Funciones (con Prólogo / Resolución / Epílogo) → Algorítmica.
- Constantes globales declaradas una vez en el bloque declarativo. `TAM_REGISTRO = struct.calcsize(FORMATO_REG)` (no hardcodear el número).
- `random.seed(42)` para todos los experimentos reproducibles.
- Comentarios de fin de línea alineados a dos espacios de la línea de código más larga (o a dos espacios de la línea que comentan).

## Rúbrica de evaluación (orientativa)

| Criterio | Peso |
|---|---|
| Corrección funcional (todos los tests pasan) | 30% |
| Calidad del diseño (modularidad, docstrings, convenciones) | 20% |
| Verificación de consistencia y manejo de casos límite | 15% |
| Experimento empírico (ejecución correcta + tabla coherente) | 15% |
| Informe técnico (claridad, profundidad de discusión) | 15% |
| Calidad del trabajo en GitHub (commits descriptivos, división de tareas visible) | 5% |
