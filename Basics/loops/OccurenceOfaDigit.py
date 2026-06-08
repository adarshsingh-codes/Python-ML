n=int(input("Enter a number: "))
digit1=int(input("Enter the target: "))
count=0
while n>0:
    digit=n%10
    if digit==digit1:
        count+=1
    n=n//10
print("The digit",digit1," appeared ",count," times")