"""Escriba un programa que solicite al usuario números enteros positivos,
uno de cada vez, de manera que se determine cuál es el valor máximo y el valor mínimo de todos
los valores dados. El proceso de petición de datos terminará cuando el usuario introduzca un número
negativo, momento en el que se mostrará por pantalla el valor máximo y el mínimo de todos los
facilitados por el usuario."""

entry = int(input("Introduzca un número: "))
maximo = entry
minimo = entry
print(f"Max= {maximo}")
print(f"Min= {minimo}")
while entry >= 0:
    entry = int(input("Introduzca un número: "))
    if entry >= maximo:
        maximo = entry
    elif entry <= minimo:
        minimo = entry
    print(f"Max= {maximo}")
    print(f"Min= {minimo}")