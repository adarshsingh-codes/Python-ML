n=int(input("Enter the size of the array: "))
arr=list(map(int,input().split()))
t=tuple(arr)
maxi=t[0]
for x in t:
    if x>maxi:
        maxi=x
count=[0]*(maxi+1)
for x in t:
    count[x]+=1

for i in range(len(count)):
    if count[i]>0:
        print(i," occurs",count[i]," times")
