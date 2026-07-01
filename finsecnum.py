n = int(input("Enter the number of elements: "))

lst = []

for i in range(n):
    lst.append(int(input("Enter element: ")))

lst.sort()

print("Second Largest Element:", lst[-2])