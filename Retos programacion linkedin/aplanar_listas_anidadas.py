def aplanar_lista(lista):
    for indice, valor in enumerate(lista):
        if type(valor) == list:
            valor.reverse()
            lista.pop(indice)
            for j in valor:
              lista.insert(indice,j)  
    return lista

    