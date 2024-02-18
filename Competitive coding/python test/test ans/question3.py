n=int(input('Enter a no: '))
lst=[]
for i in range(0,n):
    a=int(input('enter list item: ' ))
    lst.append(a)
print(lst)
lst.sort(reverse=False)
print(lst[0])