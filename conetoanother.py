n=int(input("Enter a number:"))
list1=[]

for i in range(1,n+1):
    list1.append(int(input("Enter a number:")))

list2=list1.copy()

print("original list:",list1)
print("copied list:",list2)