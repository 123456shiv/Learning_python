string=input("Enter a string:")

result=""
for c in string:
    if c not in result:
        result=result+c

print("The string after removing duplicate characters is:",result)