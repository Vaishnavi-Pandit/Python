import pandas as pd
mydict={'col1':[1,2,3,4],'col2':[4,6,7,8]
        , 'col3':['four','six','seven','eight']}
df=pd.DataFrame(mydict)
print(df.iloc[1:3])
print(df.iloc[1:3,[0,2]])
print(df.loc[1:3])
print(df.loc[1:3,['col1','col2']])
print(df.loc[df['col1']<3])