#check if the number is prime or not
n=int(input("Enter the number: "))
a=1
if n==0 or n==1:
    a=0
for i in range(2,n):
    if n%i==0:
        a=0
if a==1:
    print("Yes it is a prime number")
else:
    print("No it is not a prime number")