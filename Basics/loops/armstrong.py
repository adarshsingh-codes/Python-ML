n=int(input("Enter the number: "))

original=n
count=0
while original>0:
    count+=1
    original=original//10
sum=0
original=n
while n>0:
    digit=n%10
    sum+=digit**count
    n=n//10
print(sum)
if original==sum:
    print("Yes it is armstrong")
else:
    print("Not armstrong")