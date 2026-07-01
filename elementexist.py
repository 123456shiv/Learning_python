n=int(input("Enter the number of elements: "))
lst=[]

for i in range(n):
    ele=int(input("Enter the element: "))
    lst.append(ele)

search=int(input("Enter the element to search: "))
found=False

for num in lst:
    if num==search:
        found=True
        break

if found:
    print(f"{search} exists in the list.") 
else:
    print(f"{search} does not exist in the list.")