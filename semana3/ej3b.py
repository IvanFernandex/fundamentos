"""Escribir un programa en Python que solicite al usuario un número entero positivo n (n ≥ 1)
y calcule y muestre:
(b) La sucesión de números malabaristas (juggler sequence) desde n hasta llegar a 1, indicando igualmente la cantidad de pasos y el valor máximo alcanzado.
"""

"""Sucesion de numeros malabaristas
Si n es par: n → ⌊n^(1/2)⌋ (raíz cuadrada, truncada)
Si n es impar: n → ⌊n^(3/2)⌋ (n elevado a 3/2, truncado)
Casos de prueba:
- n = 6 -> Malabarista -> 2 pasos, máximo 6;
- n = 9 -> Malabarista -> 7 pasos, máximo 140"""

"""Análisis: Una entrada int (n ≥ 1). Para cada sucesión: iterar hasta llegar a 1, contando pasos
y rastreando el máximo. Caso especial: n = 1 (cero pasos).
"""

numero_str = input("Ingrese un numero entero: ")
numero_int = int(numero_str)
pasos = 0
maximo = numero_int

if numero_int < 1:
    print("Error: EL numero es menor que 1")
else:
    print(numero_int, end="")
    while numero_int != 1:
        #Veo que el numero sea par
        if numero_int % 2 == 0: #par
            numero_int *= 0.5
        else:
            numero_int *= 1.5
        pasos += 1
        if numero_int > maximo:
            maximo = numero_int
    print(f"\nCantidad de pasos: {pasos}. Altitud máxima: {maximo}.")
    