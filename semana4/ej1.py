"""Retomar la solución del Problema 3 de la Semana 2 (conversión de un entero positivo entre 1 y 3999 a números
romanos) y refactorizarla aplicando funciones. El programa debe mantener exactamente el mismo comportamiento observable (mismas entradas, mismas salidas), pero su estructura interna debe ser modular.

Requisitos de modularización
El diseño debe incluir, como mínimo, las siguientes funciones:
digito_a_romano(digito, uno, cinco, diez): recibe un dígito (0-9) y los tres símbolos romanos correspondientes
a su posición (por ejemplo, para las decenas: uno='X', cinco='L', diez='C'). Retorna la cadena romana
equivalente. Esta función encapsula la lógica de los nueve casos (0-9) que se repetía cuatro veces en la versión
original.
decimal_a_romano(numero): recibe un entero entre 1 y 3999, extrae los dígitos posicionales (millares,
centenas, decenas, unidades), invoca digito_a_romano para cada posición con los símbolos apropiados, y
retorna la cadena romana completa.
validar_rango(numero, minimo, maximo): retorna True si el número está en el rango [minimo, maximo], False
en caso contrario. Función reutilizable para validación de entradas."""

def digito_a_romano(digito, uno, cinco, diez):
    if digito == 0:
        return ""
    elif digito == 1:
        return uno
    elif digito == 2:
        return uno * 2
    elif digito == 3:
        return uno * 3
    elif digito == 4:
        return uno + cinco
    elif digito == 5:
        return cinco
    elif digito == 6:
        return cinco + uno
    elif digito == 7:
        return cinco + uno * 2
    elif digito == 8:
        return cinco + uno * 3
    elif digito == 9:
        return uno + diez

def decimal_a_romano(numero):
    millares = numero // 1000
    centenas = (numero % 1000) // 100
    decenas = (numero % 100) // 10
    unidades = numero % 10

    romano_millares = digito_a_romano(millares, 'M', '', '')
    romano_centenas = digito_a_romano(centenas, 'C', 'D', 'M')
    romano_decenas = digito_a_romano(decenas, 'X', 'L', 'C')
    romano_unidades = digito_a_romano(unidades, 'I', 'V', 'X')

    return romano_millares + romano_centenas + romano_decenas + romano_unidades

def validar_rango(numero, minimo, maximo):
    return minimo <= numero <= maximo

def main():
    numero = int(input("Ingrese un número entero positivo entre 1 y 3999: "))
    if validar_rango(numero, 1, 3999):
        romano = decimal_a_romano(numero)
        print(f"El número {numero} en números romanos es: {romano}")
    else:
        print("Número fuera de rango. Por favor, ingrese un número entre 1 y 3999.")

main()