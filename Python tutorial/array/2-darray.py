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
