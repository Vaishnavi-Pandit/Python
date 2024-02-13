import pandas as pd
mydict={'col1':[1,2,3,4],'col2':[4,6,7,8]
        , 'col3':['four','six','seven','eight']}
df=pd.DataFrame(mydict)
print(df.query('col1>2'))
print(df.query('2*col1>=col2'))
print(df.query("col3 in ['six','four']"))
print(df.query('col2!=[5,7]'))
print(df.query('col2 not in [5,7]'))