n=int(input("Enter the size of first array: "))
arr=list(map(int,input().split()))
s1=set(arr)
n1=int(input("Enter the size of the second element: "))
arr2=list(map(int,input().split()))
s2=set(arr2)


print(s1 &s2)  #this is intersection