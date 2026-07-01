n=int(input("Enter the number of elements:"))
lst=[]

for i in range(n):
    element=int(input("Enter the element:"))
    lst.append(element)
remove=int(input("Enter the element to remove:"))

if remove in lst:
    lst.remove(remove)
    print("updated list:", lst)

else:
    print("Element not found in the list.")