n=int(input("Enter the size of the arr: "))
arr=list(map(int,input().split()))

# maxi=arr[0]
# for i in range(1,n):
#     if maxi<arr[i]:
#         maxi=arr[i]
    
# #count[maxi+1]

# count=[0]*(maxi+1)

# for i in range(n):
#     count[arr[i]]+=1

freq={}
for num in arr:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1

print(freq)

maxi=-1
val=0
for key,value in freq.items():
    if maxi<value:
        maxi=value
        val=key

print(val,maxi)