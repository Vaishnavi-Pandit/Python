#add corresponding elements of two list and store them in another list.
lst=[4,6,5,4,9,7]
lst1=[6,7,8,4,5,3]
lt=[]
if len(lst)>=len(lst1):
  
    lt=[lst[i]+lst1[i]for i in range(0,len(lst)) ]

else:
      lt=[lst[i]+lst1[i]for i in range(0,len(lst1)) ]
print(lt)