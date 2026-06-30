n=int(input("Enter the number of elements:"))
lst=[]
for i in range(n):
    element=(int(input("Enter element:")))
    lst.append(element)

avg=sum(lst)/len(lst)
print("Average of list element:",avg)
