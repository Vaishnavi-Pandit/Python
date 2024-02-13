#accept the no and represent the day.
p=int(input('enter a no'))
if p>7 or p<1:
    print('invalid input')
else:
    if p==1:
        print('Monday')
    elif p==2:
        print('Tuesday')
    elif p==3:
        print('Wednesday')
    elif p==4:
        print('Thursday')
    elif p==5:
        print('Friday')
    elif p==6:
        print('Saturday')
    else:
        print('Sunday')
