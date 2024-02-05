#subset of dataframes
import pandas as pd
mydict={'col1':[1,2,3,4],'col2':[4,6,7,8]
        , 'col3':['four','six','seven','eight']}
df=pd.DataFrame(mydict)
print(df)
print(df.columns)#to print column names
print(df.index)#to know row index
print(len(df))#no of rows
print(df['col1'])# to reterive col1 value
print(df.col1)
print(df[['col1','col3']])#to print multiple columns
print(df[df.col1>1])
print(df[df.col1>1]['col1'])#to print col1 where col1>1
print(df[df.col1>1][['col1','col3']])#to print col1 and col3 where col1>1
print(df[(df.col1>1)&(df.col2!=7)])
print(df[(df.col1>1)&(df.col2!=7)]['col1'])

