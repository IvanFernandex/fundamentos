"""
Sección Declarativa

Descripción: Convierte un número entero positivo (hasta 999.999.999) a su cardinalidad 
en palabras en español, implementando todas las reglas gramaticales y excepciones.

Casos de prueba:
- 0 -> cero
- 15 -> quince
- 42 -> cuarenta y dos
- 100 -> cien
- 101 -> ciento uno
- 1001 -> mil uno
- 21000 -> veintiún mil
- 2025 -> dos mil veinticinco
- 1000000 -> un millón
- 121000000 -> ciento veintiún millones

Recursos:
- numero (int): Número a procesar.
- millones, miles, unidades_grupo (int): Agrupación de a 3 dígitos.
- c, d, u (int): Centenas, decenas y unidades de cada grupo temporal.
- texto_millones, texto_miles, texto_unidades, resultado, temp (str): Cadenas de texto.
"""

# Sección Algorítmica

# 1) Prólogo
print("--- Conversor de Números a Palabras (Versión Completa) ---")
numero = int(input("Ingrese un número entero no negativo (hasta 999999999): "))

# 2) Desarrollo
if numero == 0:
    resultado = "cero"
elif numero < 0 or numero > 999999999:
    resultado = "Error: Número fuera del rango permitido."
else:
    # Descomposición en grupos de 3 dígitos
    millones = numero // 1000000
    miles = (numero % 1000000) // 1000
    unidades_grupo = numero % 1000
    
    texto_millones = ""
    texto_miles = ""
    texto_unidades = ""

    # ==========================================
    # PROCESAMIENTO GRUPO MILLONES
    # ==========================================
    if millones > 0:
        if millones == 1:
            texto_millones = "un millón"
        else:
            c = millones // 100
            d = (millones % 100) // 10
            u = millones % 10
            temp = ""
            
            # Centenas
            if c == 1:
                if d == 0 and u == 0: temp = temp + "cien "
                else: temp = temp + "ciento "
            elif c == 2: temp = temp + "doscientos "
            elif c == 3: temp = temp + "trescientos "
            elif c == 4: temp = temp + "cuatrocientos "
            elif c == 5: temp = temp + "quinientos "
            elif c == 6: temp = temp + "seiscientos "
            elif c == 7: temp = temp + "setecientos "
            elif c == 8: temp = temp + "ochocientos "
            elif c == 9: temp = temp + "novecientos "
            
            # Decenas y Unidades
            if d == 0:
                if u == 1: temp = temp + "un" # Apócope para millones
                elif u == 2: temp = temp + "dos"
                elif u == 3: temp = temp + "tres"
                elif u == 4: temp = temp + "cuatro"
                elif u == 5: temp = temp + "cinco"
                elif u == 6: temp = temp + "seis"
                elif u == 7: temp = temp + "siete"
                elif u == 8: temp = temp + "ocho"
                elif u == 9: temp = temp + "nueve"
            elif d == 1:
                if u == 0: temp = temp + "diez"
                elif u == 1: temp = temp + "once"
                elif u == 2: temp = temp + "doce"
                elif u == 3: temp = temp + "trece"
                elif u == 4: temp = temp + "catorce"
                elif u == 5: temp = temp + "quince"
                elif u == 6: temp = temp + "dieciséis"
                elif u == 7: temp = temp + "diecisiete"
                elif u == 8: temp = temp + "dieciocho"
                elif u == 9: temp = temp + "diecinueve"
            elif d == 2:
                if u == 0: temp = temp + "veinte"
                elif u == 1: temp = temp + "veintiún" # Apócope
                elif u == 2: temp = temp + "veintidós"
                elif u == 3: temp = temp + "veintitrés"
                elif u == 4: temp = temp + "veinticuatro"
                elif u == 5: temp = temp + "veinticinco"
                elif u == 6: temp = temp + "veintiséis"
                elif u == 7: temp = temp + "veintisiete"
                elif u == 8: temp = temp + "veintiocho"
                elif u == 9: temp = temp + "veintinueve"
            elif d >= 3:
                if d == 3: temp = temp + "treinta"
                elif d == 4: temp = temp + "cuarenta"
                elif d == 5: temp = temp + "cincuenta"
                elif d == 6: temp = temp + "sesenta"
                elif d == 7: temp = temp + "setenta"
                elif d == 8: temp = temp + "ochenta"
                elif d == 9: temp = temp + "noventa"
                
                if u > 0:
                    temp = temp + " y "
                    if u == 1: temp = temp + "un" # Apócope
                    elif u == 2: temp = temp + "dos"
                    elif u == 3: temp = temp + "tres"
                    elif u == 4: temp = temp + "cuatro"
                    elif u == 5: temp = temp + "cinco"
                    elif u == 6: temp = temp + "seis"
                    elif u == 7: temp = temp + "siete"
                    elif u == 8: temp = temp + "ocho"
                    elif u == 9: temp = temp + "nueve"
            
            texto_millones = temp.strip() + " millones"

    # ==========================================
    # PROCESAMIENTO GRUPO MILES
    # ==========================================
    if miles > 0:
        if miles == 1:
            texto_miles = "mil"
        else:
            c = miles // 100
            d = (miles % 100) // 10
            u = miles % 10
            temp = ""
            
            # Centenas
            if c == 1:
                if d == 0 and u == 0: temp = temp + "cien "
                else: temp = temp + "ciento "
            elif c == 2: temp = temp + "doscientos "
            elif c == 3: temp = temp + "trescientos "
            elif c == 4: temp = temp + "cuatrocientos "
            elif c == 5: temp = temp + "quinientos "
            elif c == 6: temp = temp + "seiscientos "
            elif c == 7: temp = temp + "setecientos "
            elif c == 8: temp = temp + "ochocientos "
            elif c == 9: temp = temp + "novecientos "
            
            # Decenas y Unidades
            if d == 0:
                if u == 1: temp = temp + "un" # Apócope para miles
                elif u == 2: temp = temp + "dos"
                elif u == 3: temp = temp + "tres"
                elif u == 4: temp = temp + "cuatro"
                elif u == 5: temp = temp + "cinco"
                elif u == 6: temp = temp + "seis"
                elif u == 7: temp = temp + "siete"
                elif u == 8: temp = temp + "ocho"
                elif u == 9: temp = temp + "nueve"
            elif d == 1:
                if u == 0: temp = temp + "diez"
                elif u == 1: temp = temp + "once"
                elif u == 2: temp = temp + "doce"
                elif u == 3: temp = temp + "trece"
                elif u == 4: temp = temp + "catorce"
                elif u == 5: temp = temp + "quince"
                elif u == 6: temp = temp + "dieciséis"
                elif u == 7: temp = temp + "diecisiete"
                elif u == 8: temp = temp + "dieciocho"
                elif u == 9: temp = temp + "diecinueve"
            elif d == 2:
                if u == 0: temp = temp + "veinte"
                elif u == 1: temp = temp + "veintiún" # Apócope
                elif u == 2: temp = temp + "veintidós"
                elif u == 3: temp = temp + "veintitrés"
                elif u == 4: temp = temp + "veinticuatro"
                elif u == 5: temp = temp + "veinticinco"
                elif u == 6: temp = temp + "veintiséis"
                elif u == 7: temp = temp + "veintisiete"
                elif u == 8: temp = temp + "veintiocho"
                elif u == 9: temp = temp + "veintinueve"
            elif d >= 3:
                if d == 3: temp = temp + "treinta"
                elif d == 4: temp = temp + "cuarenta"
                elif d == 5: temp = temp + "cincuenta"
                elif d == 6: temp = temp + "sesenta"
                elif d == 7: temp = temp + "setenta"
                elif d == 8: temp = temp + "ochenta"
                elif d == 9: temp = temp + "noventa"
                
                if u > 0:
                    temp = temp + " y "
                    if u == 1: temp = temp + "un" # Apócope
                    elif u == 2: temp = temp + "dos"
                    elif u == 3: temp = temp + "tres"
                    elif u == 4: temp = temp + "cuatro"
                    elif u == 5: temp = temp + "cinco"
                    elif u == 6: temp = temp + "seis"
                    elif u == 7: temp = temp + "siete"
                    elif u == 8: temp = temp + "ocho"
                    elif u == 9: temp = temp + "nueve"
            
            texto_miles = temp.strip() + " mil"

    # ==========================================
    # PROCESAMIENTO GRUPO UNIDADES
    # ==========================================
    if unidades_grupo > 0:
        c = unidades_grupo // 100
        d = (unidades_grupo % 100) // 10
        u = unidades_grupo % 10
        temp = ""
        
        # Centenas
        if c == 1:
            if d == 0 and u == 0: temp = temp + "cien "
            else: temp = temp + "ciento "
        elif c == 2: temp = temp + "doscientos "
        elif c == 3: temp = temp + "trescientos "
        elif c == 4: temp = temp + "cuatrocientos "
        elif c == 5: temp = temp + "quinientos "
        elif c == 6: temp = temp + "seiscientos "
        elif c == 7: temp = temp + "setecientos "
        elif c == 8: temp = temp + "ochocientos "
        elif c == 9: temp = temp + "novecientos "
        
        # Decenas y Unidades
        if d == 0:
            if u == 1: temp = temp + "uno" # Sin apócope al final del número
            elif u == 2: temp = temp + "dos"
            elif u == 3: temp = temp + "tres"
            elif u == 4: temp = temp + "cuatro"
            elif u == 5: temp = temp + "cinco"
            elif u == 6: temp = temp + "seis"
            elif u == 7: temp = temp + "siete"
            elif u == 8: temp = temp + "ocho"
            elif u == 9: temp = temp + "nueve"
        elif d == 1:
            if u == 0: temp = temp + "diez"
            elif u == 1: temp = temp + "once"
            elif u == 2: temp = temp + "doce"
            elif u == 3: temp = temp + "trece"
            elif u == 4: temp = temp + "catorce"
            elif u == 5: temp = temp + "quince"
            elif u == 6: temp = temp + "dieciséis"
            elif u == 7: temp = temp + "diecisiete"
            elif u == 8: temp = temp + "dieciocho"
            elif u == 9: temp = temp + "diecinueve"
        elif d == 2:
            if u == 0: temp = temp + "veinte"
            elif u == 1: temp = temp + "veintiuno" # Sin apócope
            elif u == 2: temp = temp + "veintidós"
            elif u == 3: temp = temp + "veintitrés"
            elif u == 4: temp = temp + "veinticuatro"
            elif u == 5: temp = temp + "veinticinco"
            elif u == 6: temp = temp + "veintiséis"
            elif u == 7: temp = temp + "veintisiete"
            elif u == 8: temp = temp + "veintiocho"
            elif u == 9: temp = temp + "veintinueve"
        elif d >= 3:
            if d == 3: temp = temp + "treinta"
            elif d == 4: temp = temp + "cuarenta"
            elif d == 5: temp = temp + "cincuenta"
            elif d == 6: temp = temp + "sesenta"
            elif d == 7: temp = temp + "setenta"
            elif d == 8: temp = temp + "ochenta"
            elif d == 9: temp = temp + "noventa"
            
            if u > 0:
                temp = temp + " y "
                if u == 1: temp = temp + "uno" # Sin apócope
                elif u == 2: temp = temp + "dos"
                elif u == 3: temp = temp + "tres"
                elif u == 4: temp = temp + "cuatro"
                elif u == 5: temp = temp + "cinco"
                elif u == 6: temp = temp + "seis"
                elif u == 7: temp = temp + "siete"
                elif u == 8: temp = temp + "ocho"
                elif u == 9: temp = temp + "nueve"
        
        texto_unidades = temp.strip()

    # ==========================================
    # ENSAMBLADO FINAL
    # ==========================================
    resultado = ""
    if texto_millones != "":
        resultado = resultado + texto_millones + " "
    if texto_miles != "":
        resultado = resultado + texto_miles + " "
    if texto_unidades != "":
        resultado = resultado + texto_unidades
        
    resultado = resultado.strip()

# 3) Epílogo
print(f"Número ingresado : {numero}")
print(f"En palabras      : {resultado}")
input("Pulse Enter para terminar el programa")
