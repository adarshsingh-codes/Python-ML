n=int(input("Enter the size of the array: "))
arr=list(map(int,input().split()))
s=set()
found=False
for i in range(n):
    if(arr[i] not in s):
        s.add(arr[i])
    else:
        found=True
        print(arr[i])
        break
if(found==False):
    print(-1)