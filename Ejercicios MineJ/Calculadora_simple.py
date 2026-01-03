"""Escriba un programa que realice las siguientes tareas:
Solicite al usuario dos números enteros (N1, N2). Después, muestre el mensaje “El numero
entero 1 es: “, seguido del valor de N1 y el mensaje “El numero entero 2 es: “, seguido del
valor de N2. Estos mensajes deben aparecer en líneas independientes.
Solicite al usuario un carácter (operacion) y muestre el mensaje “La operacion solicitada es: “,
seguido del valor del carácter. Este mensaje debe aparecer en una línea independiente.
Si el carácter es ‘+’, se hará la suma de N1 y N1 y se mostrará el mensaje “La suma es: “,
seguido del valor resultante de la operación. Este mensaje debe aparecer en una línea
independiente.
Si el carácter es ‘-’, se hará la resta de N1 y N1 y se mostrará el mensaje “La resta es: “,
seguido del valor resultante de la operación. Este mensaje debe aparecer en una línea
independiente.
Si el carácter es ‘*’, se hará el producto de N1 y N1 y se mostrará el mensaje “El producto es:
“, seguido del valor resultante de la operación. Este mensaje debe aparecer en una línea
independiente.
Si el carácter es ‘/’, se hará la división de N1 y N1 y se mostrará el mensaje “La division es: “,
seguido del valor resultante de la operación. Este mensaje debe aparecer en una línea
independiente.
Si el carácter es otro valor, se mostrará el mensaje “La operacion indicada NO ES VALIDA“.
Este mensaje debe aparecer en una línea independiente"""

N1 = int(input("Introduzca un número: "))
N2 = int(input("Introduzca un número: "))
print(f"El número entero 1 es {N1}")
print(f"El número entero 2 es {N2}")
operacion = str(input("Introduzca un signo: "))[0]
print(f"La operacion solicitada es: {operacion}")
if operacion == "+":
    print(N1 + N2)
elif operacion == "-":
    print(N1 - N2)
elif operacion == "*":
    print(N1 * N2)
elif operacion == "/":
    print(N1/N2)
else:
    print("La operacion indicada NO ES VALIDA")