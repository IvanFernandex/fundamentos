"""Enunciado
Escribir un programa en Python que realice los siguientes experimentos con el módulo struct,
registrando las predicciones antes de ejecutar cada bloque y verificándolas después con len() y
con un volcado hexadecimal manual:
Experimento 1 — Tipos elementales:
(a) Empaquetar el entero 42 con cuatro formatos distintos: 'b' (int8), 'h' (int16), 'i' (int32),
'q' (int64). Predecir antes de ejecutar: ¿cuántos bytes ocupa cada uno? Verificar con
len(struct.pack(...)) y mostrar los bytes con .hex().
(b) Empaquetar el flotante 3.14 con 'f' (float32) y con 'd' (float64). Comparar tamaños y bytes
producidos. ¿Qué diferencia se observa entre la representación de 32 y 64 bits?
(c) Empaquetar la cadena b'Ada' con tres formatos: '3s', '10s' y '2s'. Predecir y verificar:
¿qué pasa con la cadena cuando el formato es más corto que la cadena? ¿Y cuando es más
largo? ¿Con qué bytes se rellena?
Experimento 2 — Endianness:
(d) Empaquetar el entero 305419896 (que en hexadecimal es 0x12345678) con tres prefijos:
'<i' (little-endian), '>i' (big-endian) y '!i' (network byte order). Comparar los bytes
producidos. ¿Qué relación hay entre > y !?
(e) Sin usar el prefijo ('i' solo), empaquetar 305419896 y comparar con los resultados de (d).
¿Qué endianness se usa por defecto en esta máquina? Justificar consultando la
documentación del módulo struct.
Experimento 3 — Desempaquetado y validaciones:
(f) Crear bytes_originales = struct.pack('<ii', 100, 200). Desempaquetar con
struct.unpack('<ii', bytes_originales). Verificar que el resultado es la tupla (100, 200).
Luego intentar desempaquetar con '<i' (un solo entero, formato más corto que los datos):
registrar el error y explicar la causa.
(g) Calcular struct.calcsize('<i32s16s40s') y verificar que coincide con la suma manual (4
+ 32 + 16 + 40 = 92 bytes). ¿Por qué es importante usar calcsize en lugar de hardcodear el
número 92 en el programa?"""

import struct
#Experimento 1 — Tipos elementales:

formatos = ['b','h','i','q']

cadenas = ['3s','10s','2s']

for f in formatos:
    paquete = struct.pack(f,42)
    print(f"El valor 42 en formato {f} ocupa {len(paquete)} bytes y su representación hexadecimal es {paquete.hex()}.")

for f in ['f','d']:
    paquete = struct.pack(f,3.14)
    print(f"El valor 3.14 en formato {f} ocupa {len(paquete)} bytes y su representación hexadecimal es {paquete.hex()}.")
    #La diferencia es que en 32 bits se utiliza menos espacio para representar el número, lo que puede llevar a una menor precisión en comparación con 64 bits. 32 bits utiliza 4bytes, mientras que 64 bits utiliza 8 bytes.
"""Predecir y verificar:
¿qué pasa con la cadena cuando el formato es más corto que la cadena? ¿Y cuando es más
largo? ¿Con qué bytes se rellena?"""
for f in cadenas:
    paquete = struct.pack(f, b'Ada')
    print(f"Empaquetar 'Ada' con formato {f} produce {len(paquete)} bytes y su representación hexadecimal es {paquete.hex()}.")
    #Cuando el formato es más corto que la cadena, se trunca la cadena a la longitud especificada. Por ejemplo, con '2s', solo se empaquetan los primeros 2 caracteres de 'Ada', resultando en 'Ad'. Cuando el formato es más largo que la cadena, se rellena con bytes nulos (0x00) hasta alcanzar la longitud especificada.

#Experimento 2 — Endianness:

formatos_endian = ['<i', '>i', '!i']
for f in formatos_endian:
    paquete = struct.pack(f,305419896)
    print(f"El valor 305419896 en formato {f} produce {len(paquete)} bytes y su representación hexadecimal es {paquete.hex()}.")
    #La relación entre > y ! es que ambos indican big-endian, pero ! se utiliza específicamente para el orden de bytes de red (network byte order), que es big-endian. Por lo tanto, >i y !i producirán la misma representación hexadecimal para el mismo valor.

for f in ['i']:
    paquete = struct.pack(f,305419896)
    print(f"El valor 305419896 en formato {f} produce {len(paquete)} bytes y su representación hexadecimal es {paquete.hex()}.")
    #En la mayoría de las arquitecturas modernas, el orden de bytes por defecto es little-endian. Consultando el modulo struct, se puede confirmar que esta maquina utiliza little-endian por defecto.

#Experimento 3 — Desempaquetado y validaciones:
bytes_originales = struct.pack('<ii', 100, 200)
desempaquetado = struct.unpack('<ii', bytes_originales)
print(f"Desempaquetado: {desempaquetado}")
desempaquetado_incorrecto = struct.unpack('<i', bytes_originales)
print(f"Desempaquetado incorrecto: {desempaquetado_incorrecto}")
#El error ocurre ya que se esta intentado desempaquetar un solo entero es decir 4bytes mientras que los datos originales contienen dos enteros, es decir 8 bytes.