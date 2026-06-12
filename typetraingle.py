a=int(input("Enter the first side: "))
b=int(input("Enter the second side: "))
c=int(input("Enter the third side: "))
if (a==b) and (b==c):
    print("The triangle is an equilateral triangle.")   
elif (a==b) or (b==c) or (a==c):
    print("The triangle is an isosceles triangle.")
else:
    print("The triangle is a scalene triangle.")
    