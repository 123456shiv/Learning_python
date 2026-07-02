n = int(input("Enter the number of elements: "))

lst = []

for i in range(n):
    lst.append(int(input("Enter element: ")))

even_list = [num for num in lst if num % 2 == 0]
odd_list = [num for num in lst if num % 2 != 0]

print("Even List:", even_list)
print("Odd List:", odd_list)