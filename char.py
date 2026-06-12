ch=input("Enter a character:")
if(ch>='A' and ch<='Z') or (ch>='a' and ch<='z'):
    print(ch, "is an Alphabet")
elif ch>='0' and ch<='9':
    print(ch, "is a Digit")
else:
    print(ch, "is a special character")
