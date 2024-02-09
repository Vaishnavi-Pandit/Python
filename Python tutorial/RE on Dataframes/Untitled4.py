#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[6]:


df=pd.read_csv('E:\Python\datasets1/AAPL Data.csv',parse_dates=['Date'],index_col='Date')#we are parsing to make manipulation easy.


# In[4]:


df


# In[7]:


df.loc['2020-01']


# In[10]:


df.loc['2020-01'].Close.mean()


# In[11]:


df.loc['2020-01'].Close.max()


# In[13]:


df.loc['2020-01-27']


# In[14]:


df.loc['2020-01-27':'2020-01-31']


# In[19]:


df.Close.resample('M').mean()


# In[21]:


#line plot
'''%matplotlib inline#inline inclusion after this step matplotlib will be available'''
df.Close.resample('M').mean().plot(kind='line')


# In[25]:


df.plot.scatter(x='Open',y='Close',alpha=0.5)


# In[26]:


df[['High','Low']]


# In[27]:


df1=pd.read_csv('E:\Python\datasets1/AAPL Data1.csv')


# In[28]:


df1


# In[29]:


pd.set_option('display.max_rows',None)


# In[32]:


#generate 100 dates and add them into dataframe.
rng=pd.date_range(start='2020/1/20',end='2020/6/7',freq='B')
rng


# In[33]:


rng=pd.date_range(start='2020/1/20',periods=100,freq='B')
rng


# In[34]:


df.set_index(rng,inplace=True)
df


# In[36]:


df.asfreq('D',method='pad')#D,B,H,M,Y


# In[ ]:




