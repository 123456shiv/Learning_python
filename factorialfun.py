def calculate_factorial(n):
    if n < 0:
        return "Factorial does not exist for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial

    user_input = int(input("Enter a positive integer: "))
    
    result = calculate_factorial(user_input)

try:

    user_input = int(input("Enter a positive integer: "))
    result = calculate_factorial(user_input)

    print(f"The factorial of {user_input} is: {result}")
except ValueError:
    print("Please enter a valid integer.")