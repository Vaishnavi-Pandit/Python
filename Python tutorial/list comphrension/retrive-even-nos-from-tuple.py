tp1=(7,5,6,7,8,9)
lt=[]
lst=[]
l1=[]
for i in range(0,len(tp1)):
    if(tp1[i]%2==0 and tp1[i]!=0):
         lt.append(tp1[i])
for i in tp1:
     if(i%2==0):
          lst.append(i)
print(lt)
print(lst)
l1=[i for i in tp1 if i%2==0 and i!=0]
print(l1)