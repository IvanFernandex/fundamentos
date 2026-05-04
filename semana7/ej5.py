"""Enunciado
Implementar tres funciones recursivas clásicas y analizar su comportamiento en la pila de
ejecución:
(a) factorial(n): retorna n! para n ≥ 0 (caso base: 0! = 1).
(b) suma_lista(datos): retorna la suma de los elementos de una lista (caso base:
lista vacía → 0).
(c) potencia(base, exponente): retorna base^exponente para exponente ≥ 0
(caso base: exponente == 0 → 1).
Para cada función:
1. Documentar el caso base y el caso recursivo en la docstring.
2. Agregar una instrucción print al inicio de cada invocación que muestre el nivel de
profundidad y los argumentos recibidos.
3. Verificar la correctitud con al menos tres casos de prueba incluyendo el caso base.
4. Ejecutar factorial(4) y suma_lista([3, 7, 2, 5]) en Python Tutor y
observar la pila de frames.
5. Trazar manualmente la pila de ejecución de potencia(2, 4) en una tabla.
Ejemplo de salida esperada para factorial(4):
factorial(4) — profundidad 1
factorial(3) — profundidad 2
factorial(2) — profundidad 3
factorial(1) — profundidad 4
factorial(0) — profundidad 5 [caso base]"""
#a)
def factorial(n, profundidad=1):
    """Calcula el factorial de n.
    Pre: n >= 0
    Post: Devuelve n! (n factorial)
    Caso base: factorial(0) = 1
    Caso recursivo: factorial(n) = n * factorial(n - 1) para n > 0
    """
    print("  " * profundidad + f"factorial({n}) — profundidad {profundidad}")
    if n == 0:
        print("  " * profundidad + "[caso base]")
        return 1

    return n * factorial(n - 1, profundidad + 1)
    
#b)
def suma_lista(datos, profundidad=1):
    """Suma los elementos de una lista recursivamente.
    Pre: datos es una lista
    Post: retorna la suma de sus elementos
    Caso base: suma_lista([]) = 0
    Caso recursivo: suma_lista(datos) = datos[0] + suma_lista(datos[1:]) para datos no vacía
    """
    print("  " * profundidad + f"suma_lista({datos}) — profundidad {profundidad}")
    if datos == []:
        print("  " * profundidad + "[caso base]")
        return 0

    return datos[0] + suma_lista(datos[1:], profundidad + 1)

#c)
def potencia(base, exponente, profundidad=1):
    """Calcula la base del exponente usando recursión.
    Pre: exponente >= 0
    Post: retorna base^exponente usando recursion"""
    print(" " * profundidad + f"potencia({base}, {exponente}) — profundidad {profundidad}")
    if exponente == 0:
        print(" " * profundidad + "[caso base]")
        return 1
    else:
        return base * potencia(base, exponente - 1, profundidad + 1)
    
def main():
    print("=== Factorial ===")
    print("Resultado:", factorial(4))

    print("=== Suma_lista ===")
    print("Resultado:", suma_lista([3, 7, 2, 5]))

    print("=== Potencia ===")
    print("Resultado:", potencia(2, 4))
main()
