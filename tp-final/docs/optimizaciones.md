# Mejoras y optimizaciones algorítmicas - Fase 3

---

Teniendo en cuenta el documento propuesto por la cátedra para la Semana 15, donde se indica que la mejora típica del Dominio B consiste en "acumular el stock en un diccionario por clave de producto, no recalcular por consulta", esa mejora en nuestro caso no fue necesaria implementarla como un paso en la optimización ya que nuestro en nuestro diseño lo contemplamos desde el inicio, no era necesario recorrer todos los movimientos para ver el stock actual, sino que el mismo se podria actualizar a traves de un diccionario con el producto, como lo planteamos, y actualizarlo alli segun el movimiento.
Lo que nos llevaria a una complejidad O(M) por consulta es decir recorrer todos los movimientos para recalcular el stock lo hacemos directamente en una consulta O(1) a traves de nuestro diccionario de productos

Además, durante el desarrollo del proyecto fuimos capaces de detectar una mejora de optimización adicional gracias a la ayuda de la IA, sabiamos que se podia implementar algo mejor, se encuentra documentado en la seccion 1 de [`docs/registro_ia.md`](docs/registro_ia.md): Nos dimos cuenta que podria haber una manera mejor para encontrar un producto dado su codigo y que no era necesario recorrer todos los registros del archivo de productos para encontrarlo.

Implementamos un diccionario de índices que utiliza como clave el código del producto y como valor la posición de su registro en el archivo `inventario.bin`. De esta forma, al actualizar un producto podemos acceder directamente a su posición en el archivo sin tener que recorrerlo registro por registro hasta encontrarlo. 

---

## Mejora (Durante codigo) - Diccionario de índices para acceso directo al archivo maestro

### Problema detectado

Para actualizar un producto tras un movimiento de entrada o salida,
la versión original recorría el archivo `inventario.bin` registro por registro
hasta encontrar el código buscado. Cada actualización tenía un costo O(n),
donde n es la cantidad de productos en el archivo, creimos que podria haber una mejora para que esto no suceda.

### Solución implementada

Luego de verificar todas las opciones se dicidio agregar un diccionario en memoria llamado `indice` que se construye una
única vez al iniciar el programa, junto con el diccionario de productos, en la función `cargar_productos()`.

```
indice[codigo_str] = posicion_registro
```

La clave es el código del producto como string y el valor es el número de
registro (posición) dentro del archivo. Entonces esta mejora nos serviria para actualizar un producto ya que se consulta su posición en O(1) y se aplica `seek(posicion * TAMAÑO_REGISTRO)` directamente, sin la necesidad de recorrer el archivo.

### Análisis antes/después

| Aspecto | Antes (sin índice) | Después (con índice) |
|---|---|---|
| La busqueda de un producto en el archivo | O(n) - recorrer registro por registro | O(1) - consulta directa al diccionario |
| Actualizar el stock | O(n) - buscar el registro + escribirlo | O(1) - seek directo + escribirlo |

Ademas la construcción del diccionario de indices ocurre dentro de `cargar_productos()`, que ya recorría el archivo completo para construir el diccionario de productos.
Agregar el diccionario índice no agrega una pasada extra al archivo sino que se construye en el mismo recorrido O(n) que ya existía. El único costo adicional es la memoria del diccionario, que es O(n) - proporcional a la cantidad de productos, no a la de movimientos.

### Justificación

Se gasta O(n) de memoria adicional (un diccionario pequeño) para convertir
la operación más frecuente del sistema de O(n) a O(1). No va a ser necesario un acceso costoso al disco, es decir al archivo persistente, ya que si este es de grandes magnitudes perderiamos eficiencia en nuestro programas, es preferible usar mas memoria en el programa.

### Dónde se ve en el código

1. `archivos.py` --> `cargar_productos()`: construye y devuelve `indice` junto con `productos`.
2. `archivos.py` --> `actualizar_producto(codigo, datos, indice)`: usa `indice[codigo_str]`
3. `archivos.py` --> `guardar_producto(codigo, datos, indice)`: registra la posición del nuevo producto en el índice.
4. `main.py` --> `main()`: recibe ambos diccionarios de `cargar_productos()` y los pasa a las funciones que los necesitan.
---
