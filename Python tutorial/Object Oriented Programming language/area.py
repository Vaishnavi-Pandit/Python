from rectangle import *

lst=[int(i) for i in input('enter the sides: ').split()]
p1=Rectangle()
if len(lst)==2:
    a=lst[0]
    b=lst[1]
    p1.setareaofrect(a,b)
    print(p1.getareaofrect())
elif len(lst)==1:
    a=lst[0]
    p1.setareaofsquare(a)
    print(p1.getareaofsquare())

else:
    print('invalid input')