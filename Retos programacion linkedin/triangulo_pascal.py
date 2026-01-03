def triangulo_pascal(numero):
    lista = []
    for n_fila in range(numero):
        fila = []
        for posicion in range(n_fila + 1):
            if posicion == 0 or posicion == n_fila:
                fila.append(1)
            else:
                valor = lista[n_fila - 1][posicion - 1] + lista[n_fila -1][posicion]
                fila.append(valor)
        lista.append(fila)
    return lista