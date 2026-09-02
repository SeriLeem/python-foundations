import numpy as np
#1 making an array and printing its properties
# import numpy as np
# A=np.array([[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14]])
# print(A)
# print(A.dtype) #data type of the array
# print(A.ndim) #number of dimensions
# print(A.shape) #shape of the array
# print(A.itemsize) #size of each element in bytes
# print(A.data) #buffer containing the actual elements of the array
# print(A.size) #total number of elements
# print(A.nbytes) #total number of bytes used by the array

#2 making an array using python list
# import numpy as np
# l1=[1,2,3]
# l2=[1.2,3.5,5.1]

# print(np.array(l1))
# print(np.array(l2))


#3 making an array with range
# A=np.array(range(1,11))
# print(A)
    
#4 making 2D array with np.array()
# A=np.array([[1,2,3],[4,5,6]])
# print(A)


#5 use np.arange() to make an array with regular intervals
# A=np.arange(2, 5, 0.25)
# print(A)
# B=np.arange(0, 10, 2)
# print(B)

#6 use np.arange() to make character type array
# #A=np.arange(1, 10, 1, dtype='str') #this is wrong!
# A=np.arange(1,10,1).astype('str') 
# print(A)

#7
# A=np.arange(0, 3, 1)
# print(A)
# B=np.arange(0,3,1).astype('float32')
# print(B)
# C=np.arange(3, 10)
# print(C)
# D=np.arange(3, 10, 2)
# print(D)


#8 use np.arange() to make 1D, 2D and 3D arrays
# a1=np.arange(0,6)
# print(a1)
# a2=np.arange(0,12).reshape(4,3)
# print(a2)
# a3=np.arange(0, 24).reshape(2,3,4)
# print(a3)

#10 use zeros to make N-dimensional array consisting of 0
# print(np.zeros((3,4)))

#11 make ones to initialize an array with 1
# a=np.ones((2,4))
# print(a)

#12 use zeros_like() and ones_like to make an array of zeros and ones with the same shape and type as a given array
# a=np.zeros_like([1,2,3,4,5])
# print(a)
# b=np.ones_like([[1,2,3],[4,5,6]])
# print(b)
# c=np.zeros_like((3, 4))
# print(c)

#13 use numpy.full to make an array of given shape and type, filled with np.inf(infinity)
# a=np.full((2,2), np.inf)
# print(a)

#14 use np.empty_like to make an uninitialized array with the same shape and type as a given array
# a=np.array([[1,2,3],[4,5,6]])
# print(a)
# a_like=np.empty_like(a)
# print(a_like)

#15