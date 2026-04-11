
#Funciones
"""Requisitos de modularización

campesina_rusa(a, b): recibe dos enteros no negativos y retorna su producto usando el algoritmo descrito.
Utiliza << 1 y >> 1 para duplicar y dividir por 2.

multiplicar(a, b): recibe dos enteros cualesquiera (con signo), determina el signo del resultado, convierte a valores absolutos, invoca campesina_rusa y aplica el signo. Reutiliza la lógica de manejo de signos del Problema 1 de la Semana 3."""

#Algoritmo de descomposicion binaria
"""resultado = 0
mientras b > 0:
si b es impar: resultado = resultado + a
a = a << 1 # duplicar a
b = b >> 1 # mitad entera de b"""

"""
=============================================================================
Sección Declarativa - Programa Principal

Descripción: Multiplica dos números enteros utilizando el algoritmo de la 
campesina rusa (complejidad O(log b)), delegando el manejo de signos y 
la lógica binaria en funciones modulares.

Casos de prueba:
- 13 x 11 -> 143 (Caso normal)
- 3 x 4 -> 12 (Acumula solo cuando b impar)
- 7 x 0 -> 0 (Caso límite)
- -3 x 4 -> -12 (Signo negativo, opera con absolutos)

Recursos del programa principal:
- num1, num2 (int): Factores ingresados por el usuario.
- resultado (int): Producto calculado.
=============================================================================
"""
# ==========================================
# DEFINICIÓN DE FUNCIONES
# ==========================================
#Pre: num1 y num2 deben ser dos numeros enteros no negativo
#Post: retorna el producto de los numero utilizando el algoritmo matematico de la campesina rusa.
def campesina_rusa(num1: int, num2: int) -> int:
    resultado = 0
    while num2 > 0:
        #Para averiguar si num2 es impar sin usar el operador %, basta con saber si el último dígito de su representación binaria es 1 con la condición b & 1 == 1
        if num2 & 1 == 1: #si es impar
            resultado = resultado + num1
        num1 = num1 << 1 #duplica el primer numero con un corrimiento de bits
        num2 = num2 >> 1 #divide por el segundo numero usando corrimiento de bits
    return resultado
#Pre:
#Post: retorna la multiplicacion de dos numeros, convierte a valores absolutos, invoca a campesina_rusa y restaura el signo.
def multiplicar(num1: int, num2: int) -> int:
    #Veo el valor del signo de la multiplicacion
    if num1 < 0 != num2 < 0:
        signo = -1
    else:
        signo = 1
    
    #veo los valores absolutos de los numeros
    if num1 < 0:
        abs_num1 = -num1
    else:
        abs_num1 = num1
    if num2 < 0:
        abs_num2 = -num2
    else:
        abs_num2 = num2

    producto_absoluto = campesina_rusa(abs_num1, abs_num2)

    if signo == -1:
        producto_absoluto * signo
    return producto_absoluto
def main():

    # ==========================================
    # SECCIÓN ALGORÍTMICA
    # ==========================================

    # 1) Prólogo 
    num1 = int(input("Ingrese el primer entero: "))
    num2 = int(input("Ingrese el segundo entero: "))

    # 2) Desarrollo 
    # Se delega toda la responsabilidad del cálculo a la función principal
    resultado = multiplicar(num1, num2)

    # 3) Epílogo 
    print(f"Resultado de {num1} x {num2} = {resultado}")
main()