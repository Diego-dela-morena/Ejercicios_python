def calcular_numero_triangular(numero):
    result = 0
    for i in range(1,numero + 1):
        result += i
    return result


print(calcular_numero_triangular(4))