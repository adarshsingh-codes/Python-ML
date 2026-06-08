#check if the number is palindrome
n=int(input("Enter the number: "))
original=n
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
if original==rev:
    print("Yes palindrome")
else:
    print("Not a palindrome")