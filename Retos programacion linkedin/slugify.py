def slugify(texto):
    texto = texto.lower()
    texto = texto.strip()
    texto = texto.replace(" ","-")
    lista = []
    for i in texto:
        if i.isalnum() or i == "-":
            lista.append(i)
    slug = "".join(lista)
    print(slug)