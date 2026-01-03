def comprobar_primo(numero):
    es_primo = True
    for i in range(2,int(numero/2)):
        if numero % i == 0:
            es_primo = False
    if numero <= 1:
        es_primo = False
    return es_primo