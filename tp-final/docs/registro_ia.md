# Registro de interacciones con IA generativa

> Este registro es parte del proyecto final y se entrega versionado dentro del
> repositorio. No es una formalidad: es una herramienta de aprendizaje y, a la
> vez, lo que permite al docente entender el proceso real de elaboracion.
>
> **Criterio del curso:** todo el codigo que el equipo entrega debe ser codigo
> que el equipo puede explicar y defender linea por linea. La IA generativa es
> una herramienta —como una biblioteca de terceros o una consulta a una
> documentacion—; lo que se incorpora a la solucion es responsabilidad del
> equipo.
>
> **Cómo usar este archivo:** registrar **cada uso significativo** de IA
> generativa copiando el bloque de la plantilla de abajo. Hacerlo en el momento,
> no al final: el registro reconstruido a posteriori pierde su valor. Hacer
> commit del registro junto con el código al que se refiere.

---

## Plantilla de entrada

> Copiar este bloque para cada interacción y completarlo. Borrar esta cita.

### Entrada N — [fecha] — [integrante que la realizó]

**Contexto:** [en qué parte del proyecto se estaba trabajando y qué se
necesitaba resolver.]

**Herramienta utilizada:** [qué herramienta de IA generativa.]

**Prompt exacto:**

```
[el prompt tal como se escribió.]
```

**Respuesta obtenida:** [la respuesta, o su esencia si fue muy extensa. Si fue
código, puede incluirse aquí o resumirse.]

**Análisis crítico:** [qué se tomó de la respuesta y qué se descartó, y por qué.
¿La respuesta era correcta? ¿Tenía errores? ¿Se adaptaba a la estructura y la
metodología del proyecto, o hubo que reescribirla?]

**Aprendizaje:** [qué entendió mejor el equipo a partir de esta interacción.
¿Qué concepto quedó más claro? ¿Qué se haría distinto la próxima vez?]

---

## Registro

> A partir de aquí van las entradas reales del equipo, de la más antigua a la
> más reciente.

[completar — primera entrada.]

### Entrada 1 — [11/06] — [Fernandez Ivan]

**Contexto:** Se necesitaba implementar una funcion para actualizar los productos es decir la entrada y salida de los mismo. Lo que surgio es que al momento de implementar el diseño no se vio una inconsistencia la cual era que se iba a necesitar recorrer todos registros del archivo maestro es decir del (inventario.bin) hasta encontrar el codigo del producto para poder actualizarlo. Se necesitaba resolver eso y se busco una manera mas eficiente (Lo veia en el modo de que si era un archivo demasiado grande se iba a demorar demasiado tiempo y no iba a ser eficiente)

**Herramienta utilizada:** ChatGPT

**Prompt exacto:**

```
Teniendo en cuenta estos archivos (diseño, consignas) y el modulo archvios.py. 
Al momento de actualizar los productos se recorren todos los registros del archivo binario, se podria mejorar la funcionalidad de alguna manera que recomiendes? Tambien se penso en agregar un campo al diccionario con la posicion del registro
```

**Respuesta obtenida:** 
Sí. De hecho, en tu diseño actual hay una contradicción interesante:

Tenés un diccionario en memoria para buscar productos en O(1).
Pero cuando querés persistir una modificación en productos.bin, si recorrés todo el archivo para encontrar el producto, terminás haciendo una operación O(n).

La mejora más importante que podrías documentar para la Fase 3 sería implementar un índice de posiciones físicas en memoria.
```
Opción 1: Índice de posiciones (la que recomiendo)

Cuando cargás el inventario, además de guardar los datos del producto, guardás su posición dentro del archivo.

productos[codigo] = {
    "descripcion": descripcion,
    "stock": stock_actual,
    "stock_minimo": stock_minimo,
    "precio": precio,
    "posicion": numero_registro
}

o incluso
indices[codigo] = numero_registro

Durante la carga:

posicion = 0

while registro:
    ...
    indices[codigo] = posicion
    posicion += 1
```
Complejidad
Antes:
Buscar producto en archivo: O(n)
Sobrescribir: O(1)
Total:
O(n)
Después:
Buscar posición en diccionario: O(1)
seek(): O(1)
Sobrescribir: O(1)
Total:
O(1)

Opción 2: Reescribir el archivo completo

Otra posibilidad es:

Modificar el diccionario.
Al finalizar la operación, recrear todo el archivo.

**Análisis crítico:** [qué se tomó de la respuesta y qué se descartó, y por qué.
¿La respuesta era correcta? ¿Tenía errores? ¿Se adaptaba a la estructura y la
metodología del proyecto, o hubo que reescribirla?]

Se tomo como respuesta la opcion uno, ya que encaja fuertemente con el proyecto y sirvio para dar claridad y mejorar la eficiencia ya que no se tendria que estar recorriendo todo el archivo de los registros.
Se descarto la segunda opcion ya que no tendria sentido volver a reescribir el archivo completo a traves del diccionario ya que este se carga a partir del archivo y no viceversara, no seria algo logico con nuestra estructura del proyecto.

**Aprendizaje:** [qué entendió mejor el equipo a partir de esta interacción.
¿Qué concepto quedó más claro? ¿Qué se haría distinto la próxima vez?]

Se entendio mejor el concepto de las complejidades al momento de los registros ya que esta duda como bien mencione antes surgio al momento de pensar que seria mas optimo no tener que recorrer todos los registros del archivo, sino que se podria guardar la posicion de alguna manera para no tener que recorrer todo el archivo.
Creo que la proxima vez podriamos enfocarnos mas en los diseños de los registros y la complejidad que lleva el acceso a estos, tal ves estamos apresurandonos en tratar de llevar todo al codigo y no enfocarnos tanto en el diseño; esta vez nos dimos cuenta este error intentando codificar y no diseñando, podria ser mejor que suceda antes del codigo y no del diseño.

### Entrada 2 — [13/06] — [Fernandez Ivan]

**Contexto:** [en qué parte del proyecto se estaba trabajando y qué se
necesitaba resolver.]
[Se estaba trabajando en el modulo de validaciones y se necesitaba implementar una funcion que le pida al usuario una fecha en formato YYYY-MM-DD. El problema surgio creimos que habria alguna mejora en la funcion con el modulo datetime sin necesidad de tener que splitear la cadena ingresada por el usuario para verificar que sea el formato valido y no se tenga que hacer demasiadas validaciones.]

**Herramienta utilizada:** [ChatGPT]

**Prompt exacto:**

```
Se podria podria implementar una forma de pedir una fecha del formato YYYY-MM-DD, sin tener que splitear la cadena ingresada, se penso que se podria utilizar el modulo datetime.

```

**Respuesta obtenida:** [la respuesta, o su esencia si fue muy extensa. Si fue
código, puede incluirse aquí o resumirse.]

Sí, el módulo datetime es justamente la forma más limpia de validar una fecha sin tener que hacer split() manualmente.

Puedes usar datetime.strptime(), que intenta convertir una cadena al formato indicado y lanza una excepción si no coincide o si la fecha no existe.

from datetime import datetime

def pedir_fecha():
    fecha_valida = False

    while not fecha_valida:
        fecha = input("Ingrese una fecha (YYYY-MM-DD): ")

        try:
            datetime.strptime(fecha, "%Y-%m-%d")
            fecha_valida = True
        except ValueError:
            print("Error. Debe ingresar una fecha válida en formato YYYY-MM-DD.")

    return fecha


**Análisis crítico:** [qué se tomó de la respuesta y qué se descartó, y por qué.
¿La respuesta era correcta? ¿Tenía errores? ¿Se adaptaba a la estructura y la
metodología del proyecto, o hubo que reescribirla?]

Se tomo la respuesta obtenida ya que creo que usa manera mas legible de codigo sin necesidad de tener que necesariamente splitear toda la cadena y verificar dia/mes/anio por separado, ya que si existe un metodo que lo puede hacer no veria la forma de no utilizarlo y eso es lo que nos ayuda en implementar el modulo datetime.strptime. 
Se adapto correctamente ya que no modifico ninguna estructura,metodologia,etcetera. Veniamos realizando las funciones de verificaciones del casi mismo modo en que nos fue enviada la respuesta por la IA, solo que no se pense en el metodo de strptime ya que no se conocia.

**Aprendizaje:** [qué entendió mejor el equipo a partir de esta interacción.
¿Qué concepto quedó más claro? ¿Qué se haría distinto la próxima vez?]
De esta interaccion quedo mas claro el concepto de datetime y su metodo strptime el cual nos sirve para validar un fecha en un formato pedido. Tal vez la proxima vez podriamos investigar metodo por metodo de alguna biblioteca que se necesite utilizar, no vimos necesario no pedir el codigo ya que es basicamente como veniamos implementando nuestras funciones.

### Entrada 3 — [14/06] — [Fernandez Ivan]

**Contexto:** [en qué parte del proyecto se estaba trabajando y qué se
necesitaba resolver.]
Se necesitaban pruebas independientes para el modulo de movimientos, se estaba cerca de la fecha de entrega de la semana 14.

**Herramienta utilizada:** [qué herramienta de IA generativa.] 
Claude Code

**Prompt exacto:**

```
Dado el archivo de movimientos podrias ayudarme a generar unas pruebas independientes  para dicho modulo.
Sencillas que cumplan lo pedido y con una politica de stock que es la siguiente
stock = 50, minimo = 10, salida = 45
nuevo_stock = 50 - 45 = 5
5 < 10 , se registra el movimiento, y se advierte al usuario
```

**Respuesta obtenida:** [la respuesta, o su esencia si fue muy extensa. Si fue
código, puede incluirse aquí o resumirse.] Basicamente dio las pruebas del modulo movimientos.py.

**Análisis crítico:** [qué se tomó de la respuesta y qué se descartó, y por qué.
¿La respuesta era correcta? ¿Tenía errores? ¿Se adaptaba a la estructura y la
metodología del proyecto, o hubo que reescribirla?] Se comprobo que funcionen correctamente y se implemento.

**Aprendizaje:** [qué entendió mejor el equipo a partir de esta interacción.
¿Qué concepto quedó más claro? ¿Qué se haría distinto la próxima vez?] Sirve si no hay imaginacion para tipos de pruebas especificas y sencillas de cada modulo, se tendria en cuenta si se esta corto de tiempo o para comprobar que algun modulo funcione correctamente.

No creo necesario explayar demasiado las respuestas de este uso ya que fue meramente para pruebas de un modulo.


### Entrada 4 - [15/06] - [Villar Manuel]

**Contexto:** [en qué parte del proyecto se estaba trabajando y qué se
necesitaba resolver.]
Se necesitaban pruebas para el modulo main.py

**Herramienta utilizada:** [qué herramienta de IA generativa.]
Claude Code

**Prompt exacto:**

```
Creame el bloque if __name__ == "__main__" para realizar pruebas en el modulo main.py
```

**Respuesta obtenida:** [la respuesta, o su esencia si fue muy extensa. Si fue
código, puede incluirse aquí o resumirse.] Basicamente dio las pruebas del modulo main.py

**Análisis crítico:** [qué se tomó de la respuesta y qué se descartó, y por qué.
¿La respuesta era correcta? ¿Tenía errores? ¿Se adaptaba a la estructura y la
metodología del proyecto, o hubo que reescribirla?] Se comprobo que funcionen correctamente y se implemento.

**Aprendizaje:** [qué entendió mejor el equipo a partir de esta interacción.
¿Qué concepto quedó más claro? ¿Qué se haría distinto la próxima vez?] Sirve si no hay imaginacion para tipos de pruebas especificas y sencillas de cada modulo, se tendria en cuenta si>

Considero que se utilizo de manera correcta unicamente para realizar pruebas.
