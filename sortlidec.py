n=int(input("Enter the number of elements:"))
lst=[]
for i in range(n):
    element=int(input("Enter an element:"))
    lst.append(element)
lst.sort(reverse=True)
print("The sorted list is:", lst)  