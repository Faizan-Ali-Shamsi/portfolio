expense = []

while True:
    print("Welcome to the Expense Tracker CLI!")

    print("1. Add expense")
    print("2. View expenses")
    print("3. Summary")
    print("4. Quit")

    choice = input("1/2/3/4: ")

    if choice == "4":
        print("Good bye!")
        break

    elif choice == "1":
        print("You chosed option: 1")
        Catogary = input("Enter catogary: ")
        Amount = input("Enter amount: ")
        expense.append({"Catogary": Catogary, "Amount": Amount})
        print("Expense added.")

    elif choice == "2":
        print("You chosed option: 2")
        if not expense:
            print("No expenses yet.")
        else:
            print("EXpenses: ")
            for exp in expense:
                print(f"{exp['Catogary']} - {exp['Amount']}")

    elif choice == "3":
        print("You chosed option: 3")
        if not expense:
            print("No expenses yet.")
        else:
            total = 0
            for exp in expense:
                total += float(exp['Amount'])
                print(f"Total spent: {total}")

    else:
        print("Invalid choise, try again!")
