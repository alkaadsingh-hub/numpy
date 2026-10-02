import numpy as np

a1 = np.arange(12)                 #1d array
a2 = np.arange(12).reshape(3,4)   #2d array
a3 = np.arange(8).reshape(2,2,2)   #3d array
a4 = np.arange(27).reshape(3,3,3)   #3d array

print(a1)
print(a2)
print(a3)
print(a4)

##INDEXING
#negative indexing and positive indexing:-

print(a1[7])
print(a1[-1])




# accessing 2d array through indexing

print(a2[1,4])    # first we write row(1) and then we mention coloumn(4)
print(a2[0,3])    # first we write row(0) and then we mention coloumn(3)
print(a2[1,2])    # first we write row(1) and then we mention coloumn(2)




 
#accessing 3d array through indexing
 
print(a3[1,1,0])        # first we need to print dimension of array i.e. 3D array is made up of 2D array so first we need to identify 
                          # that how much 2d array is present in array ....indexing start from 0......there is two 2d array is present a3 i.e. 0 and 1 [1,1,0]  1 is 2nd 2d array another 1 is row of 2nd 2d array  and 0 is coloumn of 2nd 2D array.



                                           



##SLICING

#slicing for 1D array:-


print(a1[1:5])        
            
print(a1[1:5:3])       #the last one print the value after skipping the values


#slicing for 2d array:-


print(a2[0,:])         # this will print the whole first row  .....(:)colon means all the row.

print(a2[:,3])         # this will print the coloumn of every row ......it has printed 3rd coloumn of every row. 

print(a2[0:,2:4])      # 0 is representing row comma(,) is representing onwards ....2 is representing coloumn 4 is representing end of column we want to print 2,3,6,7,10,11  we have  written 4 in end as in python last isnot included.

print(a2[::2,1::2])

print(a2[1,::3])       # 1 is representing row.... comma(,) is representing onwards ....3 is representing coloumn  we have  written 3 in end as in python last isnot included.

print(a2[0:2,1:4])     # 0:2 is representing row.... comma(,) is representing onwards ....1:4 is representing coloumn  we have  written 4 in end as in python last isnot included.

print(a2[0:2,1::2])

print(a2[1:3,1::2])



## slicing for 3d array:-

print(a4[2])

print(a4[0,::3])      #this will print the 0th 2d array of a4 and then it will print the 0th row and 3rd coloumn of that 2d array.

print(a4[::2])        #this will print the 0th and 2nd 2d array of a4

print(a4[1,:,1])      #this will print the 1st 2d array of a4 and then it will print the 1st row and 1st coloumn of that 2d array.

print(a4[2,1:,1:])

print(a4[::2,0,::2])    #this will print the 0th and 2nd 2d array of a4 and then it will print the 0th row and 0th and 2nd coloumn of that 2d array.









