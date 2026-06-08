print("Hello")
age=20
print(age)
print(type(age))
# name=input("Enter your name: ")
#print(name)
#marks=int(input("enter your marks: "))
#print(marks)

#cgpa=float(input("Enter your name"))
#print(cgpa)

print(2**3) #2**3 means 2 to the power 3
print(10/3)
print(10//3) #this is integer division

if age>=20:
    print("adult")
else:
    print("not adult")

#pyhton has and,or,not instead of &&,|| !

i=0
while i<5:
    print(i)
    i+=1
print("next")
for j in range(5):
    print(j)
print("next")
#range(10) means 0 1 2 3 4 5 6 7 8 9

for j in range(1,6): #starts from 1 
    print(j)
print("next")
for i in range(1,11,2): #means range is from 1 to 11 with increment of 2 in each loop iteration
    print(i)

a=5
b=10
def add(a,b):
    return a+b;

ans=add(a,b)
print(ans)

#Lists (python arrays)
arr=[10,20,30,40]
print(arr[0])
print(len(arr))

for x in arr:
    print(x)

arr.append(30)

print(arr)

n =int(input())
arr=list(map(int,input().split()))

print(arr)


n = int(input())

arr = []

for i in range(n):
    x = int(input())
    arr.append(x)

print(arr)