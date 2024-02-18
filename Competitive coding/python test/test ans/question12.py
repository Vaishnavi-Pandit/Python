import pandas as pd
lst=list(input('Enter a string: ').split(','))
lst1=[]
for i in range(0,len(lst)):
    lst1.append(lst[i])
lst2=pd.unique(lst1)
print(lst2)



