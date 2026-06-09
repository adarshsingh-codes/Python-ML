#best time to byt and sell stock

def besttime(nums):
    n=len(nums)
    mini=nums[0]
    maxi=0
    for i in range(1,n):
        if nums[i] <mini:
            mini=nums[i]
        profit=nums[i]-mini

        if profit>maxi:
            maxi=profit
    return maxi


n=int(input("Enter the array size: "))
nums=list(map(int,input().split()))
print(nums)
n1=besttime(nums)
print(n1)