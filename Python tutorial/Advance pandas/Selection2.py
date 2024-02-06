import pandas as pd
import numpy as np
df = pd.DataFrame(data=np.random.randint(0,100,(4,3)),columns=('Test1','Test2','Test3'), index=['vinay','anil','Gopal','Rao'])
print(df)
df1=df.where(df<80,'A+')
print(df1)
df2=df.where(df['Test1']<80,'Excellent')
print(df2)
df3=df.where(lambda x:x<70,'Good')
print(df3)