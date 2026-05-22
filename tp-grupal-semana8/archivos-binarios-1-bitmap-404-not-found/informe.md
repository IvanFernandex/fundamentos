# Informe técnico — Desafío 1 (bitmap de espacio libre)

**Equipo:** Fernandez Ivan ; Villar Manuel
**Fecha:** 14/05/2026

---

## 1. División de tareas

Describir brevemente cómo se distribuyó el trabajo entre los dos integrantes.

| Integrante | Responsabilidades principales | Commits aprox. |
|---|---|---|
| Fernandez Ivan | Verificar consistencia, contribucion en alta y baja, marcar libre y ocupado, experimentos.py | 7 |
| Villar Manuel | Implementación de contar libres, listar activos, inicializar archivo, contribución en alta y baja, informe.md  | 5 |

## 2. Decisiones de diseño

### 2.1 Organización del bitmap

Justificar la convención de bits elegida (bit `1` = libre vs. bit `0` = libre) y por qué.

Nos pareció más lógico usar 1 para representar el bit libre ya que está disponible y hay espacio mientras que 0 representaria el ocupado porque no tiene espacio.

### 2.2 Tratamiento del campo `activo` redundante

Justificar la decisión de mantener (o no) el byte `activo` dentro del registro, dado que el bitmap externo ya cumple esa función. ¿Aporta robustez? ¿Vale la pena el costo?

Se decidió mantener el byte activo dentro del registro como redundancia defensiva. Si bien el bitmap externo ya indica qué slots están ocupados, tener el byte activo en el .dat permite detectar inconsistencias entre ambos archivos.


## 3. Resultados experimentales

Tabla comparativa para la secuencia: 1000 altas + 500 bajas aleatorias + 500 altas más, con `random.seed(42)`:

| Implementación | Tiempo total (s) | Tamaño archivo principal (B) | Tamaño estructura auxiliar (B) | Total (B) |
|---|---:|---:|---:|---:|
| Free list encadenada | _0.0221_ | _97012_ | _0 (en cabecera)_ | _97012_ |
| Bitmap externo | _0.1374_ | _93000_ | _125_ | _93125_ |

Diferencia porcentual de tiempo: _El bitmap tardó un 521% más que la free list (6.23x más lento)_

Diferencia porcentual de tamaño: _El bitmap ocupa un 4% menos que la free list (0.96x el tamaño total)_

## 4. Discusión

### 4.1 ¿En qué condiciones es preferible cada implementación?

_Desarrollar 2 a 4 párrafos. Considerar: cantidad esperada de registros, frecuencia relativa de altas y bajas, importancia de la velocidad de cálculo de estadísticas (cuántos libres / cuántos ocupados), riesgo de pérdida de la cabeza de la free list, ..._


La free list encadenada es preferible cuando el archivo tiene pocos registros y la velocidad de las operaciones de alta y baja es crítica. Al almacenar el índice del siguiente libre dentro del registro borrado, encontrar un slot disponible es O(1): basta leer la cabecera. Sin embargo, si la cabecera se corrompe (por un cierre abrupto, por ejemplo), toda la cadena se pierde y no hay forma de reconstruirla sin recorrer el archivo completo.


El bitmap externo es preferible cuando la cantidad de registros es grande, cuando se necesita calcular frecuentemente cuántos slots están libres, o cuando la robustez ante fallos es prioritaria. Al ser un archivo separado y compacto, verificar la consistencia global es barato. La desventaja observada en el experimento es que cada alta requiere abrir y recorrer el bitmap para encontrar el primer bit libre, lo que lo hace más lento que la free list en operaciones individuales.



### 4.2 ¿Por qué los sistemas de archivos reales eligen mayoritariamente bitmaps?

_Considerar: ext4 con bitmaps de bloques y bitmaps de inodos, NTFS con `$Bitmap`, APFS con `bitmap allocator`. Identificar por lo menos dos razones por las que la elección por bitmap predomina pese a su mayor consumo de espacio relativo._


El bitmap permite verificar y reconstruir el estado del sistema de archivos de forma eficiente tras un cierre abrupto. Con una free list, si se pierde la cabeza de la lista, la información de qué bloques están libres desaparece; con un bitmap, basta recorrer todos los bits para reconstruir el estado completo. El bitmap permite calcular en O(N/8) cuántos bloques libres quedan en el disco, una estadística que el sistema operativo necesita constantemente para decidir si puede alojar nuevos archivos. Con una free list, esa misma operación requeriría recorrer toda la cadena de nodos libres, lo que es O(cantidad de libres).


### 4.3 Ventaja específica de `bin(byte).count('1')`

_¿Por qué calcular cuántos bits están encendidos en un byte usando `bin(byte).count('1')` es eficiente? ¿Cómo escala con la cantidad de registros? Comparar con el costo equivalente sobre la free list._

`bin(byte).count('1')` convierte un byte a su representación binaria en string y cuenta los caracteres '1' procesando 8 bits en una sola operación. Para un archivo de N registros el bitmap tiene (N+7) // 8 bytes por lo que contar todos los libres cuesta O(N/8) iteraciones es decir 8 veces menos pasos que revisar cada registro individualmente. En la freelist habria que recorrer toda la cadena de nodos libres lo que en el peor de los casos quedaria como  O(N). El bitmap siempre gana en esta operación especifica. 

## 5. Conexión con conceptos del curso

Identificar al menos tres conceptos previos del curso que se reutilizan en este desafío y dónde aparecen:

- Operaciones bit a bit (Semana 2) : Se usan en bit libre , marcar libre, marcar ocupado para leer y modificar bits individuales
- Archivos binarios (Semana 8) : Toda la lectura y escritura usa acceso directo por seek aprovechando que los registros tienen longitud fija
- Estructuras iterativas while (Semana 3) : Utilizacion del bucle while varias veces en todo el archivo agenda_bitmap.py

## 6. Reflexión sobre el trabajo en GitHub

_Breve reflexión sobre el flujo de trabajo: cómo coordinaron commits, si surgieron conflictos de merge, cómo los resolvieron, qué aprendieron sobre el trabajo colaborativo en repositorios._

En un inicio no tuvimos problema ya que teniamos buena comunicacion, esto evitaba que surjan merge conflicts sin embargo por error mio (Villar Manuel) hubo un merge conflict que solucioné gracias a Pycharm eligiendo una de las versiones que habia trabajado mi compañero. Por el resto el trabajo con github fue bastante bien gracias a que tambien lo utilizamos en otra materia por lo que estabamos bastante comodos.
