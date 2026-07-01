n=int(input("Enter the number of elements:"))
lst=[]
for i in range(n):
    lst.append(int(input("Enter element:")))

visited=[]
for  num in lst:
    if num not in visited:
        count=lst.count(num)
        print(f"{num} occurs {count} times")
        visited.append(num)