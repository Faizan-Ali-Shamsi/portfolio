# Fixed PIN and starting balance
PIN = "1234"
balance = 0.0   # starting balance in PKR


def atm():
    global balance
    # ask for PIN
    entered_pin = input("Enter your 4-digit PIN: ")

    if entered_pin != PIN:
        print("Incorrect PIN. Access Denied.")
        return

    # main ATM menu loop
    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print(f"Your balance is: RS{balance:.2f}")
        elif choice == "2":
            amount = float(input("Enter amount to deposit (RS): "))
            balance += amount
            print(f"Deposited RS{amount:.2f}. New balance: RS{balance:.2f}")
        elif choice == "3":
            amount = float(input("Enter amount to withdraw (RS): "))
            if amount <= balance:
                balance -= amount
                print(
                    f"Withdrawn RS{amount:.2f}. New balance: RS{balance:.2f}")
            else:
                print("Insufficient funds.")
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# run the ATM program
atm()
