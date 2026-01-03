cadena = input("Ingrese la cadena: ")
cadena = cadena.replace(" ","")
lista = []
repite = False
for i in cadena:
    if i in lista:
        repite = True
        break
    else:
        lista.append(i)
if repite == True:
    print(f"La primera letra en repetirse es '{i}'")
else:
    print("None")