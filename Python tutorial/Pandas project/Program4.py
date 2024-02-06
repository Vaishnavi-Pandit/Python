import pandas as pd
import numpy as np
df = pd.read_csv("E:\Python\datasets-df-series/nba.csv")
print(df)
ser=pd.Series(df['Name'])
ser1=pd.Series(df['Age'])
df1=pd.concat([ser,ser1],axis=1)
df1.columns=['playername','playerage']
print(df1)
mydict={'pname': ser,'plage': ser1}
df2=pd.DataFrame(mydict)
print(df2)
arr=np.array([10,20,30,40])
ser=pd.Series(arr)
print(ser)
my_dict={'name': ["a","b","c","d","e"],'age': [10,20,30,40,50],'designation':["ceo","vp","svp","am","dev"]}
ser=pd.Series(my_dict)
print(ser)
names=ser['name']
print(names)
