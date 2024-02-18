q=int(input('enter the cost price of the item: '))
t=int(input('enter the discount: '))
if t<100:
    sp=q-(q*t/100)
    print('price of item after discount: ',sp)
else:
    print('Invalid input')