import pandas as pd
import numpy as np
df = pd.DataFrame(data=np.random.randint(0,100,(4,3)),columns=('Test1','Test2','Test3'), index=['vinay','anil','Gopal','Rao'])
print(df)
df2=pd.DataFrame(data=np.random.randint(0,100,(4,3)),columns=('Test1','Test2','Test3'), index=['vinay','anil','Gopal','Rao'])
print(df2)
print(df.where(df<70,df2))