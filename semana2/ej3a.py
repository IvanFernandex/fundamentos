"""Escribir un programa en Python que solicite al usuario un número entero positivo entre 1 y
3999 y lo convierta a su representación en números romanos. El programa debe validar que el
número esté en el rango válido y mostrar el resultado."""

# Sección Declarativa
"""
Descripcion: Convierte un numero (1-3999) a su representacion en numeros romanos

Casos de prueba:
- 4 -> IV
- 42 -> XLII
- 1582 -> MDLXXXII
- 2025 -> MMXXV
- 3999 -> MMMCMXCIX

Recursos:
- numero (int): Entrada a convertir.
- millares, centenas, decenas, unidades (int): Dígitos extraídos.
- romano (str): Resultado acumulado mediante concatenación.
"""
# 1) Prólogo
print("--- Conversor a Números Romanos (Descendente Optimizado) ---")
numero = int(input("Ingrese un número entre 1 y 3999: "))

if numero < 1 or numero > 3999:
    print("Ingrese un numero valido.")
else:
    # 2)Desarrollo
    millares = numero // 1000
    centenas = (numero % 1000) // 100
    decenas = (numero % 100) // 10
    unidades = numero % 10

    romano = ""
    # Evaluacion de millares
    if millares > 0:
        romano = romano + (millares * "M")
    # Evaluacion de centenas
    if 0 < centenas < 4:
        romano = romano + (centenas * "C")
    elif 5 < centenas < 9:
        romano += "D" + ((centenas - 5) * "C")
    elif centenas == 4:
        romano += "CD"
    elif centenas == 5:
        romano += "D"
    elif centenas == 9:
        romano += "CM"
    # Evaluación de decenas
    if 0 < decenas < 4:
        romano = romano + (decenas * "X")
    elif 5 < decenas < 9:
        romano = romano + "L" + ((decenas - 5) * "X")
    elif decenas == 4:
        romano = romano + "XL"
    elif decenas == 5:
        romano = romano + "L"
    elif decenas == 9:
        romano = romano + "XC"
    #Evaluacion de Unidades
    if 0 < unidades < 4:
        romano = romano + (unidades * "I")
    elif 5 < unidades < 9:
        romano = romano + "V" + ((unidades - 5) * "I")
    elif unidades == 4:
        romano = romano + "IV"
    elif unidades == 5:
        romano = romano + "V"
    elif unidades == 9:
        romano = romano + "IX"
    
    # 3) Epílogo
    print(f"\nRepresentación en números romanos: {romano}")

input("\nPulse Enter para terminar el programa")