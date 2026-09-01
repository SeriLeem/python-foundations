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