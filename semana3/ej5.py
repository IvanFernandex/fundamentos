"""Escribir un programa en Python que solicite al usuario un número entero positivo n (n ≥ 2)y determine si es un número perfecto, deficiente o abundante, según la relación entre n y
la suma de sus divisores propios. El programa debe mostrar los divisores propios
encontrados, su suma y la clasificación."""

solicitar_numero = input("Ingrese un numero entero positivo mayor o igual a 2: ")
numero = int(solicitar_numero)

if numero < 2:
    print("Error: El numero debe ser mayor o igual a 2.")
else:
    suma_divisores = 0
    for divisor in range(1, numero):  # Divisores propios van desde 1 hasta numero-1
        if numero % divisor == 0:
            suma_divisores += divisor
            print(f"Divisor propio encontrado: {divisor}")
    print(f"Suma de divisores propios: {suma_divisores}")

    if suma_divisores == numero:
        print(f"{numero} es un número perfecto.")
    elif suma_divisores < numero:
        print(f"{numero} es un número deficiente.")
    else:
        print(f"{numero} es un número abundante.")