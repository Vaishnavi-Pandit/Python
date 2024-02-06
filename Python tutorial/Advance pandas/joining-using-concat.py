import pandas as pd

df1 = pd.DataFrame({'Player name': ['Rahul Dravid', 'Virat Kohle', 'Vinod Kamle'], 'Age': [30, 24, 22]})
print(df1)
df2 = pd.DataFrame(
    {'Player name': ['Rahul Dravid', 'Virat Kohle', 'Harbhajan singh'], 'Salary': [45000, 60000, 440000]})
print(df2)
df3=pd.concat([df1,df2])#two tables are joined with similar index as previous one and the join takes the all rows fron 1st and 2nd it does not merge.
print(df3)
df4=pd.concat([df1,df2],axis=1)#to merge
print(df4)
df5=df1._append(df2,sort=True)# but not recommended as it may or may not be available in every version
print(df5)