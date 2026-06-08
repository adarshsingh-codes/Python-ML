#find the largest digit and smallest digit in the number
n=int(input("Enter the number: "))
maxi=0
mini=9
while n>0:
    digit=n%10
    if digit>maxi:
        maxi=digit
    if digit<mini:
        mini=digit
    n=n//10
print("The max element is:",maxi)
print("The min is :",mini)