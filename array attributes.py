# Array attributes

# 1.ndim
#ndim provide the dimension of array

import numpy as np
a = np.arange((10))
b = np.arange(16).reshape(4,4)
c = np.arange(18).reshape(3,3,2) #where 3 is number of rows, 3 is number of columns and 2 is number of depth

print(a)
print(b)
print(c)

print(a.ndim)
print(b.ndim)
print(c.ndim)



#2. shape
#this tell us about the dimensions i.e. how many rows nd coloumn are there in dimension.
print(a.shape)
print(b.shape)
print(c.shape)



#3. size
#ittellthe number of iteam
print(a.size)
print(b.size)
print(c.size)



#4. itemsize
#how size is occupied by each iteam

print(a.itemsize)
print(b.itemsize)
print(c.itemsize)



#5. dtypes
#tells the datatype of an element


print(a.dtype)
print(b.dtype)
print(c.dtype)


