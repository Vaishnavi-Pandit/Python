t=str(input('Enter a credit card no : '))
lst=[]
a=len(t)
for i in range(0,a-4):
    lst.append('*')

for i in range(a - 4,a):
    lst.append(t[i])
for i in range(0,len(lst)):
    print(lst[i],end='')




