ch=input("Enter a character:")
if ch in ('A','a','E','e','I','i','O','o','U','u'):
    print(ch, "is a Vowel")

elif ch in ('B','b','C','c','D','d','F','f','G','g',
            'H','h','J','j','K','k','L','l','M','m',
            'N','n','P','p','Q','q','R','r','S','s',
            'T','t','V','v','W','w','X','x','Y','y',
            'Z','z'):
    print(ch, "is a Consonant")

else:
    print("Invalid Input")