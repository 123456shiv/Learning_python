n = int(input("Enter number of sublists: "))

nested_list = []

for i in range(n):
    sublist = list(map(int, input("Enter elements separated by space: ").split()))
    nested_list.append(sublist)

flat_list = []

for sublist in nested_list:
    for num in sublist:
        flat_list.append(num)

print("Flatten List:", flat_list)