a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
operator = input("Enter an operation (+, -, *, /): ")

# Python uses 'match', not 'switch'
match operator:
    case '+':
        print("result=", a + b)
    case '-':
        print("result=", a - b)
    case '*':
        print("result=", a * b)
    case '/':
        if b != 0:
            print("result=", a / b)
        else:
            print("Error: Division by zero is not allowed.")
    case _:  # Default wildcard case requires an underscore
        print("Invalid operation. Please enter one of +, -, *, or /.")