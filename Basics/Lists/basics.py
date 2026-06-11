n=int(input("Enter array size: "))
nums=list(map(int,input().split()))
print("The List is: ")
print(nums)


#some operations
print(nums[3:])

print(nums[::-1])

print(len(nums))

print(max(nums))

print(min(nums))

print(sum(nums))

nums.sort()

nums.sort(reverse=True)



squares=[]

for i in range(1,6):
    squares.append(i*i)

print(squares)

