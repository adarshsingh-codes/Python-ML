a=int(input("enter the first side length: "))
b=int(input("enter the second side length: "))
c=int(input("enter the third side length: "))

if a+b>c and b+c>a and a+c>b:
    print("Valid triangle")
else:
    print("Invalid triangle")
