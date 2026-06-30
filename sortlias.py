n=int(input("Enter the element:"))
lst=[]
for i in range(n):
    element=int(input("Enter a element"))
    lst.append(element)

print("Sorted list is:",sorted(lst))