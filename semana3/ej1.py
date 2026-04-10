"""Enunciado
Escribir un programa en Python que solicite al usuario dos números enteros (positivos, negativos o cero) y calcule su producto utilizando exclusivamente sumas sucesivas, sin usar el operador *. El programa debe manejar correctamente los signos y mostrar el resultado"""

#Pedir al usuario dos numeros
#Calcular el producto con sumas sucesivas
#Guardar en variables y sumar dos veces
#Determino el signo del producto

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
signo = 1
producto = 0
if num1 < 0 != num2 < 0:
    signo = -1
else:
    signo = 1
#Veo el signo de los numeros
abs_num1 = -num1 if num1 < 0 else num1
abs_num2 = -num2 if num2 < 0 else num2

if abs_num1 < abs_num2:
    #Si el primer numero es menor que el segundo, los intercambio para reducir el numero de sumas
    abs_num1, abs_num2 = abs_num2, abs_num1
for i in range(abs_num2):
    producto += abs_num1
if signo == -1:
    producto = -producto
else:
    producto = producto
print(f"El producto de {num1} y {num2} es: {producto}")