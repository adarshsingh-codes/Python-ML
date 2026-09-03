import numpy as np

#scaler arithmetic

array=np.array([1,2,3])

print(array+1) #each element would have one added to them
print(array-2) # each element gets 2 subtracted
print(array * 3)   # each element gets multiplied by 3
print(array / 4)   # each element gets divided by 4
print(array ** 5)  # each element gets raised to the power 5

"""
Scalar
   ↓
a single value
array + scalar
   ↓
operation is applied to every element
"""


#Vectorized math function
""" in numpy it is a function that can perform a mathematical operation on 
    every element of an array at once,wihout us writing a Python for loop

"""

array=np.array([1,2,3])
#basically apply a fucntion to an array withut running the loop\


print(np.sqrt(array))

array=np.array([1.01,2.5,3.99])

print(np.round(array))
# to always round down we can use floor

print(np.floor(array))
#to always round up we can use ceil
print(np.ceil(array))

print(np.pi) #pie value


#Exercise
radii=np.array([1,2,3])

#area of circle
print(np.pi* radii**2)



#Element wise arithmetic
"""
    in this we can apply operations between 
    single elemnts between two arrays
"""
array1=np.array([1,2,3])

array2=np.array([4,5,6])


print(array1+array2)
print(array1*array2)
print(array1/array2)
print(array1**array2)



#comprison operators


scores=np.array([91,55,100,73,82,64])

print(scores==100)  #returns boolean array


print(scores>=60)

#wow - in the scores array we are chekcing elemtns and if that is less than 60 then doom it goes to  re assign and become 0
scores[scores<60]=0
#THIS IS CALLED BOOLEAN MASKING / BOOLEAN INDEXING
"""
scores < 60
        ↓
[False, True, False, False, False, False]
        ↓
select elements where True
        ↓
replace those elements with 0
"""
print(scores)

