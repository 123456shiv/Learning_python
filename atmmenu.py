menu = int(input("Enter your choice (1-4): "))
balance = int(input("Enter your initial balance: "))

match menu:
    case 1:
        print("Your balance is:", balance)

    case 2:
        amount = int(input("Enter the amount: "))
        balance += amount
        print("Amount deposited successfully.")
        print("Updated balance is:", balance)

    case 3:
        amount = int(input("Enter the amount: "))
        if amount <= balance:
            balance -= amount
            print("Amount withdrawn successfully.")
            print("Remaining balance is:", balance)
        else:
            print("Insufficient balance.")

    case 4:
        print("Thank you for using the ATM. Goodbye!")

    case _:
        print("Invalid choice. Please enter a number between 1 and 4.")