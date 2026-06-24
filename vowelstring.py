ch=input("Enter a string:")
count=0
for ch in ch:
    if ch in "aeiouAEIOU":
        count+=1
print("Number of vowels =",count)