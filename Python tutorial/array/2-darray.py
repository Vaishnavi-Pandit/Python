<<<<<<< HEAD
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
=======
from numpy import *
arr = array([[1, 2, 3], [6, 7, 8], [5, 6, 7]])
print(arr)
# 3d array
u = array([[[1, 2], [5, 6]], [[6, 7], [8, 9]]])
x = zeros((3, 4), int)
t = ones((3, 4))
yep = eye(5, dtype=int)

y = arr.mean()
z = arr.min()
o = arr[1]
p = arr[2]
aq = arr[0, 0]
mt = arr[0:2, 1:3]
mp = arr[:2, 1:]
lp = arr[1:3, 0:2]
nt = arr[1:, :2]
dt = arr[0:3, 1:2]
pt = arr[:, 1]
print(u, x, t, yep, y, z, o, p, aq, mt, mp, lp, nt, dt, pt)
>>>>>>> f23942d3c37617485cd07ce563557c3b264549a5
