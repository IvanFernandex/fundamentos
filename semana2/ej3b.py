"""
Sección Declarativa

Descripción: Convierte un número decimal (1-3999) a romano procesando desde 
las unidades hasta los millares (concatenación a la izquierda), optimizado 
mediante productos de cadenas y rangos condicionales.

Casos de prueba:
- 9 -> IX
- 399 -> CCCXCIX
- 444 -> CDXLIV
- 888 -> DCCCLXXXVIII

Recursos:
- numero (int): Entrada y variable mutada para extraer dígitos.
- unidades, decenas, centenas, millares (int): Dígitos extraídos progresivamente.
- romano (str): Resultado acumulado mediante concatenación.
- equivalencia (str): Valor parcial de cada posición temporal.
"""

# Sección Algorítmica

# 1) Prólogo
print("--- Conversor a Números Romanos (Ascendente Optimizado) ---")
numero = int(input("\nIngrese un número entre 1 y 3999: "))

if numero < 1 or numero > 3999:
    print("Error: Número fuera de rango válido.")
else:
    # 2) Desarrollo
    romano = ""
    # === Unidades ===
    unidades = numero % 10
    numero = numero // 10
    equivalencia = ""
    
    if 0 < unidades < 4:
        equivalencia = unidades * "I"
    elif 5 < unidades < 9:
        equivalencia = "V" + ((unidades - 5) * "I")
    elif unidades == 4:
        equivalencia = "IV"
    elif unidades == 5:
        equivalencia = "V"
    elif unidades == 9:
        equivalencia = "IX"
    # Las condiciones se ordenan de mayor o igual a menor probabilidad de que se cumplan (eficiencia)  
    romano = equivalencia + romano  # Se antepone al resultado global

    # === Decenas ===
    decenas = numero % 10
    numero = numero // 10
    equivalencia = ""
    
    if 0 < decenas < 4:
        equivalencia = decenas * "X"
    elif 5 < decenas < 9:
        equivalencia = "L" + ((decenas - 5) * "X")
    elif decenas == 4:
        equivalencia = "XL"
    elif decenas == 5:
        equivalencia = "L"
    elif decenas == 9:
        equivalencia = "XC"
        
    romano = equivalencia + romano

    # === Centenas ===
    centenas = numero % 10
    numero = numero // 10
    equivalencia = ""
    
    if 0 < centenas < 4:
        equivalencia = centenas * "C"
    elif 5 < centenas < 9:
        equivalencia = "D" + ((centenas - 5) * "C")
    elif centenas == 4:
        equivalencia = "CD"
    elif centenas == 5:
        equivalencia = "D"
    elif centenas == 9:
        equivalencia = "CM"
        
    romano = equivalencia + romano

    # === Millares ===
    millares = numero % 10
    equivalencia = ""
    
    if millares > 0:
        equivalencia = millares * "M"
        
    romano = equivalencia + romano

    # 3) Epílogo
    print(f"\nRepresentación en números romanos: {romano}")

input("\nPulse Enter para terminar el programa")
