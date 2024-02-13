lt=[]
lt2=[]
lt=[i for i in input('enter Strings:').split(',')]
print(lt)

'''n= int(input("enter len of list"))
lt2=[input('enter strings:') for i in range(0,n)]
print(lt2)
'''
#sort this list.
for y in lt:
    lt.append(y.strip())#to remove white spaces between strings. 
lt.sort()
print(lt)