expenses = []

while True:
    print("\n1. Add Expense")
    print("2. Show Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")

        expenses.append((amount, category))
        print("Expense Added")

    elif choice == "2":
        print("\nAll Expenses:")
        for expense in expenses:
            print(expense)

    elif choice == "3":
        total = 0
        for expense in expenses:
            total += expense[0]

        print("Total Expense:", total)

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice")
