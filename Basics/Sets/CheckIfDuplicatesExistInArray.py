n=int(input("Enter the size of the Array: "))
arr=list(map(int,input().split()))

print(arr)

for x in arr:
    print(x,end=" ")

s=set()
print("\n")
if len(arr)!= len(set(arr)):
    print("duplicated exist")
else:
    print("No duplicates")