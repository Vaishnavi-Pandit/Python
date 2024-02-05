import pandas as pd
tpl=[(1001,'Nagesh'),(1002,'Lakshmi'),(1003,'Ganesh'),(1004,'Vaishnavi')]
df=pd.DataFrame(tpl)
print(df)
df.columns=['col1','col2']#to give column names
print(df)
df.rename(columns={'col1':'empid','col2':'empname'},inplace=True)#to rename columns
print(df)
#to add column
df['dept']='sales'#add same value in new column
print(df)
df['dept']=['sales','It','HR','Product']
print(df)
#to place column at particular place
df.insert(loc=1,column='salary', value=[23552,46547,47657,646464])
print(df)
df['tax']=df['salary']*10/100
print(df)
#create new column
#for using lambda we need assign method
df1=df.assign(PF=lambda x:x.salary*12.5/100)
print(df1)
#gross salary=salary-tax-pf
df2=df1.assign(gross_salary=lambda x:x.salary-x.tax-x.PF)
print(df2)