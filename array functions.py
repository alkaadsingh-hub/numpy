import numpy as np

a = np.random.random((3,4))

#1. max function

print(a)
print(np.max(a))    #provide maximum element from matrix



#2. min function

print(np.min(a))    #provide minimum element from matrix



#3. sum function 

print(np.sum(a))



#4. product function

print(np.prod(a))


#  THE MUST PART OF NUMPY IS IT PROVIDE FLEXIBLITY 

#  Now we will find the min,max,sum......and so on from all rows and coloumn of matrix

# 0 is used to axix coloumn and 1 is used to axis row

print(np.min(a,axis=1))
print(np.max(a,axis=1))
print(np.sum(a,axis=1))
print(np.prod(a,axis=1))



print(np.min(a,axis=0))
print(np.max(a,axis=0))
print(np.sum(a,axis=0))
print(np.prod(a,axis=0))



#statistical operation

#1.mean function

print(np.mean(a))    #we can also axis or can print mean of all rows and coloumn seperately by using axis =1,axis=0 respectively

#2. meadian 
#it will sort the element and provide mid value 

print(np.median(a))

#3. standard deviation

print(np.std(a))

#4. variance

print(np.var(a))



#trignometry function

#1.sin
#2.cos
#3.tan

print(np.sin(a))

print(np.cos(a))

print(np.tan(a))




##dot product function

#dot product we do multiplication between two matrices and to do that there is a condition that the coloumn of first matrix must be equal to the row of second matrix then only dot product is possible 
# AND the final otput or matrix must be equal to row of first matrix and coloumn of second matrix
#i.e.  (3,4) (4,3)   and its output must be = (3,3)


a1 = np.arange(12).reshape(3,4)
a2 = np.arange(12,24).reshape(4,3)

print(a1)
print(a2)

# dot product
print(np.dot(a1,a2))        #matrix will form of (3,3)



# #log and exponent function

# Exponent means raising a number to a power
# A logarithm tells you what power is needed to get a number.

print(np.log(a1))
print(np.exp(a2))



#round function   it round  off the value to its nearest integer
a3 = np.random.random((2,3))*100
print(a3)      #got floating values
#now i want  to print a3 in int so we will use round function todo that

# a3 = np.round(np.random.random((2,3))*100)
print(a3)



#floor function   
#it moves back side of int value example at 6.9 it will give us 6.

a3 = np.floor(np.random.random((2,3))*100)
print(a3)



#ceil function
#it moves forward side of int value example at 5.1 it will give the utput of 5.

a3 = np.ceil(np.random.random((2,3))*100)
print(a3)

