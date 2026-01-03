def encontrar_duplicados(lista):
    duplicados = set()
    if len(lista) == 0:
        return None
    for indice, valor in enumerate(lista):
        lista.pop(indice)
        if valor in lista:
            duplicados.add(valor)
        lista.insert(indice,valor)
    return duplicados