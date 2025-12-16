import math
theta1, theta2 = 0, 0
n1 = 0
while theta1 >= 90 or theta2 >= 90 or theta1 <= 0 or theta2 <= 0 or n1 <= 0:
    theta1 = float(input("Introduzca el ángulo incidente theta1 (en grados): "))
    n1 = float(input("Ingrese el índice de refracción del primer medio n1 (si se encuentra en el aire n1 = 1): "))
    theta2 = float(input("Introduzca el ángulo de refracción theta2 (en grados): "))
    if theta1 >= 90 or theta2 >= 90 or theta1 <= 0 or theta2 <= 0:
        print("Los ángulos deben ser mayores que 0 y menores que 90.")
    elif n1 <= 0:
        print("El índice de refracción del medio debe ser un número positivo.")
n2 =  n1 * math.sin(math.radians(theta1)) / math.sin(math.radians(theta2))
print(f"El índice de refracción del segundo medio es: {round(n2,4)}")