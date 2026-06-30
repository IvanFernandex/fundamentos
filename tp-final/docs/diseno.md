# Diseño del algoritmo

> Documento de diseño del proyecto final. Sigue las fases de Pólya a escala de
> proyecto. Se construye principalmente en la Semana 13 (Análisis y diseño) y se
> ajusta a medida que el proyecto avanza.
>
> Completar las secciones marcadas con `[completar]` y eliminar este bloque.

---

## 1. Análisis del problema

### 1.1. Enunciado

Se solicita la creacion de un sistema de gestión de inventario para un depósito. El sistema debe permitir registrar productos con su stock disponible y stock mínimo, ademas debe registrar movimientos de entrada y salida de mercadería con persistencia en un historial y detectar automáticamente los productos que requieren reposición (cuyo stock es menor al mínimo). El sistema lista el inventario completo ordenado por descripcion y permite consultar el historial de movimientos de un producto dado por su codigo.
Como extension opcional elegida, ante una salida de stock, el sistema aplica la siguiente politca:
- Se rechaza únicamente si la cantidad excede el stock disponible.
- Si la salida es válida pero deja el stock por debajo del mínimo, el movimiento **se registra** y se emite una advertencia al usuario. El producto quedará visible en el reporte de productos a reponer.

Luego de leer la ampliacion del proyecto, se decidio implementar una funcionalidad la cual al hacer un alta de producto se registre su stock inicial con un movimiento el cual es de apertura y eso mismo nos sirver para verificar la consistencia del stock almacenado en nuestro archivo maestro y el historial de movimientos. Esto lo podemos ver en la implementacion de `guardar_apertura` en el modulo de `archivos.py` 

### 1.2. Datos de entrada

|       Dato         |         Tipo         |   Restricciones   |  Medio  |
| ------------------ | -------------------- | ----------------- | ------- |
| Código de producto | Entero positivo| Único | Teclado |
| Descripción | Cadena | No vacía | Teclado |
| Stock actual | Entero | Mayor o igual a 0 | Teclado |
| Stock mínimo | Entero | Mayor o igual a 0 | Teclado |
| Precio unitario | Real | Mayor a 0 | Teclado |
| Tipo de movimiento | Carácter | 'E' [Entrada] o 'S' [Salida] | Teclado |
| Cantidad | Entero | Positivo | Teclado |
| Fecha | Cadena | Formato AAAA-MM-DD| Teclado |

### 1.3. Resultados esperados

* Menú de consola que guía al usuario con todas las operaciones disponibles.
* Confirmaciones y mensajes de error claros ante cada operación: confirmaciones de altas, movimiento
registrados correctamente, operación rechazadas por stock insuficiente, productos no encontrados, código invalido.
* Advertencia cuando un movimiento válido deja el stock por debajo del mínimo.
* Listado del inventario en forma de tabla: Ordenada por descripción, con código, descripción, stock
actual, stock mínimo, precio unitario y una marca de reposición cuando corresponda
* Reporte de productos a reponer: lista de productos los cuales su stock es menor stock minimo y se deben reponer
* Historial de movimientos de un producto: lista de todos los movimientos de un producto dado su codigo.

### 1.4. Casos de análisis

> Construir casos exhaustivos: escenarios normales, casos límite y casos
> extremos. Cada caso indica una entrada concreta y la salida que debería
> producir. Estos casos se usan luego para probar el programa.

| # | Tipo    | Entrada | Salida esperada | Observaciones |
|---|----------|----------|----------|----------|
| 1 | Normal | Alta de un producto con stock=50, stock_minimo=10 | Se registra correctamente; se agrega movimiento de apertura 'A' al historial | Operación válida |
| 2 | Normal | Producto con 20 unidades de stock y una entrada de 10 unidades | Se registra el movimiento y se actualiza el stock a 30 | Operación válida |
| 3 | Normal | Producto con 30 unidades de stock, stock minimo de 10 y una salida de 5 | Se registra el movimiento y se actualiza el stock a 25 | Operación válida |
| 4 | Límite | Producto con 10 unidades de stock y stock mínimo 10 | No aparece en productos a reponer | No se registra como producto a reponer |
| 5 | Límite | Producto con stock 9 y stock mínimo 10 | Aparece en productos a reponer | Esta debajo del minimo |
| 6 | Extremo | Salida de stock de producto mayor al stock actual | Operación rechazada y sin registrar movimiento | Stock insuficiente |
| 7 | Extremo | Inventario vacío | Se informa que el listado esta vacio | Sin errores |
| 8 | Extremo | Consulta de producto inexistente | Mensaje de error | Código no registrado |
| 9 | Extremo | Alta con codigo ya existente | Se rechaza el alta  | Operacion invalida |


---

## 2. Diseño de la solución

### 2.1. Estrategia general


Se buscara resolver el problema a traves de formas iterativas interactuando con un menu, el usuario opera en este hasta que eligue salir, los recorridos sobre el historial (para calcular stock, generar reportes o verificar stock) son todos bucles lineales sobre el archivo de movimientos por ende no se requiere recursividad ni backtracking porque el problema no tiene estructura combinatoria ni subproblemas que se reduzcan a sí mismos, por esta misma razon decidimos utilizar metodos iterativos.

Para el ordenamiento del inventario se implementa un algoritmo de ordenamiento el cual es insercion, que tiene complejidad temporal O(n²) , decidimos utilizar el mismo ya que la cantidad de productos no suele ser relativamente grande y los listados de los productos se generan de manera ocasional y no permanentemente, por lo que no resulta necesario incorporar algoritmos más complejos.

Se utilizaran dos tipos de informacion persistente(Binario):

**Un archivo principal de productos** `inventario.bin`

**Un archivo de historial de movimientos** `movimientos.bin`

Se utilizan estos mismos ya que son la herramienta adecueda a nuestro parecer para la persistencia de archivos y el espacio que ocupan.

### 2.2. Estructuras de datos

**Archivo de productos:**

Sera un registro de longitud fija donde cada uno de ellos almacenara el estado actual de cada producto, se decide utilizar esta estructura para que los datos persistan y poder acceder a ellos rapidamente a traves de su posicion, lo cual nos garantiza un timpo O(1)
* Codigo
* Descripcion
* Stock actual
* Stock Minimo
* Precio unitario

**Archivo de movimientos/transacciones:**

Un registro de longitud fija donde cada uno almacenara una E/S de producto, permitira saber cuando se produjo cada una de ellas y sobre que producto se realizo, los registros siempre se agregaran al final y nunca se sobreescriben
* Codigo de producto
* Tipo de movimiento (Entrada/Salida/Apertura(Alta de productos))
* Cantidad (Ingreso/Egreso de producto)
* Fecha

**Diccionario en memoria de productos:**

Esta estructura nos permite acceder a cualquier producto en tiempo O(1) y evitamos recorrer repetidas veces el archivo de productos durante la ejecucion del programa, nos ayuda para facilitar las consultas sobre productos y stock; cada vez que modificamos algo podemos actualizar el diccionario y el archivo binario para la consistencia.

Se carga el archivo de productos completo en un diccionario cuya clave es el código del producto y cuyo valor es otro diccionario con todos los datos del producto de la forma:
productos[`codigo`] = {
    descripcion,
    stock,
    minimo,
    precio
}

**Diccionario en memoria de índice:**

Se construye esta estructura junto con el diccionario de productos al llamar a cargar_productos() ya que queriamos encontrar una manera para actualizar y/o buscar un producto en el archivo persistente sin necesidad de tener que recorrer registro por registro.
Su propósito es distinto al de productos: no almacena los datos del artículo sino la posición física de su registro en el archivo. La clave es el código como string y el valor es el número de registro (entero) es decir su posicion.
indice[codigo_str] = posicion_registro

**Lista temporal de productos:**
Elegimos esta estructura ya que principalmente todos los algoritmos de ordenamiento operan naturalmente sobre listas y nos ayudaria a hacer todos los listados de los productos y sus dichos reportes. Ademas nos ayuda a evitar duplicar la informacion almacenada en los archivos

* Listados.
* Reportes.
* Ordenamiento.


### 2.3. Descomposición modular


| Función                 | Subtarea que resuelve                                 | A cargo de  |
|--------------           |---------------------------                            |-------------|
| mostrar_menu()          | Mostrar al usuario el menu con las opciones           | Manuel Villar |
| inicializar_archivos()  | Crea dos archivos binarios vacios                     | Ivan Fernandez |
| cargar_productos()      | Crea dos diccionario con el inventario y sus indices cargados           | Ivan Fernandez |
| guardar_producto(codigo, datos,indices)      | Guarda el producto en el archivo binario inventario   | Ivan Fernandez |
| actualizar_producto(codigo, datos,indices)   | Actualiza el producto en el archivo                   | Ivan Fernandez |
| guardar_movimiento(codigo,tipo,cantidad,fecha)    | Añade el movimiento en el archivo binario movimientos | Manuel Villar e Ivan Fernandez |
| ingresar_opcion_valida() | Valida la opcion elegida en el menu para evitar errores | Manuel Villar |
| leer_codigo()           | Valida el codigo brindado de un producto              | Manuel Villar |
| pedir_stock()           | Valida que el stock sea un numero valido              | Manuel Villar |
| pedir_cantidad()        | Valida que la cantidad sea un numero valido           | Manuel Villar |
| pedir_descripcion()     | Valida que se de una descripcion no vacía             | Manuel Villar |
| ingresar_movimiento()    | Valida que el movimiento ingresado sea E o S          | Ivan Fernandez |
| pedir_fecha()           | Valida el formato brindado de la fecha                | Ivan Fernandez |
| alta_producto(productos,indices)         | Da de alta un producto en el diccionario y archivo y registra la apertura en el log    | Ivan Fernandez |
| registrar_movimiento(productos,indices)  | Registra un movimiento en el archivo binario si es valido y actualiza el stock en el diccionario |Manuel Villar e Ivan Fernandez |
| mostrar_inventario(productos)    | Muestra el inventario ordenado por descripcion e informa si esta vacio            | Ivan Fernandez |
| mostrar_productos_a_reponer(productos) | Informa al usuario los productos que debe reponer   | Ivan Fernandez |
| ordenar_por_descripcion(lista_productos) | Ordena los productos basados en su descripcion      | Ivan Fernandez |
| mostrar_movimientos(productos) | Dado un producto muestra el total de E/S del mismo      | Manuel Villar e Ivan Fernandez |
| guardar_apertura(codigo, stock_inicial, fecha) | Registra el stock inicial como movimiento tipo 'A' en el historial al dar de alta un producto | Ivan Fernandez, Manuel Villar |
| pedir_stock_minimo()    | Valida que el stock minimo sea un numero entero >= 0       | Ivan Fernandez |
| convertir_dic_lista(diccionario) | Convierte el diccionario de productos en una lista temporal para ordenamiento | Ivan Fernandez |

### 2.4. Pseudocódigo

> Diseño del algoritmo en pseudocódigo (en español) o en literate programming,
> antes de codificar. El pseudocódigo permite razonar la solución sin la
> distracción de la sintaxis.

```
================================
Modulo main.py

mostrar_menu()
mostrar:
    1) Dar alta producto
    2) Registrar movimiento
    3) Listar inventario ordenado
    4) Ver productos a reponer
    5) Consultar historial de movimientos #Funcionalidad de ver movimientos de un producto
    6) Salir


inicializar_archivos()
productos,indices <-- cargar_productos()
repetir
    mostrar_menu()
    opcion <-- ingresar_opcion()
        si opcion == 1: alta_producto(productos,indices)
        si opcion== 2: registrar_movimiento(productos,indices)
        si opcion == 3: listar_inventario(productos)
        si opcion == 4: listar_productos_a_reponer(productos)
        si opcion == 5: ver_historial_movimientos() #Falta implementar la funcionalidad en el modulo de movimientos
        si opcion == 6: salir

hacer hasta opcion = 6
================================
Modulo archivos.py (guarda e inicializa los archivos para no hacerlo con productos.py y que solo el modulo de productos de altas y los guarde)

inicializar_archivos()

    si productos.bin no existe en la ruta actual
        crear productos.bin en modo escritura binaria
    fin

    si movimientos.bin no existe en la ruta actual
        crear movimientos.bin en modo escritura binaria
    fin

cargar_productos()
    abrir el archivo de productos para cerrar luego de utilizarlo
    
    mientras existan registros
        leer registro
        desempaquetamos el registro
        guardamos el producto con su codigo, descripcion, stock_actual, stock_minimo y precio
    fin mientras

    devolver diccionario de productos y diccionario de indices

guardar_producto(codigo,datos,indices)
    empaquetar registro con los datos
    calculamos la posicion del registro con el total de indices
    abrimos el archivo producto en modo de cierre luego de utilizarlo
    posicionarse al final con seek
    escribir registro
    actualizamos el diccionario de indices con la posicion del nuevo registro

guardar_apertura(codigo, stock_inicial, fecha)
    codigo_str <-- str(codigo)
    empaquetar (codigo_str, 'A', stock_inicial, fecha) con struct.pack
    abrir movimientos.bin en modo append binario
    escribir registro


actualizar_producto(codigo,datos,indices)
    localizamos la posicion del registro segun su indice
    sobrescribir registro con los datos empaquetados

    cerrar 
    
guardar_movimiento(codigo,tipo,cantidad,fecha)

    empaquetar movimiento

    abrir movimientos.bin en modo de cierro luego de utilizarlo
    posicionarse al final
    escribir movimiento

================================
Modulo validaciones.py

ingresar_opcion_valida()
    solicitar opcion

    mientras opcion no sea una opcion valida (1,6)
        informar error
        solicitar nuevamente

    fin 
    devolver opcion

leer_codigo()
    solicitar codigo

    mientras codigo <= 0
        informar error
        solicitar nuevamente
    fin 
    devolver codigo

pedir_stock() #se reutiliza para validar stock_minimo
    solicitar stock

    mientras stock < 0
        informar error
        solicitar nuevamente
    
    fin 
    devolver stock

pedir_cantidad()
    solicitar cantidad
    mientras cantidad <= 0

        informar error
        solicitar nuevamente

    fin 
    devolver cantidad

pedir_descripcion()
    solicitar descripcion
    mientras descripcion esté vacía
        informar error
        solicitar nuevamente

    fin 
    devolver descripcion

validar_movimiento()
    solicitar tipo

    mientras tipo no sea E y tipo no sea S
        informar error
        solicitar nuevamente

    fin 
    devolver tipo

pedir_fecha()
    solicitar fecha
    validar formato
    
    mientras fecha inválida
        informar error
        solicitar nuevamente
    
    fin 
    devolver fecha
================================
Modulo productos.py

alta_producto(productos,indices)
    leemos el codigo 
    si el codigo lo cual antes llevaba O(n)existe en productos
        informamos "Producto ya registrado"
    sino

    pedimos descripcion
    pedimos stock
    pedimos stock_minimo
    pedimos el precio
    pedimos fecha

    creamos un nuevo producto y guardarlo dentro del diccionario usando el código como clave.
    guardar_producto(archivo, codigo,productos[codigo])
    guardar_apertura(codigo,stock,fecha)

    informamos que el producto fue agregado

    fin

mostar_inventario(productos)

    inventario <-- convertir_diccionario_a_lista(productos) #funcion trivial
    si el inventario esta vacio lo informa

    ordenar_por_descripcion(inventario)

    mostrar inventario

mostar_productos_a_reponer(productos)

    declaramos si hay productos para reponercomo negacion
    para cada producto en productos
        si el stock del producto es menor al stock minimo

            mostrar producto e informamos que hay que reponerlo
            declaramos como verdad que si hay productos para reponer

        fin
    fin para

    si al verificar todos los produtctos no hay ninguno

        informamos que no hay ningun producto para reponer

    fin


================================
Modulo movimientos.py

registrar_movimiento(productos, indices) #se debe actualizar el diccionario en memoria tambien

    leemos el codigo

    si el codigo no existe en productos

        informamos que no existe

    sino

    validamos si es un movimiento de entrada/salida
    cantidad de ingreso/egreso
    pedimos la fecha
        si fue una entrada:
            registramos la entrada, actualizamos stock, registramos en archivo de movimientos informamos que se registro la entrada correctamente, se actualiza el stock

        sino (fue salida):
            primero se verifica si tenemos suficiente stock mediante un calculo, si la diferencia entre stock y stock minimo es negativa entonces la salida se rechaza por falta de stock, si no hay stock suficiente para cumplir la orden tambien se rechaza y si hay suficiente para el movimiento la salida se aprueba y se registra en el archivo  ademas de actualizar el stock. 
            es decir si cantidad > stock_actual se rechaza la operación
        fin

    fin

mostrar_movimientos(productos) #Falta desarrollar, nos dimos cuenta tarde de la ausencia de esta funcionalidad.
    leemos el codigo <-- pedir_codigo()
    verificamos que este en la lista de productos

    creamos una lista para el historial
    abrimos el archivo de movimientos
    vemos todos los registros de ese producto
    desmpaquetamos los datos
    y lo agregamos al historial

    informamos si el historial esta vacio
        no hay movimientos para ese producto
    
    informamos el historial si hay registro de movimientos

================================
Modulo ordenamientos.py

ordenar_por_descripcion(lista_productos)

    aplicar algoritmo de inserción
    comparar por descripcion

    devolver lista ordenada

================================


```

---

## 3. Análisis de complejidad


En nuestra solucion diseñana la complejidad temporal es la siguiente:
* Alta de productos: Se realiza en tiempo de complejidad O(1), se agrega al final del registro de inventario.
* Búsqueda de productos: Al realizar la busqueda de un producto mediante un diccionario en memoria cuya clave es el codigo del producto, conlleva una **complejidad temporal O(1)**
* Ordenamiento de inventario: En nuestro diseño generamos un listado que se convierte el diccionario a una lista y luego se aplica un ordenamiento por inserción, lo cual lleva una complejidad temporal O(n²) en los peores casos.
* Registro de movimientos: En el cual la búsqueda del producto se realiza mediante el diccionario, la actualización del stock es constante y la escritura del movimiento se realiza al final del archivo y su complejidad temporal sera O(1)
* Actualizacion de un producto: Realizamos la actualizacion de un producto mediante la nueva implementacion de un diccionario de indices con el codigo de un producto y su posicion la cual antes nos llevaba un tiempo O(n) ahora esta estructura nos garantiza una complejidad O(1); Antes recorriendo registro por registro hasta encontrar el codigo del producto pedido, ahora ya no es necesario.
* **Registro de apertura**: O(1). `guardar_apertura` escribe un único registro al final de `movimientos.bin` en modo append. (Funcionalidad agregada luego de ver ampliacion del proyecto)
* Consulta del historial de un producto: Se recorre el archivo completo de forma secuencial filtrando por código. Es el punto de mayor costo lineal del sistema con complejidad O(M) donde M es la cantidad de movimientos en el archivo.


---

## 4. Revisión entre pares

> Espacio para registrar la devolución recibida en la revisión entre pares de
> la Semana 13 y los ajustes que se hicieron al diseño a partir de ella.

[completar.]

---

*Proyecto Final Integrador · Fundamentos de Programación · FIUBA*