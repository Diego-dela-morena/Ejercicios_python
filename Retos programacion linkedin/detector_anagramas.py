palabra1 = input("Ingrese la primera palabra: ")
palabra2 = input("Ingrese la segunda palabra: ")
palabra1 = palabra1.lower()
palabra2 = palabra2.lower()
palabra1_lista = list(palabra1)
palabra2_lista = list(palabra2)
palabra1_lista.sort()
palabra2_lista.sort()
if palabra1_lista == palabra2_lista:
    print("Son anagramas")
else:
    print("No son anagramas")