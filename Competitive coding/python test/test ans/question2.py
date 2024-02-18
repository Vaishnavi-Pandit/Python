n=int(input('Enter a no: '))
lst=[]
for i in range(0,n):
    a=int(input('enter list item: ' ))
    lst.append(a)
print(lst)
s=int(input('Enter 1 for asc and 2 for desc: '))
if s==1:
    lst.sort(reverse=False)
    print(lst)
elif s==2:
    lst.sort(reverse=True)
    print(lst)
else:
    print('invalid input')


