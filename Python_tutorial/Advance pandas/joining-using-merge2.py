import pandas as pd

df1 = pd.DataFrame({'Player name': ['Rahul Dravid', 'Virat Kohle', 'Vinod Kamle'], 'Age': [30, 24, 22]})
print(df1)
df2 = pd.DataFrame(
    {'Sports Person': ['Rahul Dravid', 'Virat Kohle', 'Harbhajan singh'], 'Salary': [45000, 60000, 440000]})
print(df2)
df3=pd.merge(df1,df2,left_on='Player name',right_on='Sports Person',how='inner')#this metod is used when col names in df are different
print(df3)
