#NumPy- Numerical Python 

"""Python itself is implemented largely in C (for the standard CPython implementation),
 but Python is not slow simply because its base is built with C. C is actually
   one reason many parts of Python are fast.
"""


"""a library used for Numerical Computing
    Numpy allows us to work with Numpy arrays
    
    NumPy arrays are generally much faster and more memory-efficient
    than Python lists for numerical operations.

    NumPy also supports vectorized operations, allowing us to perform
    operations on entire arrays without explicitly writing Python loops
""" 


#MEANING OF VECTORIZED
import numpy as np

arr=np.array([1,2,3,4])
print(arr*2)

""" Now instead of manually doing [1*2, 2*2, 3*2, 4*2]
    Numpy handles the operations over the whole array using optimized compiled code
"""


import numpy as np

#print(np.__version__)
"""
my_list=[1,2,3,4]

my_list=my_list*2  #this will duplicate the current array

print(my_list)
"""

array=np.array([1,2,3,4])

array=array*2  # now this is used to directly give the values after double nd doesnt duplicate
print(array)
print(type(array))

