def greet():
    print("hello")

def add(a,b):
    return a+b
#return sends a value back to wherever the function was called.

greet()
n1=int(input("enter num1: "))
n2=int(input("enter num2: "))

result =float(add(n1,n2))
result=int(add(n1,n2))  #this line replace the above line 

print(result) 