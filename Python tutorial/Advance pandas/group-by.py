import pandas as pd
import numpy as np
df = pd.read_csv("E:/Python/datasets1/cities_weather.csv")
print(df)
df1=df.groupby('city')#df1 is a object
print(df1)
for city,city_df in df1:
    print(city)
    print(city_df)
print(df1.get_group('mumbai').max())
print(df1.get_group('paris').min())
print(df.min())
print(df.agg('min'))
print(df1.agg('min'))
print(df.agg(['min','max']))
print(df1['temperature'].agg(['min','max']))
df2=df1.get_group('mumbai')
print(df2['temperature'].agg(['min','max']))
print(df.agg({'temperature':['min','max'],'windspeed':['mean','median']}))