"""Enunciado
Escribir un programa en Python que solicite al usuario una fecha en formato AAAAMMDD (un único entero, como los producidos en el Problema 3 de la Semana 1), verifique que corresponda a una fecha válida a partir de la vigencia del Calendario Gregoriano (15 de octubre de 1582), y determine a qué día de la semana corresponde, mostrándolo por su nombre en español."""

# Sección Declarativa
# 
# Descripción: Calcula el día de la semana para una fecha dada (posterior al 15/10/1582) 
# usando la Congruencia de Zeller.
#
# Casos de prueba:
# - 15821015 -> Viernes (Primer día del Gregoriano)
# - 20250313 -> Jueves (Fecha de referencia)
# - 20000101 -> Sábado (Inicio de milenio)
# - 19691020 -> Lunes (Llegada a la Luna)
# - 20240229 -> Jueves (Bisiesto)
#
# Recursos:
# - fecha (int): Entrada del usuario en formato AAAAMMDD.
# - anio, mes, dia (int): Componentes de la fecha.
# - K, J, h (int): Variables intermedias de Zeller.
# - nombre_dia (str): Día de la semana resultante.
#Seccion Algoritmica 

#1) Prologo

print("--- Determinacion del dia de la semana (Zeller) ---")
fecha = int(input("Ingrese una fecha válida (AAAAMMDD, posterior a 15821015): "))
#2)Desarrollo
#Extraccion de los componentes de la fecha valida
anio = fecha // 10000
mes = (fecha // 100) % 100
dia = fecha % 100

#Ajuste de zeller para Enero y febrero
if mes <= 2:
    mes = mes + 12
    anio = anio - 1
#Variables Intermedias 
K = anio % 100 #Año dentro del siglo
J = anio // 100 #Siglo
#Formula zeller
formula_zeller = (dia + (13 * (mes + 1)) // 5 + K + K // 4 + J // 4 - 2 * J) % 7

#Resultados

if formula_zeller == 0:
    nombre_dia = "Sabado"
elif formula_zeller == 1:
    nombre_dia = "Domingo"
elif formula_zeller == 2:
    nombre_dia = "Lunes"
elif formula_zeller == 3:
    nombre_dia = "Martes"
elif formula_zeller == 4:
    nombre_dia = "Miercoles"
elif formula_zeller == 5:
    nombre_dia = "Jueves"
elif formula_zeller == 6:
    nombre_dia = "Viernes"

#Epilogo
print(f"La fecha ingresada es: {nombre_dia}")
