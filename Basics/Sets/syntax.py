#no duplicates allowed

#set is a collection of unique elements

#creating a set

s1={1,2,3,4,5,6}  #method 1

s=set([1,2,3,4,5]) #method 2

s=set()  #empty set

print(s1)
print(type(s1))


# s={} this creates a dictionary

n=int(input("Enter size: "))
s2=set()
for i in range(n):
    x=int(input())
    s2.add(x)

print(s2)

s2.add(49)

s2.add(344)

s2.remove(49)
s2.discard(9)

print(s2)


s3={10,20,30,40}

print(20 in s3)
print(80 in s3)


for x in s3:
    print(x)

print(len(s3))


#convert list to set

arr=[1,2,3,4,5,6,6,7]

s4=set(arr)

print(s4)

# Creating sets
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("A =", a)
print("B =", b)

# add()
a.add(10)
print("After add(10):", a)

# remove()
a.remove(10)
print("After remove(10):", a)

# discard()
a.discard(100)  # No error
print("After discard(100):", a)

# pop()
temp = a.copy()
print("Popped element:", temp.pop())

# union
print("Union:", a.union(b))
print("Union using | :", a | b)

# intersection
print("Intersection:", a.intersection(b))
print("Intersection using & :", a & b)

# difference
print("Difference A-B:", a.difference(b))
print("Difference using - :", a - b)

# symmetric difference
print("Symmetric Difference:", a.symmetric_difference(b))
print("Using ^ :", a ^ b)

# subset
print("{1,2} subset of A ?", {1, 2}.issubset(a))

# superset
print("A superset of {1,2} ?", a.issuperset({1, 2}))

# disjoint
print("{7,8} disjoint with A ?", {7, 8}.isdisjoint(a))

# membership
print("3 in A ?", 3 in a)
print("20 in A ?", 20 in a)

# length
print("Length of A:", len(a))

# max, min, sum
print("Max:", max(a))
print("Min:", min(a))
print("Sum:", sum(a))

# sorted
print("Sorted A:", sorted(a))

# copy
c = a.copy()
print("Copy of A:", c)

# update
c.update(b)
print("After update:", c)

# intersection_update
d = a.copy()
d.intersection_update(b)
print("After intersection_update:", d)

# difference_update
e = a.copy()
e.difference_update(b)
print("After difference_update:", e)

# symmetric_difference_update
f = a.copy()
f.symmetric_difference_update(b)
print("After symmetric_difference_update:", f)

# clear
g = a.copy()
g.clear()
print("After clear:", g)
