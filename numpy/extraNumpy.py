import numpy as np

#reshape() changes the shape of an array without changing its value

array=np.arange(1,13)
print(array)
print(array.shape)

reshaped=array.reshape(3,4)
"""
    3,4 worked cuz 3*4 was 12 but 5*3 wont work cuz its not ewual to 12
"""

print(reshaped)
print(reshaped.shape)




#flatter() and ravel()   - these convert multidimensional array into 1D array
array1=np.array([[1,2,3,4],[5,6,7,8]])

print(array.flatten())
print(array.ravel())



"""
reshape → change shape

flatten → make a 1D copy

ravel → make a 1D representation
"""


#transpose - basically swap the axes of a 2d array

array=np.array([[1,2,3],[4,5,6]])

print(array)
print(array.T)

#concatenate
a=np.array([1,2,4])
b=np.array([3,4,5])

print(np.concatenate((a,b)))

#stack

#stack combines arrays by creating a new dimension

a1=np.array([1,2,3])
b1=np.array([4,5,6])

print(np.stack((a,b)))

#concatenate() joins along an existing axis, while stack() creates a new axis.

arr1=np.array([1,2,3,4,5])
print(array.dtype)
arr1=arr1.astype(float)
print(arr1)
print(arr1.dtype)



#copy  They are independent.
array3 = np.array([1, 2, 3])
new_array = array.copy()
new_array[0] = 100
print(array3)
print(new_array)


#view  Changing the view affected the original
array5 = np.array([1, 2, 3])
view= array.view()
view[0] = 100
print(array5)

a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [5, 6],
    [7, 8]
])

print(a * b)  #* means element wise multiplication
print(a @ b)  #@ means matriz multiplication



a3 = np.array([1, 2, 3])
b4 = np.array([4, 5, 6])

print(np.dot(a3, b4))  # 1*4+2*5+3*6

np.zeroes(5) #[0. 0. 0. 0. 0.]


np.linspace(0, 1, 5)  #[0.   0.25 0.5  0.75 1.  ]

np.full(5, 7) #[7 7 7 7 7]