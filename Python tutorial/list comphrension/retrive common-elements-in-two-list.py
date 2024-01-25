lst=[9,8,7,6,5]
lst2=[9,8,7,6,5]
lt=[]
lt2=[]
for x in lst:
    for y in lst2:
        if x==y:
            lt2.append(x)
print(lt2)
lt=[x for x in lst for y in lst2 if x==y]
print(lt)