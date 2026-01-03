cadena = input("Ingrese la cadena: ")
cadena = cadena.lower()
cadena = cadena.replace(" ","")
cadena_reverse = cadena[-1::-1]
palindromo = True if cadena == cadena_reverse else False
print(palindromo)