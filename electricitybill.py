a=int(input("Enter the units consumed: "))
if a<=100:
    print("No charge")
elif a<=200:
    print("Charge:",(a-100)*5)
else:
    print("Charge:",(a-200)*10+500)