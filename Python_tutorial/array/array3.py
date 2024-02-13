from numpy import *

arr = array([7, 8, 6, 5, 4, 5, 7, 6])
x = arr
arr[0] = 10  # now x will also change
z = arr.view()  # shallow copy it will show the changes on arr array on x array.
y = arr.copy()  # deep copy changes in arr will not be shown in x.
print(arr.ndim)
# two dimensional array
array = array([[1, 3, 4], [4, 5, 6]])
print(arr.shape)
print(array.shape)
print(array.itemsize)  # float no will take the 8 bytes and int no will take 4 bytes
print(arr.size)
print(arr.dtype)
print(arr.nbytes)
print(arr.reshape(2, 4))
print(array.flatten())
