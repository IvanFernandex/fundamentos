"""Escribir un programa en Python que solicite al usuario dos fechas en formato AAAAMMDD
(enteros), determine cuál es la mayor y cuál la menor, y calcule la diferencia expresada en
años, meses y días. Por ejemplo, la diferencia entre el 15/01/2023 y el 20/03/2025 es 2 años,
2 meses y 5 días. El programa debe mostrar el resultado en formato legible."""

# Sección Declarativa
"""
Descripcion: Calcula la diferencia extacta en años, meses y dias entre dos fechas.
Las fechas se ingresan como números enteros en formato AAAAMMDD.

Versión 1: se descomponen ambas fechas

Casos de prueba:
- Caso 1 (Préstamo de días): Fecha 1: 20230515, Fecha 2: 20240310 
  -> Diferencia: 9 meses, 24 días. (Se omite el año porque es 0).
- Caso 2 (Mes y día de Fecha 2 mayores a Fecha 1): Fecha 1: 20230515, Fecha 2: 20240820 
  -> Diferencia: 1 años, 3 meses, 5 días.

Recursos:
- fecha1, fecha2 (int): Fechas ingresadas por el usuario.
- anio1, mes1, dia1 (int): Componentes extraídos de la primera fecha.
- anio2, mes2, dia2 (int): Componentes extraídos de la segunda fecha.
- dif_anios, dif_meses, dif_dias (int): Diferencias calculadas.
- mes_anterior, anio_evaluar, dias_mes_anterior (int): Variables para ajustar días negativos.
- texto_diferencia (str): Cadena de texto construida dinámicamente para mostrar el resultado.
"""

#1)Prologo
print("--- Calculadora de diferencia de fechas ---")
print("Ingrese las fechas como un número entero continuo de 8 dígitos (ej. 20250815 para 15/08/2025).")
print("Asegúrese de que la primera fecha sea estrictamente menor a la segunda.\n")

fecha1 = int(input("Ingrese la primera fecha (AAAAMMDD): "))
fecha2 = int(input("Ingrese la segunda fecha (AAAAMMDD): "))
#2)Desarrollo
anio1 = fecha1 // 10000
mes1 = (fecha1 // 100) % 100
dia1 = fecha1 % 100

anio2 = fecha2 // 10000
mes2 = (fecha2 // 100) % 100
dia2 = fecha2 % 100

# Diferencia directa inicial
dif_anios = anio2 - anio1
dif_meses = mes2 - mes1
dif_dias = dia2 - dia1




