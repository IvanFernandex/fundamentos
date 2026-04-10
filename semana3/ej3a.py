"""Escribir un programa en Python que solicite al usuario un número entero positivo n (n ≥ 1)
y calcule y muestre:
(a) La sucesión de granizo (Conjetura de Collatz) desde n hasta llegar a 1, indicando la cantidad de pasos (llamada «tiempo de vuelo») y el valor máximo alcanzado (llamada «altitud máxima»).
"""

"""Sucesion de granizo 
Si n es par: n → n // 2
Si n es impar: n → 3 × n + 1

Casos de prueba:
- n = 6 Collatz -> 8 pasos, máximo 16;
- n = 9 Collatz -> 19 pasos, máximo 52;
"""
"""Análisis: Una entrada int (n ≥ 1). Para cada sucesión: iterar hasta llegar a 1, contando pasos
y rastreando el máximo. Caso especial: n = 1 (cero pasos).
"""

numero_str = input("Ingrese un numero entero: ")
numero_int = int(numero_str)
pasos = 0
maximo = numero_int

if numero_int < 1:
    print("Eror el numero debe ser mayor a 1")
else:
    print(numero_int, end="")
    while numero_int != 1:
        if numero_int % 2 == 0: #Si es par
            numero_int = numero_int // 2
        else: #inpar
            numero_int = 3 * numero_int + 1
        pasos += 1
        if numero_int > maximo:
            maximo = numero_int
        print(f" -> {numero_int}", end="")
    print(f"\nResumen Collatz: {pasos} pasos | Altitud máxima: {maximo}")
    
