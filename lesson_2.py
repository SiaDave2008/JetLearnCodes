#NumPy: Numerical Stuff/library

import numpy as np

#array slicing - chunking the data
'''
array1 = np.array([1,2,3,4,5,6,7,8])

#[starting index : ending index : step/skip] specified range of element wanted, defalut - the first one 

print(array1[0:4])
print(array1[:7])
print(array1[::-1]) #reverse

#multi dimension array
multiarray = np.array([[1,2,3],
                       [4,5,6],
                       [7,8,9]])

print(multiarray[0,0])
print(multiarray[2,1])
'''

#rand - floting point number, randint - integers
'''
array2 = np.random.randint(0, 100, size = (7, 7))
print(array2)
print(" ")
          #[start1:end1, start2:end2]
middlesection = array2[2:5,2:5]
print(middlesection)
'''

#conditional array extraction
'''
array1 = np.array([1,2,3,4,5,6,7,8])

evenArray = array1[array1 % 2 == 0]
print(evenArray)
'''

'''
arrayNew = np.arra([])
for i in range(len(array1)):
    if (array1[i] % 2 == 0):
        arrayNew[i] == array1
print(arrayNew)
'''