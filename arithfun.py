def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

print("Arithmetic Functions Module")
print("1. Add Numbers")
print("2. Subtract Numbers")
print("3. Multiply Numbers")
print("4. Divide Numbers")

try:

    choice = int(input("Enter your choice (1-4): "))
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        result = add_numbers(num1, num2)
        print(f"Result: {result}")
    elif choice == 2:
        result = subtract_numbers(num1, num2)
        print(f"Result: {result}")
    elif choice == 3:
        result = multiply_numbers(num1, num2)
        print(f"Result: {result}")
    elif choice == 4:
        result = divide_numbers(num1, num2)
        print(f"Result: {result}")
    else:
        print("Invalid choice. Please select a number between 1 and 4.")

except ValueError as e:
    print(f"Error: {e}")