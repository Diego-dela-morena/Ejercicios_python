import math
n1,n2,theta1,theta_critico = 0,1,0,90
while n1 <= 0 or n2 <= 0 or theta1 >= 90 or theta1 <= 0:
    n1 = float(input("Ingrese el índice de refracción del primer medio n1: "))
    n2 = float(input("Ingrese el índice de refracción del segundo medio n2: "))
    theta1 = float(input("Introduzca el ándulo de incidencia: ")) 
    if n1 <= 0 or n2 <= 0:
        print("Los índices de refracción deben ser mayores que 0.")
    elif theta1 >= 90 or theta1 <= 0:
        print("El ángulo de incidencia debe ser menor que 90 y mayor que 0.")
    elif n1 > n2:
        theta_critico = math.degrees(math.asin(n2/n1))
if theta1 >= theta_critico:
    print("Se producirá reflexión total (Ángulo de incidencia > Ángulo crítico).")
else:
    theta2 = math.degrees(math.asin(math.sin(math.radians(theta1))*n1/n2))
    print(f"El ángulo refractado será: {theta2}")
