import pandas as pd
df = pd.read_csv("E:\Python\datasets1/titanic.csv")
print(df)
print(df.head())#first 5 rows will be printed.
print(df.tail())#last 5 rows will be printed
print(df.head(2))#first 2 rows will be printed.
print(df.tail(2))#last 2 rows will be printed
'''print(df[['Passenger Id']])#to print name'''
'''print(df[['Passenger Id','Age']])#to print name, age'''
print(df.iloc[5:10])
print(df.iloc[5:10:2])#to print name
print(df.iloc[5,3])
print(df[df.Age>45])
print(df[(df.Age>45) & (df.Sex=='male')])
