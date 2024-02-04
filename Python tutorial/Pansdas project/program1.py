import pandas as pd
df=pd.read_csv('E:\Python\datasets1\shoppingmall.csv')
print(df)
print(df.loc[:,'Gender'])
print(df.loc[:,['Age','Income']])#if you want two rows give it in the form of list.
print(df.iloc[:,1])
print(df.iloc[:,[2,3]])# in iloc we use numbers not column name.
print(df.iloc[0:3,[2,3]])#in iloc row no 3 is not printed when we use 0:3 but it will be included in loc
print(df.loc[0:3,['Age','Income']])
print(df.loc[:,:])
print(df.iloc[:,:])
print(df.loc[3:0:-1,['Age','Income']])#to reverse the order of reows in decending order.
print(df.iloc[3:0:-1,:])
print(df.loc[[0,3,2],['Age','Income']])
print(df.iloc[[0,3,2],[4,2]])
print(df.iloc[-1])#will print last row
print(df.iloc[:,-1])#will print last column in al rows
print(df.loc[:,'Score'])
r,c=df.shape
print(r,c)#no of rows and columns
print(df.head(2))#printing rows
print(df.tail(3))#will print last rows.
print(df[1:3])
print(df[1:4:2])#in step of 2
print(df[:])#all rows all columns
print(df[:]['Age'])#to print all rows and one column
print(df[:][['Age','Score']])#print multiple column
print(df.columns)#to print all coulmn names.
print(df[['Age','Score']])
print(df[:][['Age','Score']])# is equal to print(df[['Age','Score']])
print(df['Score'])
print(df['Score'].mean())
print(df['Score'].max())
print(df['Score'].sum())
print(df['Score'].count())
print(df['Score'].min())
print(df.describe())#Statisctical methods.
