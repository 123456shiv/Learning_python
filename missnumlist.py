n1=int(input("Enter the number of elements in list 1:"))
list1=[]

for i in range(n1):
    list1.append(int(input("Enter element:")))

n2=int(input("Enter the number of elements in list 2:"))
list2=[]

for i in range(n2):
    list2.append(int(input("Enter element:")))

common=list(set(list1) & set(list2))
print("Common elements:", common)