import numpy
r,c=[int (i) for i in input ("how many rows, columns").split(',')]
arr=numpy.zeros((r,c),int)
print('enter elements:')
for i in range(r):
    arr[i]=[int(x) for x in input().split]
m=numpy.matrix(arr)
print('transpose matrix:')
m1=m.transpose()
print(m1)