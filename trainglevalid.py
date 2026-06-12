a=int(input("Enter the first side: "))
b=int(input("Enter the second side: "))
c=int(input("Enter the third side: "))  
if (a+b>c) and (a+c>b) and (b+c>a):
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")
    