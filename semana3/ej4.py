"""Escribir un programa en Python que solicite al usuario un número entero positivo y determine si es un número feliz. Si lo es, mostrar la sucesión de sumas de cuadrados de dígitos hasta llegar a 1. Si no lo es, mostrar la sucesión hasta detectar el ciclo de 8 términos que caracteriza a los números infelices, e indicar que el número no es feliz."""

"""Descripción: Determina si un número es feliz o infeliz sumando los cuadrados 
de sus dígitos repetidamente. Detecta el ciclo infeliz con el número 4.
Casos de prueba:
- 19 -> Feliz (llega a 1 en 3 iteraciones)
- 2 -> Infeliz (cae en el ciclo del 4)
- 7 -> Feliz
- 4 -> Infeliz inmediato"""

"""La operación clave es la suma de cuadrados de dígitos:
Dado n, extraer dígitos con // y %:
suma = 0
mientras n > 0:
digito = n % 10
suma = suma + digito × digito
n = n // 10"""

numero_str = input("Ingrese un numero entero positivo: ")
numero_int = int(numero_str)

if numero_int <= 0:
    print ("Error: Ingrese un numero entero positivo")
else:
    print(f"Sucesión: {numero_int}", end="")

    while numero_int != 1 and numero_int != 4:
        suma = 0
        temporal = numero_int

        while temporal > 0:
            digito = temporal % 10
            suma = suma + (digito * digito)
            temporal = temporal //10
        
        numero_int = suma
        print(f" -> {numero_int}", end="")

    if numero_int == 1:
        print (f"\nEl numero {numero_str} es feliz.")
    else:
        print (f"\nEl numero {numero_str} no es feliz.")
        



