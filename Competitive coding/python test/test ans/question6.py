def count(str):
    p=0
    t=0
    for i in range(0,len(str)):
        if str[i]=='o':
            p=p+1
        elif str[i]=='x':
            t=t+1
    if p==t:
        return 0
    else:
        return 1
t=input('Enter a string: ')
if count(t)==0:
    print('True')
else:
    print('False')

