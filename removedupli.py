n=int(input("Enter the element:"))
lst=[]

for i in range(n):
    element=int(input("Enter a element:"))
    lst.append(element)


result=list(set(lst))
print("list after removing duplicate elements:",result)