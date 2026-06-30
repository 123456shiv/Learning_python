n=int(input("Enter a element:"))
lst=[]
for i in range(n):
    element=int(input("Enter a element:"))
    lst.append(element)

print("Reversed list is:",lst[::-1])