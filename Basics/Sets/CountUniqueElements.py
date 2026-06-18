# n=int(input("Enter the number of elements: "))
# s=set()
# for i in range(n):
#     x=int(input())
#     s.add(x)

# print(len(s))



#if an ARRAY was given

n=int(input("Enter the size: "))
arr=list(map(int,input().split()))

print("The number of unique elements is: ",len(set(arr)))

