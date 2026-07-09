num_items = int(input("How many items do you want to add? "))
user_dict = {}
for _ in range(num_items):
    key = input("Enter key: ")
    value = input("Enter value: ")
    user_dict[key] = value

print("\nFinal Dictionary:", user_dict)