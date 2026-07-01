ch=int(input("Enter the number of elements in the list:"))
mylst=[]
for i in range(ch):
    mylst.append(int(input("Enter element:")))

ch2=int(input("Enter the number of elements in the second list:"))
mylst2=[]

for i in range(ch2):
    mylst2.append(int(input("Enter element:")))

mylst.extend(mylst2)
print("The merged list is:", mylst)