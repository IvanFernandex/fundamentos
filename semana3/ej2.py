"""Escribir un programa en Python que solicite al usuario un dividendo (entero, cualquier signo)y un divisor (entero, distinto de cero) y calcule el cociente entero y el resto utilizando restas sucesivas, sin usar los operadores // ni %. El programa debe verificar que el divisor no sea cero, manejar correctamente los signos y mostrar cociente y resto."""

#Pedir al usuario el dividendo y el divisor
#Calcular el cociente y el resto con restas sucesivas
#Determinar el signo del cociente
#Mostrar el resultado

#dividendo = divisor * cociente + resto

dividendo = int(input("Ingrese un dividendo: "))
divisor = int(input("Ingrese un divisor distinto de 0: "))

if divisor == 0:
    print("Error:No se puede realizar la operacion.")
else:
    if dividendo < 0 != divisor < 0:
        signo = -1
    else:
        signo = 1
    #Calculamos el signo de los divisores y dividendo
    if dividendo < 0:
        abs_dividendo = -dividendo
    else:
        abs_dividendo = dividendo

    if divisor < 0:
        abs_divisor = -divisor
    else:
        abs_divisor = divisor

    #El cociente se obtiene contando cuántas veces se puede restar el dividendo (|b|) de el divisor (|a|) antes de que el resultado sea menor que el dividendo (|b|)
    #Calculamos el cociente 
    cociente = 0
    resto = abs_dividendo
    while resto >= abs_divisor:
        resto -= abs_divisor
        cociente += 1

    if signo == -1:
        cociente = -cociente
    
    if dividendo < 0:
        resto = -resto
    
    abs_dividendo = abs_divisor * cociente + resto
    print(f"\nCociente: {cociente}")
    print(f"Resto: {resto}")
    
    # Verificamos la identidad fundamental de la división
    identidad = (dividendo == divisor * cociente + resto)
    print(f"Verificación (Dividendo == Divisor * Cociente + Resto): {identidad}")
    input("Pulse Enter para terminar el programa.")