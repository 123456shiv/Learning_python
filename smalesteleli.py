n=int(input("Enter a the numbers of elements:"))
lst=[]

for i in range(n):

    element=int(input("Enter element"))
    lst.append(element)

smallest=lst[0]

for i in lst:
    if i<smallest:
        smallest=i

print("smallest element:",smallest)