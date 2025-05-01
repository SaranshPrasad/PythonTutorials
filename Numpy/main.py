# Numpy 

import numpy as np 


a = np.array(12) # 0D Array
a1 = np.array([1,2,3,4,5,6,7,8,9,10]) # 1D Array
a2 = np.array([[1,2,3],[4,5,6]]) # 2D Array
a3 = np.array([[[1,2,3],[4,5,6],[7,8,9]]]) # 3D Array

# ndim -> used to check dimensions of array.
# print(a.ndim) # 0
# print(a1.ndim) # 1
# print(a2.ndim)  # 2
# print(a3.ndim)   # 3

a4 = np.array([1,2,3,4,5], ndmin=4) # We can define the number of dimensions by using the ndmin argument.

# Accessing Elements 
# print(a1[0])   # 1
# print(a2[0,0])  # 1
# print(a3[0,1,2]) # 6

# Slicing Arrays
# print(a1[:-1]) # [1 2]
# print(a1[1:]) # [2 3]
# print(a2[0, :-1]) # [1 2]
# print(a1[1:8:2]) # [2 3]
# print(a1[::2]) # Return every second element
# print(a2[1,:-1]) # Slicing in 2d array
# print(a2[0:2,0]) # from both array return element on 0th index
# print(a2[0:2, 0:2]) # -> [[1 2][4 5]]

# Data Types in Numpy 
# dtype -> used to check data type of the array 
# int, float, char, bool
# print(a1.dtype)
# arr = np.array([1,2,3], dtype='S')
# print(arr)
# print(arr.dtype)

# Converting data types 
# newarr = a1.astype('int')
# print(newarr)
# print(newarr.dtype)
# newarr = np.array([1,0,0])
# newarr = newarr.astype(bool)
# print(newarr)

# Copy and View 
# copy -> The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.
# view -> The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.
# base -> check if an array owns it's data or not.
# x = a1.copy()
# x[0] = 200
# print(x.base)
# # print(a1)
# x2 = a1.view()
# print(x2.base)
# # x2[0] = 100
# # print(a1)
# # print(x2)

# Array Shape
# print(a1.shape)
# print(a2.shape)
# print(a3.shape)
# Array reshape 
# print(a1.reshape(2,5)) # Reshape 1d array a1 into 2d array of 2x5 
# Flattening the arrays
# print(a3.reshape(-1)) # makes any dimensions array into oned array
# for x in a3:
#     for y in x:
#         for z in y:
#             print(z)
# arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# The function nditer() is a helping function that can be used from very basic to very advanced iterations. It solves some basic issues which we face in iteration, lets go through it with examples.
# for x in np.nditer(arr):
#   print(x)

# Joining Arrays in Numpy
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr3 = np.array([7,8,9])
newarr = np.concatenate((arr1,arr2,arr3)) # use concatenate function and pass 2 or more arrays as tuples. 
# print(newarr)

new_a = np.concatenate((a2,a2), axis=1) # concatenate 2d arrays  - by default axis = 0, else we can set it to 1 for adding along rows.  0 -> Along Columns 1 -> Along Rows
# print(new_a)

# Adding using Stack
aa  = np.stack((a1,a1)) # Output -> [[ 1  2  3  4  5  6  7  8  9 10][ 1  2  3  4  5  6  7  8  9 10]]
aa  = np.stack((a1,a1), axis=1) # Output -> [[ 1  1][ 2  2][ 3  3][ 4  4][ 5  5][ 6  6][ 7  7][ 8  8][ 9  9][10 10]]
# print(aa)

# Stacking along rows -> hstack()
ar = np.hstack((a1,a1))  # Output -> [ 1  2  3  4  5  6  7  8  9 10  1  2  3  4  5  6  7  8  9 10]
# print(ar) 
# Stacking along columns -> vstack()
ar = np.vstack((a1,a1)) # Output -> [[ 1  2  3  4  5  6  7  8  9 10][ 1  2  3  4  5  6  7  8  9 10]]
# print(ar)
# Stacking along depth (height) -> dstack()
ar = np.dstack((a1,a1)) # Output -> [[[ 1  1][ 2  2][ 3  3][ 4  4][ 5  5][ 6  6][ 7  7][ 8  8][ 9  9][10 10]]]
# print(ar)
# Spliting Arrays
ar = np.array_split(a1,5) # Output -> [array([1, 2]), array([3, 4]), array([5, 6]), array([7, 8]), array([ 9, 10])]
# print(ar)

# Searching Arrays 
x = np.where(a1 == 10)
# print(x) # Output (array([9], dtype=int64),)
# searchsorted() which performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order.
x = np.searchsorted(a1,7)
# print(x)

num = np.array([1,9,2])
frt = np.array(["apple", "kela", "aam"])
# print(np.sort(num)) # [1 2 9]
# print(np.sort(frt)) # ['aam' 'apple' 'kela']
# Filter in Arrays
flt_arr = a1 % 2 == 0 # [False  True False  True False  True False  True False  True]
# print(flt_arr)
n_a = a1[flt_arr] # [ 2  4  6  8 10]
# print(n_a)


# Random in Numpy 
from numpy import random

x = random.randint(100) # gives only integer range 0 - 99 
# print(x)
x = random.rand() # can give floating point number range 0 - 1
# print(x)

# Generate random array 
x = random.randint(10000, size=5)
# print(x)

xx = random.randint(100, size=(2,3))
# print(xx)
x = random.rand(5)
# print(x)
x = random.rand(3,5)
# print(x)
x = random.choice(a1)
# print(x)
random.shuffle(a1)
# print(a1)
# print(random.permutation(a1))

# Visualization : Seaborn is a library that uses Matplotlib underneath to plot graphs. It will be used to visualize random distributions.

import seaborn as sns
import matplotlib.pyplot as plt

# sns.displot(a1)
sns.displot([0, 1, 2, 3, 4, 5], kind="kde")
plt.show()