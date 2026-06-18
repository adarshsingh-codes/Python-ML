def rotate(nums,n1,n2):
    i=n1
    j=n2-1
    while i<j:
        temp=nums[i]
        nums[i]=nums[j]
        nums[j]=temp
        j-=1
        i+=1

n=int(input("Enter the array size: "))
nums=list(map(int,input().split()))
k=int(input("Enter the rotation index: "))
k = k % n
rotate(nums,0,n)
rotate(nums,0,k)
rotate(nums,k,n)
for i in range(n):
    print(nums[i],end=" ")