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
# import numpy as np

# x=np.linspace(0,99,100)
# print(x)

# x1=np.linspace(0,99,25)
# print(x1)

# x2=np.linspace(1,6,5,endpoint=False) #do not include the enpoint
# print(x2)
 
#ex10 forming an unit matrix using identity() and eye() methods
# import numpy as np
# print('===4x4===')
# D=np.identity(4)
# print(D)

# print('===exp===')
# D=np.identity(3, dtype=int)
# print(D)
# print()

# print('===3x3===')
# E1=np.eye(3,dtype=int)
# print(E1)

# print('===2x3===')
# E1=np.eye(2,3, dtype=int)
# print(E1)

# print('===start from 0 column===')
# E2=np.eye(3,k=0,dtype=int)
# print(E2)
# print('===start from 1 column===')
# E3=np.eye(3,k=-1,dtype=int)
# print(E3)

#ex11 form an array using linspace() and logspace() methods
# import numpy as np
# print('===linspace===')
# print(np.linspace(0.0, 10.0, num=5))#
# print(np.linspace(0.0, 10.0, num=5, retstep=True)) #return the calculated step size along with the array of numbers
# print(np.linspace(0.0, 10.0, num=5, endpoint=False, retstep=True))
# print()
# print('===logspace===')
# x1=np.logspace(0.1, 1, num=10)
# print(x1)
# y=np.linspace(1,10, num=10, dtype=int)
# print(y)
# print('===converting y to float64===')
# print(y.astype('float64'))

#ex12 Kim's salary was 100000 when she was 30 and 1000000 when she was 60.
# case 1 - her salary increases as a linear correlation
#case 2 - her salary increases exponentially
# compare her salary when she is 40 and 50, respectively for both cases


#ex13 convert datatypes
# import numpy as np
# x_float64=np.array([1.4, 2.6, 3.0, 4.9, 5.32], dtype=np.float64)
# print(x_float64.dtype)
# print(x_float64)
# print('\nconverting float64 to int64')
# x_int64=x_float64.astype(np.int64)
# print(x_int64.dtype)
# print(x_int64)
# print('\nconverting float64 to int64')
# x_int64_2=np.int64(x_float64)
# print(x_int64_2.dtype)
# print(x_int64_2)

# print('\nconverting float64 to string')
# x_string=x_float64.astype(np.strings_) #AttributeError: `np.string_` was removed in the NumPy 2.0 release. Use `np.bytes_` instead.
# print(x_string.dtype)
# print(x_string)

# print('\nconverting string to float64')
# x_from_string_to_float64=x_string.astype(np.float64)
# print(x_from_string_to_float64.dtype)
# print(x_from_string_to_float64)

#ex14 selecting elements you want
# import numpy as np

# vector=np.array([1,2,3,4,5,6])
# matrix=np.array([[1,2,3], [4,5,6], [7,8,9]])
# print(vector[:3]) #[1 2 3]

# print(vector[3:]) #[4 5 6]

#ex15 using a list to select elements
# import numpy as np

# matrix=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(matrix[[0,2]])
# print(matrix[[0,2], [1,0]])

#ex16 ave arrays using save() method
# import numpy as np

# a=np.random.randint(0,10,(2,3))
# b=np.random.randint(0,10,(2,3))
# print(a)
# print(b)

# #save 1 array as a file
# np.save("d:/data/my_array1", a)

# #save a number of arrays as files
# np.savez("d:/data/my_array2", a, b)

#ex17 use numpy.savetxt() to store array as a textfile
# import numpy as np
# x=np.array([1,2,3,4])
# y=np.array([5,6,7,8])
# z=np.array([9,10,11,12])

# np.savetxt('d:data/array_x.csv', x, delimiter=',') #a delimiter is a character or string used to separate individual data values within a text file when reading or writing arrays.
# np.savetxt('d:data/array_xy.csv', (x,y))
# np.savetxt('d:data/array_z.csv', z, fmt='%1.4e') #result: [9.0000e+00, 1.0000e+01, 1.1000e+01, 1.2000e+02]

#ex18 load the files you stored in ex17
# import numpy as np
# a=np.load("d:/data/my_array1.npy")
# print(a)
# print()

# #loading several files
# npzfiles=np.load("d:/data/my_array2.npz")
# print(npzfiles['arr_0'])
# print(npzfiles['arr_1'])


#ex19 load a text file

# import numpy as np

# a1=np.loadtxt('d:/data/data1.csv')
# a2=np.loadtxt("d:/data/data1.csv", dtype=np.int)
# print(a1)
# print(a2)

#ex19 use numpy.loadtxt to load data from a textfile
import numpy as np
x=np.array([1,2,3,4])
y=np.array([5,6,7,8])
z=np.array([9,10,11,12])

np.savetxt('array_x.csv', x, delimiter=',')
np.savetxt('array_xy.csv', (x,y))
np.savetxt('array_z.csv', z, fmt='%1.4e')

load_x=np.loadtxt('array_x.csv')
load_xy=np.loadtxt('array_xy.csv')
load_z=np.loadtxt('array_z.csv')
print(load_x)
print(load_xy)
print(load_z) #Your last print() does not show scientific notation because np.savetxt only formats the text inside the saved file, whereas np.loadtxt reads those values back into memory as standard floating-point numbers.

