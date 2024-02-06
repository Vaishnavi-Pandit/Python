import pandas as pd

df1 = pd.DataFrame({'Player name': ['Rahul Dravid', 'Virat Kohle', 'Vinod Kamle'], 'Age': [30, 24, 22]})
print(df1)
df2 = pd.DataFrame(
    {'Player name': ['Rahul Dravid', 'Virat Kohle', 'Harbhajan singh'], 'Salary': [45000, 60000, 440000]})
print(df2)
df3 = pd.merge(df1, df2)  # inner joins are default joins in merge where common elements are taken
print(df3)
df3 = pd.merge(df1, df2, how='inner')  # inner joins are joins where common elements are taken
print(df3)
df4 = pd.merge(df1, df2, how='outer')
# outer join are the joins where all the elements from the df1 and df2 are taken and at the empty places it will place Nan.
print(df4)
'''df1.join(df2,on='Player name')#not ideal'''
df5 = pd.merge(df1, df2, how='left')  # all the rows from the first/left table are taken
print(df5)
df6 = pd.merge(df1, df2, how='right')  # all the rows from the second/right table are taken.
print(df6)
