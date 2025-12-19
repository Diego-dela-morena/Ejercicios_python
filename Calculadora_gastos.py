print("Welcome to the Daily Expense Tracker!")
print()
print("Menu:")
print("1. Add a new expense")
print("2. View all expenses")
print("3. Calculate total and average expense")
print("4. Clear all expenses")
print("5. Exit")
gastos = []
total = 0
avrg = 0
while True:
    choice = int(input("Choice your option: "))
    if choice == 5:
        print("Exiting the Daily Expense Tracker. Goodbye!")
        break
    elif choice == 1:
        gasto = float(input("Introduce your expense: "))
        gastos.append(gasto)
        print("Expense added successfully!")
    elif choice == 2:
        if len(gastos) == 0:
            print("No expenses recorded yet.")
        else:
            print("Your expenses:")
            for index,element in enumerate(gastos):
                print(f"{index + 1}. {element}")
    elif choice == 3:
        if len(gastos) == 0:
            print("No expenses recorded yet.")
        else:
            for i in gastos:
                total += i
            print(f"Total expense: {total}")
            avrg = total / len(gastos)
            print(f"Average expense: {avrg}")
    elif choice == 4:
        gastos = []
        print("All expenses cleared.")
    else:
        print("Invalid choice. Please try again.")
