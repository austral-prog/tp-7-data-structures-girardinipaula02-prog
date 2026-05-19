# Ejercicios de diccionarios: sistema de inventario


def create_inventory(items):
 """ Crea un diccionario "inventario" a partir de una lista de items.
 Cada clave es el nombre de un item y su valor es la cantidad de veces que aparece en la lista.
   Args: items: Lista de items (strings)
 Returns: Un diccionario con cada item y su cantidad """
 
  
 inventario = {}

 for item in items:

        if item in inventario:

            inventario[item] += 1

        else:

            inventario[item] = 1

 return inventario
print(create_inventory(["coal", "wood", "wood", "diamond", "diamond", "diamond"]))

def add_items(inventario, items):
    """
    Agrega una lista de items a un inventario existente. Si un item ya está
    en el inventario, incrementa su cantidad en 1. Si no, lo agrega con
    cantidad 1.

    Args:
        inventario: Diccionario con el inventario actual
        items: Lista de items a agregar

    Returns:
        El inventario actualizado
    """

    for item in items:
        if item in inventario:
            inventario[item] += 1
        else:
            inventario[item] = 1

    return inventario
print(add_items({"coal": 1}, ["wood", "iron", "coal", "wood"]))


def decrement_items(inventario, items):
    """
    Resta 1 a la cantidad del inventario por cada vez que un item aparezca
    en la lista. Las cantidades no pueden ser negativas.
    """

    for item in items:
        if item in inventario and inventario[item] > 0:
            inventario[item] -= 1

    return inventario
print(decrement_items({"coal": 3, "diamond": 1, "iron": 5},
                ["diamond", "coal", "iron", "iron"]))
print(decrement_items({"coal": 2, "wood": 1, "diamond": 2},
                ["coal", "coal", "wood", "wood", "diamond"]))


def remove_item(inventario, item):
    """
    Elimina un item del inventario por completo (clave y cantidad).
    Si el item no está en el inventario, retornar el inventario sin cambios.
    """

    if item in inventario:
        del inventario[item]

    return inventario
print(remove_item({"coal": 2, "wood": 1, "diamond": 2}, "coal"))
print(remove_item({"coal": 2, "wood": 1, "diamond": 2}, "gold"))


def list_inventory(inventario):
    """
    Retorna una lista de tuplas (item, cantidad) con el contenido del
    inventario. Solo incluye los items con cantidad mayor a 0.
    """

    lista = []

    for item, cantidad in inventario.items():
        if cantidad > 0:
            lista.append((item, cantidad))

    return lista
print(list_inventory({"coal": 7, "wood": 11, "diamond": 2, "iron": 7, "silver": 0}))


def find_max_value(diccionario):
    """
    Recibe un diccionario de nombres y puntajes, y retorna la clave
    con el valor más alto.
    """

    if len(diccionario) == 0:
        return ""

    return max(diccionario, key=diccionario.get)
print(find_max_value({'John': 85, 'Emma': 92, 'Sophia': 78}))
print(find_max_value({}))


def reverse_dict(diccionario):
    """
    Invierte un diccionario: cada valor pasa a ser clave y cada
    clave pasa a ser valor.
    """

    nuevo_dic = {}

    for clave, valor in diccionario.items():
        if valor in nuevo_dic:
            nuevo_dic[valor] += clave
        else:
            nuevo_dic[valor] = clave

    return nuevo_dic
print(reverse_dict({'a': 1, 'b': 2, 'c': 3, 'd': 3, 'e': 2}))
print(reverse_dict({}))


def word_frequency(palabras):
    """
    Cuenta cuántas veces aparece cada palabra en la lista.
    """

    if palabras == "":
        return {}

    frecuencia = {}

    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1

    return frecuencia
print(word_frequency(["apple", "banana", "apple", "orange", "banana", "apple"]))
print(word_frequency(""))


def find_biggest_expense(gastos):
    """
    Recibe un diccionario donde cada clave es una categoría y el valor
    una lista de gastos.
    """

    if len(gastos) == 0:
        return ""

    categoria_max = ""
    promedio_max = 0

    for categoria, lista in gastos.items():
        promedio = sum(lista) / len(lista)

        if promedio > promedio_max:
            promedio_max = promedio
            categoria_max = categoria

    return categoria_max
print(find_biggest_expense({'Food': [60, 80, 100],
                      'Transport': [10, 1, 2],
                      'Games': [10, 20, 30]}))


def sum_expenses(gastos):
    """
    Recibe un diccionario de categorías con listas de gastos y retorna
    un nuevo diccionario con la suma total de los gastos por categoría.
    """

    resultado = {}

    for categoria, lista in gastos.items():
        resultado[categoria] = sum(lista)

    return resultado
print(sum_expenses({'Food': [60, 80, 100],
              'Transport': [10, 1, 2],
              'Games': [10, 20, 30]}))


def sum_expenses_by_type(gastos):
    """
    Recibe un diccionario de categorías cuyos valores son listas de
    tuplas (tipo, monto). Retorna un nuevo diccionario con la suma
    de montos agrupada por tipo.
    """

    resultado = {}

    for categoria, lista in gastos.items():
        for tipo, monto in lista:
            if tipo in resultado:
                resultado[tipo] += monto
            else:
                resultado[tipo] = monto

    return resultado
print(sum_expenses_by_type({
    'Food': [("A", 60), ("B", 100), ("A", 20)],
    'Transport': [("A", 10), ("B", 50), ("C", 5)],
    'Games': [("A", 6), ("B", 24), ("C", 99)]
}))
