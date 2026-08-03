print("....Mobile recharge menu....")
print("1. Recharge mobile")
print("2. Check balance")
print("3. View offers")
print("4. Exit")

choice = int(input("Enter your choice: "))
balance =int(input("Enter your current balance: "))
match choice:
    case 1:
        amount=int(input("Enter the amount to recharge: "))
        print("Recharge of ₹", amount, "is successful.")

    case 2:
        print("Your current balance is: ₹", balance)

    case 3:
        print("Available Offers:")
        print("1. ₹199 - 28 Days")
        print("2. ₹299 - 28 Days + 2GB/Day")
        print("3. ₹399 - 56 Days")

    case 4:
        print("Thank you for using our service.")

    case _:
        print("Invalid Choice!")