n=int(input("Enter the element:"))
lst=[]

for i in range(n):
    element=int(input("Enter element:"))
    lst.append(element)

print("sum of list element:",sum(lst))