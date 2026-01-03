texto = input("Ingrese texto con paréntesis: ")
num_abre_parentesis = 0
num_cierra_parentesis = 0
parentesis_abierto = False
output = None
for i in texto:
    if i == "(":
        num_abre_parentesis += 1
        parentesis_abierto = True
    elif i == ")":
        if parentesis_abierto:
            num_cierra_parentesis += 1
        else:
            output = False
if output == False:
    print(f"{output} (se cerró un paréntesis sin abrir)")
else:
    print(num_abre_parentesis == num_cierra_parentesis)