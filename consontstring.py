ch=input("Enter a string:")
count=0
for ch in ch:
    if ch not in "BCDEFGHIJKLMNOPQRSTUVWXYZbcdefghijklmnopqrstuvwxyz":
        count+=1
print("Number of consonants in the string:", count)
