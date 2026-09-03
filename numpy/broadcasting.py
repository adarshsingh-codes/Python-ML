import numpy as np
"""
Broadcasting allows NumPy to perform operations on arrays
with different shapes by virtually expanding dimensions
so they match the larger array's shape.

For corresponding dimensions:
    - They must have the same size
    OR
    - One of the dimensions must have size 1.
"""

#we read the dimentions from left ro right by the above 2 rules#and this holds for both row and column

array1=np.array([[1,2,3,4]])
array2=np.array([[1],[2],[3],[4]])
print(array1.shape)
print(array2.shape)

print(array1*array2)



arr1=np.array([[1,2,3,4,5,6,7,8,9,10]])
arr2=np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[20]])

print(arr1.shape)
print(arr2.shape)

print(arr1*arr2)


