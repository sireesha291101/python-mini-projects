expenses = []
total = 0
budget = float('inf')

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))

        expenses.append((name, amount))
        total += amount

        print("Expense Added Successfully!")

        if total > budget:
            print("Warning: Budget Exceeded!")

    elif choice == "2":
        print("\n--- Expense List ---")

        for expense in expenses:
            print(expense[0], "-", expense[1])

        print("Total Spending =", total)

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")