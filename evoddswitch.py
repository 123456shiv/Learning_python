print("===== EVEN / ODD MENU =====")
print("1. Check Even")
print("2. Check Odd")
choice=int(input("Enter the choice: 1 for even, 2 for odd, 3 for invalid input: "))
num=int(input("Enter a number: "))

match(choice):
    case 1:
        if num % 2 == 0:
            print("The number is even.")
        else:
            print("The number is odd.")

    case 2:
        if num % 2 != 0:
            print("The number is odd.")
        else:
            print("The number is even.")

    case 3:
        print("invalid input. Please enter a valid number. ")