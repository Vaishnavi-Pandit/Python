#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np


# In[7]:


df= pd.DataFrame({'a':[1,2,3,4,5,6,7,8],'b':[10,np.nan,np.nan,20,np.nan,np.nan,30,30]})


# In[8]:


df


# In[9]:


#find cumlative sum on column a
df['a_cumsum']=df['a'].cumsum()
df


# In[11]:


df['a_cumprod']=df['a'].cumprod()#cummin(),cummax(),cummean()
df


# In[17]:


#find the rolling sum on 'a' for window 2
obj=df['a'].rolling(window=2)#creating window
df['a_roll_sum']=obj.sum()#calculating sum for that window.
df


# In[25]:


#find a rollin count for b for rolling size 2
ob=df['b'].rolling(window=2,min_periods=2)
df['b_rollcount']=ob.count()
df#


# In[29]:


#find expanding sum
'''ob=df['a'].expanding(min_periods=1)
df['a-exp-sum']=ob.sum()
df'''
obj=df['a'].expanding(min_periods=2)#basically it is same as cumsum but it prints nan at first place 
df['a-exp-sum']=obj.sum()
df


# In[30]:


df=pd.read_csv('E:\Python\datasets1/carprices.csv')


# In[31]:


df


# In[32]:


#to print column names stsrting with m
df.filter(regex=r'^m', axis=1)


# In[33]:


# to print the column having age at last of their name.
df.filter(regex=r'age$', axis=1)


# In[34]:


#to calculate the string length of strings in the column.
df_car=df['car model']
df_car.str.len()


# In[35]:


df_car.str.contains(r'Audi \w*')


# In[36]:


df[df_car.str.contains(r'Audi \w*')]


# In[37]:


df_car.str.findall(r'Audi \w*')


# In[38]:


df_car.str.replace(r'Audi \w*',r'bodi')


# In[40]:


df_car.str.extractall(r'(BMW \w\w)')


# In[41]:


df_car.str.extract(r'(BMW \w\w)')


# In[42]:


df_car.str.split(r'[XA]\d')


# In[43]:


df['model_date'].str.findall(r'\d\d-\d\d-(\d\d\d\d)')


# In[44]:


df['model_date'].str.findall(r'(\d\d)-\d\d-(\d\d\d\d)')


# In[ ]:




