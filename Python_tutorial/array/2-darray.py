
from numpy import*
arr= array([[1,2,3],[6,7,8],[5,6,7]])
print(arr)
#3d array
t=array([[[1,2],[5,6]],[[6,7],[8,9]]])
print(t)
l=zeros((5,6),int)
print(l)
x=ones((3,4),int)
print(x)
print(eye(5,dtype=int))
print(arr.mean())
print(arr.min())
print(arr[1])
print(arr[2])
print(arr[0,0])
print(arr[0:2,1:3])
print(arr[:2,1:])
print(arr[1:3,0:2])
print(arr[1:,:2])
print(arr[0:3,1:2])
print(arr[:,1])

