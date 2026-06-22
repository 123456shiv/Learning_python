text=input("Enter a string: ")

count=0
for ch in text:
    if ch in 'aeiouAEIOU':
        count+=1
print("The number of vowels in the string is:", count)