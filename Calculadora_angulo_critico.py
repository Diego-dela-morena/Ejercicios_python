import math
n1,n2 = 0,1
while n2 > n1 or n1 <= 0:
    n1 = float(input("Ingrese el índice de refracción del primer medio n1: "))
    n2 = float(input("Ingrese el índice de refracción del segundo medio n2: "))
    if n2 > n1:
        print("El primer índice de refracción (n1) debe ser mayor que el segundo (n2) para que exista ángulo crítico.")  
    elif n1 <= 0:
        print("Los índices de refracción deben ser mayores que 0.")
theta = math.degrees(math.asin(n2/n1))
print(f"El ángulo crítico para la reflexión total es: {round(theta,4)}°.")