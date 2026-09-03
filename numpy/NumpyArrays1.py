import numpy as np

array=np.array('A')    #it is a 0 dimensianla array

print(array.ndim)  #no. of dimensions

array2=np.array(['A','B'])
print(array2.ndim)
print(array2.shape) #It's better to think of this as 2 elements along one axis, rather than "2 rows and no columns."
array3=np.array([['A','B'],['C','D'],['E','F']]) # 2D array
print(array3.ndim)

array4=np.array([
                 [['A','B'],['C','D'],['E','F']],  #each internal elements i shavig 2 elements and it shuldbe consistent in all others too
                 [['G','H'],['I','J'],['K','L']],
                 [['M','N'],['O','P'],['Q','R']]]) # 3D array
print(array4.ndim)

#ndim -number of  dimensions


print(array4.shape)   #(3,3,2) 3 layers,3 rows 3 columns

print(array4[0][0][0])   #chain indexing  for normal python

print(array4[0,0,0])   #in Numpy we have multidiemnsional indexing


word=array4[0,0,0] +array4[2,1,1]+array4[1,1,0]
print(word) # i choose the word API


