import numpy as np


#aggregate fucntions = summarize data and typically return a single value
array=np.array([[1,2,3,4,5],[6,7,8,9,10]])

print(np.sum(array))
print(np.mean(array))

print(np.std(array))

print(np.min(array))
print(np.min(array))
print(np.max(array))


#position for minimum value and max
print(np.argmin(array))
print(np.argmax(array))


print(np.sum(array,axis=0))   #if axis is 0 then we appluy it to all the columns

print(np.sum(array,axis=1))   #if axis is 1 then we sum all the rows


