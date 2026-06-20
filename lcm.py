a=int(input("Enter a 1st number:"))
b=int(input("Enter a 2nd number:"))

x=a
y=b

while y!=0:
    x,y=y,x%y

gcd=x
lcm=(a*b)//gcd

print("GCD=",gcd)
print("LCM=",lcm)