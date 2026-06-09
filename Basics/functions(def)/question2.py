def reverseList(nums):
    i=0
    j=len(nums)-1
    while i<j:
        temp=nums[i]
        nums[i]=nums[j]
        nums[j]=temp
        i+=1
        j-=1



n=int(input("Enter the size of the list: "))
nums=list(map(int,input().split()))
print(nums)
reverseList(nums)
print(nums)