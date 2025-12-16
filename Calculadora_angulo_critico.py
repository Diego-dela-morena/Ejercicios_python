import math
n1,n2 = 1,0
while n2 < n1 or n1 <= 0:
    n1 = float(input("Ingrese el índice de refracción del primer medio n1 (si se encuentra en el aire n1 = 1): "))
    n2 = float(input("Ingrese el índice de refracción del segundo medio n2: "))
    if n2 < n1:
        print("El segunde índice de refracción (n2) debe ser mayor que el primero (n1).")  
    elif n1 <= 0:
        print("Los índices de refracción deben ser mayores que 0.")
theta = math.degrees(math.asin(n1/n2))
print(f"El ángulo crítico para la reflexión total es: {round(theta,4)}°.")