def moveAllZeroes(nums):
    n=len(nums)
    k=0
    for i in range(0,n):
        if(nums[i]!=0):
            nums[k]=nums[i]
            k+=1
    while(k<n):
        nums[k]=0
        k=k+1

n=int(input("Enter the array size:"))
nums=list(map(int,input().split()))

moveAllZeroes(nums)
print(nums)