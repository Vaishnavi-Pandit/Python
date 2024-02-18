n=int(input('enter a no: '))
t=input('Enter a operator: ')
q=int(input('enter a no: '))
if t=='+':
    y=n+q
elif t=='-':
    y=n-q
elif t=='*':
    y=n*q
elif t=='/':
    y=n/q
elif t=='%':
    y=n%q
elif t=='//':
    y=n//q
else:
    print('Invalid operator')
print(y)
