# Dominio B — Gestor de inventario de un depósito
Un sistema que controla el stock de productos de un depósito: registra entradas y salidas de
mercadería, mantiene actualizadas las existencias y alerta sobre los productos que requieren reposición.
## Núcleo obligatorio
* Persistencia de los productos en un archivo binario de registros de longitud fija (código, descripción, cantidad en stock, stock mínimo, precio unitario).
* Registro de movimientos de entrada y de salida de mercadería, cada uno con su efecto sobre el stock del producto correspondiente.
* Índice en memoria (diccionario) para localizar un producto por su código en tiempo O(1).
* Detección de los productos cuyo stock cayó por debajo de su stock mínimo (productos a reponer).
* Listado del inventario ordenado por descripción o por cantidad en stock, con un algoritmo
de ordenamiento implementado por el equipo.
* Menú de consola que articule todas las operaciones.
Extensiones opcionales (elegir al menos una)
* Valorización del inventario: cálculo del valor total del stock (suma de cantidad por precio
de cada producto).
* Historial de movimientos persistente, con consulta de los movimientos de un producto dado.
* Reporte de los productos de mayor rotación a partir del historial de movimientos.
* Registro de una salida que excede el stock disponible: el sistema debe rechazarla o registrar el faltante, según una política definida y documentada por el equipo.
* Estadísticas del depósito: cantidad de productos por rango de precio o por estado de
stock.
---
### Contenidos del curso involucrados
**Archivos binarios y módulo struct (S8); diccionarios como índice (S10); algoritmos de ordenamiento (S6, S12); búsqueda (S5); patrón de recorrido con acumulador para la valorización
(S3, S11); modularización (S4).** 
Casos de análisis de referencia
* **Caso normal**: registrar una entrada de mercadería; verificar que el stock del producto aumenta en la cantidad correspondiente.
* **Caso límite**: registrar una salida que deja el stock exactamente en el mínimo; el producto aún no debe aparecer como «a reponer».
* **Caso límite**: registrar una salida que deja el stock por debajo del mínimo; el producto debe aparecer como «a reponer».
* **Caso extremo**: registrar una salida mayor que el stock disponible; el sistema debe aplicar la política definida sin interrumpirse.

#### **Cota de alcance**
> El proyecto no incluye interfaz gráfica (**la interacción es por consola**), ni base de datos (la persistencia es mediante archivos), ni acceso por red ni integración con sistemas de facturación.