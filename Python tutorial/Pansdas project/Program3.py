import pandas as pd
df= pd.read_csv("E:\Python\datasets-df-series\empdata1.csv")
print(df)#if feilds are empty it will print Nan
df1=df.fillna(0)
print(df1)
avg_sal=df['sal'].mean()
print(avg_sal)
df1= df.fillna({'ename':'No name','sal':0.00,'doj':'2-4-2002'})
print(df1)
df1= df.fillna({'ename':'No name','sal':avg_sal,'doj':'2-4-2002'})
print(df1)

df1=df.dropna()#to remove the row having no value


print(df1)

df1.to_csv("E:\Python/Book3.csv")