count=0
n=int(input("Enter the number: "))
original=n
while n>0:
    digit=n%10
    count+=1
    n=n//10
print("The number of digits in ",original,"is",count)