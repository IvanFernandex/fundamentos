"""Enunciado
Implementar un programa modular que busque los primeros k números perfectos (donde k es ingresado por el usuario), verificando la relación con los primos de Mersenne. Para cada número perfecto encontrado, mostrar el número, el primo de Mersenne asociado y el exponente p tal que 2ᵖ - 1 es primo.

Fundamento: Euler demostró que todo número perfecto par tiene la forma 2ᵖ⁻¹ * (2ᵖ - 1), donde 2ᵖ - 1 es un
primo de Mersenne. Por lo tanto, la búsqueda se reduce a: para cada p = 2, 3, 5, 7, 11, ... (primos), verificar si 2ᵖ - 1 es primo; si lo es, 2ᵖ⁻¹ * (2ᵖ - 1) es un número perfecto.

Requisitos de modularización

es_primo(n): retorna True si n es primo. Reutilizable en múltiples contextos.

mersenne(p): retorna el número de Mersenne 2ᵖ - 1 para un exponente p dado.
perfecto_desde_mersenne(p): dado un exponente primo p para el cual mersenne(p) es primo, retorna el número perfecto correspondiente: 2ᵖ⁻¹ * (2ᵖ - 1).

suma_divisores_propios(n): retorna la suma de los divisores propios de n (todos los divisores excepto n mismo). Se usa para verificar que el número perfecto encontrado cumple la definición:
suma_divisores_propios(n) == n."""
def es_primo(num):
    '''Determina si un número entero positivo es primo.

    Precondición:
      num (int): número entero, num >= 1.

    Postcondición / Retorna:
      bool: True si num es primo (divisible solo por 1 y por sí
            mismo), False en caso contrario.
      Por definición, 1 no es primo.
    '''
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def mersenne(p):
    """
    Sección Declarativa
    Descripción: Calcula el número de Mersenne para un exponente p.
    Retorna: (2^p) - 1.
    """
    return (2 ** p) - 1

def perfecto_desde_mersenne(p):
    """
    Sección Declarativa
    Descripción: Calcula el número perfecto a partir de un exponente.
    Precondición: mersenne(p) debe ser primo.
    Retorna: 2^(p-1) * (2^p - 1).
    """
    return (2 ** (p - 1)) * mersenne(p)

def suma_divisores_propios(numero):

    """Sección Declarativa
    Descripción: Calcula la suma de los divisores propios de un número.
    Precondición: numero debe ser un entero positivo.
    Postcondición: La suma de los divisores propios de numero."""
    suma_divisores = 0
    for divisor in range(1, numero):  # Divisores propios van desde 1 hasta numero-1
        if numero % divisor == 0:
            suma_divisores += divisor
            print(f"Divisor propio encontrado: {divisor}")
    print(f"Suma de divisores propios: {suma_divisores}")
    return 

#Programa principal
def main():

    # ==========================================
    # SECCIÓN ALGORÍTMICA
    # ==========================================
    k_perfectos = int(input("Ingrese la cantidad de números perfectos a encontrar: "))
    encontrados = 0
    primos = 2 # Comenzamos con el primer número primo

    while encontrados < k_perfectos:
        if es_primo(primos):
            calculo_mersenne = mersenne(primos)
            if es_primo(calculo_mersenne):
                nuemo_perfecto = perfecto_desde_mersenne(primos)
                econtrados += 1
                print(f"{encontrados:2d}) p: {p:3d} | Mersenne: {m:6d} | Perfecto: {perf:12d} | Verificado: {verificacion}")
main()