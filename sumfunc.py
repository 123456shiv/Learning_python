def sum_of_n(n):

    sum=0
    for i in range(1,n+1):
        sum+=i
    return sum

num=int(input("Enter a number: "))
print(sum_of_n(num))