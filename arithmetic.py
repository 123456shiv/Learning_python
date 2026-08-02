ch=int(input("Enter a choice:"))
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))

match ch:
    case 1:
        c=num1+num2
        print("Addition is:",c)
    case 2:
        c=num1-num2
        print("Subtraction is:",c)
    case 3:
        c=num1*num2
        print("Multiplication is:",c)
    case 4:
        c=num1/num2
        d=num1%num2
        print("Division is:",c)
        print("Remainder is:",d)

    case _:
        print("Invalid choice")


    