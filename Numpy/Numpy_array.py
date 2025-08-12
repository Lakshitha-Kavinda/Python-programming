import numpy as np

arr = np.array([2,3,5,6])
print(arr)
print(type(arr))

arr1 = np.array([[1,2,3],[4,5,6]])
# to see the dimension of the array
print(arr1.ndim)

#defining the dimesions using ndim arguement
arr = np.array([1, 2, 3, 4], ndmin=5)



#Accessing elements
#Accessing elements from a 2-D array - treat it as rows and columns
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr[1,2])


arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])


#Slicing arrays is similar to lists
#We can also define the step, like this: [start:end:step].
print(arr[1, 1:4])
print(arr[1:5:2])

#check the datatype
print(arr.dtype)
