#find the prime nunmbers in the range
n1=int(input("Enter the lower limit: "))
n2=int(input("enter the upper limit: "))
for i in range(n1,n2+1):
    a=1
    if i==0 or i==1:
        a=0
    for j in range(2,i):
        if i%j==0:
            a=0
            break
    if a==1:
        print(i)