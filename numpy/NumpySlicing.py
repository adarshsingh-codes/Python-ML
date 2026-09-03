import numpy as np

#numpy array slicing
array=np.array([[1,2,3,4],
               [5,6,7,8],
               [9,10,11,12],
               [13,14,15,16]])

#we will access the array using subscript oeperator

#array[start:end:step]

print(array[0::2])  # from index 0 to the end and with skipping one value,accessing oyl the second one from the inside section choose

print(array[0::-2])

#now lets go for column selection

print(array[:,0]) #the : means all rows and the 0 mean column 0
#array[rows,cols]


print(array[:,2])

print(array[:,0:2]) #this will print the first two columns

print(array[:,1:4]) # start from column 1 to 3

print(array[:,1::2]) #now step is being done even in column

print(array[0:2,0:2]) #rows 0,1 and column 0,1
print(array[0:2,2:4])
print(array[2:,0:2])
print(array[2:,2:4])