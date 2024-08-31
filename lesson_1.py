#NumPy: Numerical Stuff/library

import numpy as np

'''
list1 = [1,2,3,4,5]
'''

#convert list to array
'''
my_array = np.array(list1)
print(my_array)
print(list1)
'''

'''
arr = np.array( [[1,2],[3,4],[5,6]] )
'''

#Num of dimensions
#print(arr.ndim)
#Shape of array
#print(arr.shape)

#Multi numpy arrays
'''

array3D = np.array(
    [[[1,2],
      [3,4],
      [5,6]],

     [[7,8],
      [9,10],
      [11,12]]]
    )
'''

#print(array3D)
#print(array3D.ndim)
#print(array3D.shape)

#accessing the elements in 1D, 2D and 3D arrays
'''
print(arr[1,1])
print(my_array[1])
print(array3D[1,2,1])
'''

#arange func - (start, end, skip/step), default - 1, generates an even spaced values within a given range of an array 
'''
array1 = np.arange(0,10,2)
print(array1)
'''

#reshape - reshape a data (ex: 2d to 3d), must be multiples of the num given, 
# the product of the dimensions in the new shape must be the same as the product of the dimensions in the original shape
'''
array1 = np.arange(6)
reshape_array = array1.reshape(2,3)
print(array1)
print(reshape_array)
'''

'''
array4 = np.arange(12)
reshape_array1 = array4.reshape(2,3,2)
print(array4)
print(reshape_array1)
'''

#randomized array or shuffled
'''
permuted_array = np.random.permutation(array4)
print(permuted_array)
'''

#sorting arrays
'''
array5 = np.array([2, 7, 4, 9, 12, 3, 8])
sorted_arr = np.sort([array5])
print(sorted_arr)
'''

#NumPy is more mathemaically advanced/complex and efficent then list, 
# takes up less space because of the lack of data types.

#endbites - number of bites consumed
'''
array1 = np.array([1,2,3,4,5,6])
print(array1.nbytes)
'''

#Generate a 7x7 matrix using random
#rand - floting point number, randint - integers
'''
array2 = np.random.randint(0, 100, size = (7, 7))
print(array2)
print(" ")
array3 = np.random.rand(7, 7)
print(array3)
'''