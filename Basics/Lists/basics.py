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



numbers=[10,20,30,40,50]

#indexing 
print(numbers[0])
print(numbers[3])
print(numbers[-2]) #negative indexing starts from last element so -2 points tothe second last element

#changing values
numbers[1]=25

#adding/removing
numbers.append(60)
numbers.pop()
numbers.remove(30)


#slicing
numbers[1:4]  #means elements from index 1 up to but not including 4

numbers[:3] #index 0,1,2 
numbers[3:] #from index 3 to last
numbers[:] #whole list

numbers[::-1] #reversed

#list comprehension
squares=[x*x for x in numbers]

print(squares)


#witha  condition

evennum=[x for x in numbers if x%2==0]
