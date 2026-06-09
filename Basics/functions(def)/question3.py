def movezeroesToEnd(nums):
    n=len(nums)
    k=0
    for i in range(n):
        if nums[i]!=0:
            nums[k]=nums[i]
            k+=1
    while k<n:
        nums[k]=0
        k+=1
        

n=int(input("Enter the size: "))
nums=list(map(int,input().split()))
print(nums)
movezeroesToEnd(nums)
print(nums)

# 3 4 0 0 2 5 3 24 0