#ex1 understanding the properties of an array
# import numpy as np
 
# A=np.array([[1,2,3],[4,5,6]])
# print(A)
# print('data type:', A.dtype)
# print('array dimension:', A.ndim)
# print('array size:', A.shape)
# print('bytesize of array:', A.itemsize)
# print('array data:', A.data)

#ex2 making array using python list
# import numpy
# list1=[1,2,3,4]
# a=numpy.array(list1)
# print(a)
# print(a.shape)
# b=numpy.array([[1,2,3],[4,5,6]])
# print(b)
# print(b.shape)

#ex3 making 2D, 3D arrays in float type
# import numpy as np
# print('===============2D array===============')
# arr1=[(1,2,3),(4,5,6)]
# a1=np.array(arr1, dtype=float)
# print(a1)

# print('===============3D array===============')
# arr2=np.array([[[1,2,3],[4,5,6]], [[3,2,1],[4,5,6]]], dtype=float)
# a2=np.array(arr2, dtype=float)
# print(a2)

#ex4 designate a data type and make arrays usign various methods. 
# import numpy as np

# #method1
# x_float64=np.array([1.4, 2.6, 3.0, 4.9, 5.32], dtype=np.float64)
# print(x_float64.dtype)
# print(x_float64)
# print()

# #method2
# x_float64_1=np.array([1.4, 2.6, 3.0, 4.9, 5.32], dtype='f8')
# print(x_float64_1.dtype)
# print(x_float64_1)
# print()

# #method3
# x_float64_2=np.float64([1.4, 2.6, 3.0, 4.9, 5.32])
# print(x_float64_2.dtype)
# print(x_float64_2)

#use zeros() method to initialize an array with 0
# import numpy as np
# A1=np.zeros(6)
# print(A1)

# A2=np.zeros((2,3))
# print(A2)

# A3=np.array([[1,2], [3,4], [5,6]], dtype=np.int32)
# for x in np.nditer(A3, order='C'): #Cstyle, row prioritized
#     print(x,end=' ')

# print()
# A4=np.array([[1,2],[3,4],[5,6]], dtype=np.int64, order='C')
# for x in np.nditer(A4, order='F'): #Fortran style, column prioritized
#     print(x, end=' ')

#6 make arrays initialized with variety of values
# import numpy as np

# A=np.ones((2,3))
# print('=====A====')
# print(A)

# B=np.empty((2,3))
# print('====B====')
# print(B)

# C=np.full((2,3),20,dtype=np.int32)
# print('====C====')
# print(C)

# D=np.ones((2,3,4),dtype=np.int16)
# print('===D===')
# print(D)


#ex7 make consecutive data using np.arange() method
# import numpy as np

# x1=np.arange(4)
# print(x1)
# x2=np.arange(3.0)
# print(x2)

# x2=np.arange(3,10)
# print(x2)

# x3=np.arange(3,10,2)
# print(x3)


#ex8 use like method to make an arary with same dimension 
# import numpy as np
# a=np.array([[1,2,3],[4,5,6]])
# b1=np.zeros_like(a)
# b2=np.ones_like(a)
# b3=np.full_like(a,5)

# print(b1)
# print(b2)
# print(b3)

#ex9
import numpy as np

x=np.linspace(0,99,100)
print(x)

x1=np.linspace(0,99,25)
print(x1)

x2=np.linspace(1,6,5,endpoint=False) #do not include the enpoint
print(x2)
 