n=int(input("Enter a the numbers of elements:"))
lst=[]

for i in range(n):

    element=int(input("Enter element"))
    lst.append(element)

largest=lst[0]

for i in lst:
    if i>largest:
        largest=i

print("Largest element:",largest)