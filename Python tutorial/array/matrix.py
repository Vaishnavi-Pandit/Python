from numpy import *
str= '1,2,3;4,6,7;8,9,7'
m2=matrix(str)
arr=array([[2,3,4],[5,6,7],[4,5,6]])
m3=matrix(arr)
m1=matrix(arr)
m1+m3
m1*m3
m1.T#transpose of matrix
m1.transpose()#transpose of matrix
sort(m1)
sort(m1,axis=0)#column wise sorting.
