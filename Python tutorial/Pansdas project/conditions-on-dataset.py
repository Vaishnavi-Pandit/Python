import pandas as pd

df = pd.read_csv('E:\Python\datasets1\shoppingmall.csv')
print(df.Score)
print(df.Score, df.Age)
print(df['Score'][df['Score'] > 50])
print(df[:][df['Score'] > 50])
print(df['Score'] > 90)
print(df[df['Score'] > 90])
print(df[df['Score'] > 90]['Gender'])
print(df[df['Score'] > 90][['Gender', 'Age']])
# reterive the rows where empid>1004
print(df[df['Age'] > 20])
print(df[df.Age > 50])
print(df[(df.Age > 50) & (df.Score < 10)])
print(df[(df.Score < 30) | (df.Score > 90)])
print([df[(df['Score']>50)&(df['Score']<20)]])
print(df.index)
df1=df.set_index('ID')
print(df1)
print(df1.index)
print(df1.loc[192])
print(df.loc[192])#here index will be the 0th column default numbering column.
df.set_index('ID',inplace=True)#the index will be changed in same dataset.
print(df)
print(df.sort_values('Gender'))#will sort in alphabetical order