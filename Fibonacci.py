entry = int(input("Introduce la cantidad de números para la secuencia de Fibonacci: "))
lst = [0,1]
if entry == 1:
    lst = [0]
elif entry == 0:
    lst = []
elif entry < 0:
    lst = "No puedes meter un número negativo"
else:
    for i in range(2,entry):
        num = lst[i-2] + lst[i-1]
        lst.append(num)
print(lst)