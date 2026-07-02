n=int(input("Enter the number of elements in the list:"))
list1=[]

for i in range(n):
    list1.append(int(input("Enter element:")))

k=int(input("Enter the number of positions to rotate:"))
choice=input("Enter 'L' for left rotation or 'R' for right rotation: ")

k = k % n  

if choice == 'L':
    result = list1[k:] + list1[:k]
    print("Rotated list:", result)
elif choice == 'R':
    result = list1[-k:] + list1[:-k]
    print("Rotated list:", result)

else:
    print("Invalid choice. Original list:", list1)