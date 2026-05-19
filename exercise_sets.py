# Ejercicios de sets: catering del club de cocina

ALCOHOLS = {
    "whiskey", "whisky", "white rum", "dark rum", "bourbon", "rye", "scotch",
    "vodka", "tequila", "gin", "dry vermouth", "sweet vermouth", "prosecco",
    "aperol", "brandy", "mezcal", "triple sec", "coffee liqueur",
    "almond liqueur", "champagne", "orange curacao", "rum"
}


def clean_ingredients(nombre_plato, ingredientes):
    ingredientes_sin_duplicados = set(ingredientes)

    return (nombre_plato, ingredientes_sin_duplicados)
      
print(clean_ingredients('Punjabi-Style Chole',
                  ['onions', 'tomatoes', 'ginger paste', 'ginger paste',
                   'chickpeas', 'chickpeas']))
        

def check_drinks(nombre_bebida, ingredientes):
    for ingrediente in ingredientes:

        if ingrediente in ALCOHOLS:
           return nombre_bebida + " Cocktail"
    return nombre_bebida + " Mocktail"
print(check_drinks('Honeydew Cucumber',
             ['honeydew', 'coconut water', 'mint leaves', 'lime juice']))
print(check_drinks('Shirley Tonic',
             ['cinnamon stick', 'scotch', 'whole cloves', 'ginger']))


def unique_chars(texto):
    return set(texto)
print(unique_chars("hello"))
print(unique_chars(""))

def sum_set(numeros):
    total = 0
    for numero in numeros:
        total = total + numero
    return total
print(sum_set({1, 2, 3, 4}))
print(sum_set(set()))       
print(sum_set({-5, 5, -3, 3}))


def common_elements(set_a, set_b):
    comunes = set()

    for elemento in set_a:

        if elemento in set_b:
            comunes.add(elemento)

    return comunes
print(common_elements({1, 2, 3}, {2, 3, 4}))
print(common_elements({1, 2}, {3, 4}))
print(common_elements({1, 2, 3}, {1, 2, 3}))