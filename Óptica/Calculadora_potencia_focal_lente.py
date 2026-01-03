while True:   
    print("1- Calcular la potencia con la ecuación de Gauss (lentes delgadas).")
    print("2- Calcular la potencia con los radios e índice de refracción (lentes delgadas).")
    print("3- Calcular la potencia con los radios, índice de refracción y espesor central (lentes gruesas).")
    print("4- Calcular la potencia frontal posterior con los radios, índice de refracción y espesor central (lentes gruesas).")
    print("5- Salir del programa.")
    choice = int(input("Elija el método para calcular la potencia de la lente: "))
    if choice == 1:
        while True:
            s1 = float(input("Introduzca la distancia desde el objeto a la lente en cm (con signo según convenio): ")) / 100
            s2 = float(input("Introduzca la distancia desde la lente hasta la imagen en cm (con signo según convenio): ")) / 100
            if s1 == 0 or s2 == 0:
                print("Las distancias objeto e imagen tienen que ser distintas de cero")
            else:
                power = 1/s2 - 1/s1
                if power == 0:
                    print(f"La potencia de la lente es {power} D.")
                    print("La distancia focal de la lente es infinita.") 
                else:
                    focal = 1/power * 100
                    print(f"La potencia de la lente es {round(power,4)} D.")
                    print(f"La distancia focal de la lente es {round(focal,4)} cm.")
                break
    elif choice == 2:
        while True:
            n = float(input("Introduzca el índice de refracción del material de la lente: "))
            r1 = float(input("Introduzca el radio de la cara anterior en mm (signo según convenio o ponga '0' si es plano): ")) / 1000
            r2 = float(input("Introduzca el radio de la cara posterior en mm (signo según convenio o ponga '0' si es plano): ")) / 1000
            if n <= 0:
                print("El índice de refracción debe ser un número positivo.")
            elif r1 == 0 and r2 != 0:
                power = (n - 1) * (0 - 1/r2)
                if power == 0:
                    print(f"La potencia de la lente es {power} D.")
                    print("La distancia focal de la lente es infinita.")
                else:
                    focal = 1/power * 100
                    print(f"La potencia de la lente es {round(power,4)} D.")
                    print(f"La distancia focal de la lente es {round(focal,4)} cm.")
                break
            elif r1 != 0 and r2 == 0:
                power = (n - 1) * (1/r1 - 0)
                if power == 0:
                    print(f"La potencia de la lente es {power} D.")
                    print("La distancia focal de la lente es infinita.")
                else:
                    focal = 1/power * 100
                    print(f"La potencia de la lente es {round(power,4)} D.")
                    print(f"La distancia focal de la lente es {round(focal,4)} cm.")
                break
            elif r1 == 0 and r2 == 0:
                print("La potencia de la lente es 0 D.")
                print("La distancia focal de la lente es infinita.")
                break
            else:
                power = (n - 1) * (1/r1 - 1/r2)
                if power == 0:
                    print(f"La potencia de la lente es {power} D.")
                    print("La distancia focal de la lente es infinita.")
                else:
                    focal = 1/power * 100
                    print(f"La potencia de la lente es {round(power,4)} D.")
                    print(f"La distancia focal de la lente es {round(focal,4)} cm.")
                break
    elif choice == 3:
        while True:
            n = float(input("Introduzca el índice de refracción del material de la lente: "))
            r1 = float(input("Introduzca el radio de la cara anterior en mm (signo según convenio o ponga '0' si es plano): ")) / 1000
            r2 = float(input("Introduzca el radio de la cara posterior en mm (signo según convenio o ponga '0' si es plano): ")) / 1000
            e = float(input("Introduzca el espesor central de la lente en mm: ")) / 1000
            if n <= 0:
                print("El índice de refracción debe ser un número positivo.")
            elif e <= 0:
                print("El espesor central debe ser un número positivo.")
            elif r1 == 0 and r2 != 0:
                power = (1 - n)/r2
                if power == 0:
                    print(f"La potencia de la lente es {power} D.")
                    print("La distancia focal de la lente es infinita.")
                else:                 
                    focal = 1/power * 100
                    print(f"La potencia de la lente es {round(power,4)} D.")
                    print(f"La distancia focal de la lente es {round(focal,4)} cm.")
                break
            elif r1 != 0 and r2 == 0:
                power = (n - 1)/r1
                if power == 0:
                    print(f"La potencia de la lente es {power} D.")
                    print("La distancia focal de la lente es infinita.")
                else:                 
                    focal = 1/power * 100
                    print(f"La potencia de la lente es {round(power,4)} D.")
                    print(f"La distancia focal de la lente es {round(focal,4)} cm.")
                break                
            elif r1 == 0 and r2 == 0:
                    print("La potencia de la lente es 0 D.")
                    print("La distancia focal de la lente es infinita.")   
                    break             
            else:
                p1 = (n - 1)/r1
                p2 = (1 - n)/r2
                power = p1 + p2 - e * p1 * p2/n
                if power == 0:
                    print(f"La potencia de la lente es {power} D.")
                    print("La distancia focal de la lente es infinita.")
                else:                 
                    focal = 1/power * 100
                    print(f"La potencia de la lente es {round(power,4)} D.")
                    print(f"La distancia focal de la lente es {round(focal,4)} cm.")
                break
    elif choice == 4:
        while True:
            n = float(input("Introduzca el índice de refracción del material de la lente: "))
            r1 = float(input("Introduzca el radio de la cara anterior en mm (signo según convenio o ponga '0' si es plano): ")) / 1000
            r2 = float(input("Introduzca el radio de la cara posterior en mm (signo según convenio o ponga '0' si es plano): ")) / 1000
            e = float(input("Introduzca el espesor central de la lente en mm: ")) / 1000
            if n <= 0:
                print("El índice de refracción debe ser un número positivo.")
            elif e <= 0:
                print("El espesor central debe ser un número positivo.")
            elif r1 == 0 and r2 != 0:
                power = (1 - n)/r2
                if power == 0:
                    print(f"La potencia frontal posterior de la lente es {power} D.")
                    print("La distancia focal de la lente es infinita.")
                else:                 
                    focal = 1/power * 100
                    print(f"La potencia frontal posterior de la lente es {round(power,4)} D.")
                    print(f"La distancia focal de la lente es {round(focal,4)} cm.")
                break
            elif r1 != 0 and r2 == 0:
                p1 = (n - 1)/r1
                power = p1 / (1 - e/n * p1)
                if power == 0:
                    print(f"La potencia frontal posterior de la lente es {power} D.")
                    print("La distancia focal de la lente es infinita.")
                else:                 
                    focal = 1/power * 100
                    print(f"La potencia frontal de la lente es {round(power,4)} D.")
                    print(f"La distancia focal de la lente es {round(focal,4)} cm.")
                break
            elif r1 == 0 and r2 == 0:
                    print("La potencia frontal posterior de la lente es 0 D.")
                    print("La distancia focal de la lente es infinita.")
                    break                                               
            else:
                p1 = (n - 1)/r1
                p2 = (1 - n)/r2
                power = p1 / (1 - e/n * p1) + p2
                if power == 0:
                    print(f"La potencia frontal posterior de la lente es {power} D.")
                    print("La distancia focal de la lente es infinita.")
                else:                 
                    focal = 1/power * 100
                    print(f"La potencia frontal posterior de la lente es {round(power,4)} D.")
                    print(f"La distancia focal de la lente es {round(focal,4)} cm.")
                break
    elif choice == 5:
        break
    else:
        print(f"Tu elección {choice} no se encuentra entre las posibles.")