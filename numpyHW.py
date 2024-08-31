#NumPy Homework:
import numpy as np

#User inputs a list of numbers, and the program converts this list into a NumPy array
user_input = input("Enter a list of numbers: ")
array = np.array(user_input.split(), dtype = float)

#Find the shape and dimensions of the array
shape = array.shape
dimensions = array.ndim
print("Shape of array: ", shape)
print("Number of dimensions: ", dimensions)

#Reshape the array into a 2x2 matrix (if possible)
if array.size >= 4:
    reshaped_array = array.reshape(2, 2)
    print("Reshaped Array: ", reshaped_array)

#Calculate the sum of all elements in the array
total = np.sum(array)
print("Sum of all elements on array: ", total)