#test weather given no is positive or negative
p=int(input('enter a no: '))
if p==0:
    print('It is zero not negative nor positive')
elif p>0:
    print('positive no')
else:
    print('negative no')
    