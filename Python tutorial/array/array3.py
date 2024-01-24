from numpy import *
arr=[7,8,6,5,4,5,7,6]
x=arr
arr[0]=10#now x will also change
x=arr.view()#shalow copy it will show the changes on arr array on x array.
x=arr.copy()#deep copy changes in arr will not be shown in x.
arr.ndim
#two dimentional array
array=([[1,3,4],[4,5,6]])
arr.shape
array.shape
array.itemsize#float no will take the 8 bytes and int no will take 4 bytes
arr.size
arr.dtype
arr.nbytes
arr.reshape(2,4)
arr.flattern()