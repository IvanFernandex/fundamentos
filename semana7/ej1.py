import copy

def experimento_enteros():
    print("=== Experimento 1(a): Enteros ===")
    x = 10
    y = x
    # Predicción:
    # x is y True (mismo objeto)
    print("Antes:")
    print(x, y)
    print("x is y:", x is y)
    print("id(x):", id(x), "id(y):", id(y))
    
    y = y + 1
    # Predicción:
    # x no cambia
    # x is y  False (nuevo objeto)
    print("\nDespués de y = y + 1:")
    print(x, y)
    print("x is y:", x is y)
    print("id(x):", id(x), "id(y):", id(y))

def experimento_strings():
    print("\n=== Experimento 1(b): Strings ===")
    s1 = "hola"
    s2 = s1
    print("Antes:")
    print("s1 is s2:", s1 is s2)

    s2 = s2 + " mundo"
    print("\nDespués:")
    print(s1)
    print(s2)
    print("s1 is s2:", s1 is s2)

def experimento_cache():
    print("\n=== Experimento 1(c): Caché ===")

    a = 256
    b = 256
    print("256 → a is b:", a is b)

    a = 257
    b = 257
    print("257 → a is b:", a is b)

def experimento_listas_alias():
    print("\n=== Experimento 2(d): Listas alias ===")

    lista1 = [1, 2, 3]
    lista2 = lista1

    lista2.append(4)

    print("lista1:", lista1)
    print("lista2:", lista2)
    print("lista1 is lista2:", lista1 is lista2)

def experimento_listas_distintas():
    print("\n=== Experimento 2(e): Listas distintas ===")

    lista3 = [1, 2, 3]
    lista4 = [1, 2, 3]

    print("lista3 == lista4:", lista3 == lista4)
    print("lista3 is lista4:", lista3 is lista4)

def experimento_listas_distintas():
    print("\n=== Experimento 2(e): Listas distintas ===")

    lista3 = [1, 2, 3]
    lista4 = [1, 2, 3]

    print("lista3 == lista4:", lista3 == lista4)
    print("lista3 is lista4:", lista3 is lista4)

def experimento_tuplas():
    print("\n=== Experimento 2(f): Tuplas ===")

    tupla1 = (10, 20)
    tupla2 = tupla1

    tupla2[0] = 99

def experimento_copia_superficial():
    print("\n=== Experimento 3(g): Copia superficial ===")

    matriz = [[1, 2], [3, 4]]
    copia = matriz[:]

    copia[0][0] = 99

    print("matriz:", matriz)
    print("copia:", copia)


def experimento_copia_profunda():
    print("\n=== Experimento 3(h): Copia profunda ===")

    matriz = [[1, 2], [3, 4]]
    copia = copy.deepcopy(matriz)

    copia[0][0] = 99

    print("matriz:", matriz)
    print("copia:", copia)