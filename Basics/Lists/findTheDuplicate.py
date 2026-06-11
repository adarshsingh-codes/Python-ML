def duplicate(nums):
    n=len(nums)
    sum=0
    for i in range(n):
        sum=sum^nums[i]
    return sum

n=int(input("Enter the array size: "))
nums=list(map(int,input().split()))
x=duplicate(nums)
print(x)
