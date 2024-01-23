#write a lambda to test given no is even or not:
from functools import reduce


f=lambda x:'even' if x%2==0 else 'not even'
print(f(9))

#to extract even nos from list of numbers.
mylst=[0,2,4,5,3,7,6,8,9]
obj=filter(lambda x:x%2==0 and x!=0, mylst)
print(list(obj))
'''for i in obj:
    print(i)'''
#write the lamda to find squares of the elements of tuple
mytpl=(3,4,5,6,7,2,8)
b=map(lambda x:x*x, mytpl)
print(tuple(b))
#print(list(b))
#create lambda function to calculate product of elements of list.
mylst=[45,67,3,4,6,7,88]
c= reduce(lambda x,y:x*y,mylst)
print(c)