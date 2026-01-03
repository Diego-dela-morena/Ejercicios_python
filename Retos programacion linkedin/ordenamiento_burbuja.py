def ordenamiento_burbuja(lista):
    for j in range(len(lista) - 1):
        for indice, valor in enumerate(lista):
            if indice == len(lista) - 1:
                break
            elif valor >= lista[indice + 1]:
                lista[indice], lista [indice + 1] = lista[indice + 1], lista[indice]
    return lista


