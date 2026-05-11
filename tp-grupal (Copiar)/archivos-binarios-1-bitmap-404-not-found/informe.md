# Informe técnico — Desafío 1 (bitmap de espacio libre)

**Equipo:** _completar con los nombres de los integrantes_
**Fecha:** _completar_

---

## 1. División de tareas

Describir brevemente cómo se distribuyó el trabajo entre los dos integrantes.

| Integrante | Responsabilidades principales | Commits aprox. |
|---|---|---|
| _Nombre 1_ | _ej.: funciones auxiliares de bitmap, listar_activos, contar_libres_ | _N_ |
| _Nombre 2_ | _ej.: alta/baja/modificacion, verificar_consistencia, experimento_ | _N_ |

## 2. Decisiones de diseño

### 2.1 Organización del bitmap

Justificar la convención de bits elegida (bit `1` = libre vs. bit `0` = libre) y por qué.

### 2.2 Tratamiento del campo `activo` redundante

Justificar la decisión de mantener (o no) el byte `activo` dentro del registro, dado que el bitmap externo ya cumple esa función. ¿Aporta robustez? ¿Vale la pena el costo?

## 3. Resultados experimentales

Tabla comparativa para la secuencia: 1000 altas + 500 bajas aleatorias + 500 altas más, con `random.seed(42)`:

| Implementación | Tiempo total (s) | Tamaño archivo principal (B) | Tamaño estructura auxiliar (B) | Total (B) |
|---|---:|---:|---:|---:|
| Free list encadenada | _completar_ | _completar_ | _0 (en cabecera)_ | _completar_ |
| Bitmap externo | _completar_ | _completar_ | _completar_ | _completar_ |

Diferencia porcentual de tiempo: _completar_

Diferencia porcentual de tamaño: _completar_

## 4. Discusión

### 4.1 ¿En qué condiciones es preferible cada implementación?

_Desarrollar 2 a 4 párrafos. Considerar: cantidad esperada de registros, frecuencia relativa de altas y bajas, importancia de la velocidad de cálculo de estadísticas (cuántos libres / cuántos ocupados), riesgo de pérdida de la cabeza de la free list, ..._

### 4.2 ¿Por qué los sistemas de archivos reales eligen mayoritariamente bitmaps?

_Considerar: ext4 con bitmaps de bloques y bitmaps de inodos, NTFS con `$Bitmap`, APFS con `bitmap allocator`. Identificar por lo menos dos razones por las que la elección por bitmap predomina pese a su mayor consumo de espacio relativo._

### 4.3 Ventaja específica de `bin(byte).count('1')`

_¿Por qué calcular cuántos bits están encendidos en un byte usando `bin(byte).count('1')` es eficiente? ¿Cómo escala con la cantidad de registros? Comparar con el costo equivalente sobre la free list._

## 5. Conexión con conceptos del curso

Identificar al menos tres conceptos previos del curso que se reutilizan en este desafío y dónde aparecen:

- _ej.: operaciones bit a bit (Semana 2)_
- _..._
- _..._

## 6. Reflexión sobre el trabajo en GitHub

_Breve reflexión sobre el flujo de trabajo: cómo coordinaron commits, si surgieron conflictos de merge, cómo los resolvieron, qué aprendieron sobre el trabajo colaborativo en repositorios._
