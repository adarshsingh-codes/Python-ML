def SumOfDigits(n):
    sum=0
    while(n>0):
        digit=n%10
        sum+=digit
        n=n//10
    return sum

n=int(input("Enter the number: "))
sum=SumOfDigits(n)
print("Sum of digits of",n,"is ",sum)
