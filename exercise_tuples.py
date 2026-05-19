# Ejercicios de tuplas: búsqueda del tesoro pirata


def get_coordinate(registro):

    return registro[1]
print(get_coordinate(('Scrimshawed Whale Tooth','2A')))




def convert_coordinate(coordenada):
   
    return (coordenada[0], coordenada[1])
print(convert_coordinate("2A"))
print(convert_coordinate("7F"))
   

def create_record(registro_azara, registro_rui):

    # Convertimos '4B' → ('4', 'B')
    coordenada_azara = (
        registro_azara[1][0],
        registro_azara[1][1]
    )

    coordenada_rui = registro_rui[1]

    if coordenada_azara == coordenada_rui:
        return (
            registro_azara[0],
            registro_azara[1],
            registro_rui[0],
            registro_rui[1],
            registro_rui[2]
        )

    return "not a match"
print(create_record(('Brass Spyglass', '4B'), ('Abandone Lighthouse', ('4', 'B'), 'Blue')))
print(create_record(('Brass Spyglass', '4B'), ('Seaside Cottages', ('1', 'C'), 'Blue')))

def sum_tuple(numeros):
    total = 0
    if numeros == 0:
        return 0
    else:
        for numero in range (len(numeros)):
            total += numeros[numero]
        return total
print(sum_tuple((1, 2, 3, 4, 5)))
print(sum_tuple(()))
print(sum_tuple((10, -15, 5, -5)))

def count_occurrences(tupla, elemento):
    contador = 0
    for item in tupla:
        if item == elemento:
            contador = contador + 1
    return contador
        
print(count_occurrences((1, 2, 2, 3, 2), 2))
print(count_occurrences(('a', 'b', 'a'), 'c'))
print(count_occurrences((), 'x'))

def find_index(tupla, elemento):
    
    indice = 0
    for item in tupla:
        if item == elemento:
            return indice
        indice += 1
    return -1
print(find_index(('a', 'b', 'c', 'b'), 'b'))
print(find_index((1,2,3),9))
print(find_index((), 'x'))


def filter_positives(numeros):
    
    positivos = ()

    for numero in numeros:
        if numero > 0:
            positivos = positivos + (numero,)

    return positivos
print(filter_positives((-3, 1, 0, 5, -2, 7)))
print(filter_positives((-1, -2, -3)))
print(filter_positives((0, 0, 0)))