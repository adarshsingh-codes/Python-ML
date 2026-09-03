t=(10,20,30)  #this is a tuple

#t[0]=1000  #this will give error as tuple does not support item assignment
#tuples cant be modified

print(t)
t1=tuple([1,2,3,4,5,5])
print(t1)
print(t[0])
print(t[1])

for x in t:
    print(x)

print(len(t1))



print(20 in t)
print(30 in t1)

print(t1[1:4]) # here 1 is inclusive and 4 is not 


#this is some tple packing
#pyhton automaticaly packs value into a tuple
t2=10,20,30,40
print(t2)

#tuple unpacking
a,b,c,d=t2
print(a)
print(b)
print(c)
print(d)



#single element tuple
t3=(5)     # this leads to integer

print (type(t3))

t3=(5,) # this is a single element tuple
print(type(t3))


#some built in functions

print(min(t))
print(max(t))
print(sum(t))
print(len(t))





#A tuple is basica;;y a list that cant be chaned after creation
point=(10,20)

print(point[0])
print(point[1])

point[0]=60  #tis wont work as it is immutable



#tuples can bethis way

shape=(10,20)


#or functions returning multiple values

def get_data():
    return 10,20

#then 
x,y=get_data()




#example

tu=(10,20,30,40)

arr=list(tu)
print(arr)

tup=tuple(arr)