num=float(input("Enter a number:"))
operation=input("Enter an operation (+, -, *, /):")
num2=float(input("Enter another number:"))

if operation=='+':
    print("result=",num+num2)

elif operation=='-':
    print("result=",num-num2)

elif operation=='*':
    print("result=",num*num2)

elif operation=='/':    
    if num2!=0:
        print("result=",num/num2)
    else:
        print("Error: Division by zero is not allowed.")        
else:
    print("Invalid operation. Please enter one of +, -, *, or /.")  

