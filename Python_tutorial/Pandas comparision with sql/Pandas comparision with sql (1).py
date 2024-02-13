#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


cust=pd.read_csv('E:\Python\datasets1/shoppingmall.csv')


# In[5]:


cust


# In[6]:


pd.set_option('display.max_rows', None)#to display all the rows.


# In[7]:


cust


# In[8]:


#select * from cust
cust


# In[9]:


#to print 8 rows only
#select * from cust limit 8
cust.head(8)


# In[45]:


cust.groupby(['Gender','Age']).size().to_frame('Count').reset_index()


# In[12]:


#select * from cust where Income=23
cust[cust.Income==23]
cust[cust['Income']==23]#similar as upper one


# In[16]:


#select ID from cust where Income=23
cust.ID[cust.Income==23]
''''cust[cust.Income==23].ID
cust[cust['Income']==23]['ID']'''


# In[20]:


#select Id, score from cust where income=23
cust[cust['Income']==23][['ID','Score']]


# In[21]:


#select * from cust where Income=23 and Score=98
cust[(cust.Income==23) & (cust.Score==98)]


# In[28]:


cust[(cust.Income==23) & (cust.Score==98)][['ID','Score']]


# In[30]:


#select max(Age), min(Age), mean(Age) from cust
cust.agg({'Age':['max','min','mean']})


# In[31]:


#to get unique values without duplicates.
#select Distinct Income from cust
cust['Income'].unique()
#cust.Income.unique()


# In[34]:


#Select * from cust where gencer=female
cust[cust.Gender=='Female']


# In[35]:


#select * from cust where Gender=='Female' order by Score.
cust[cust.Gender=='Female'].sort_values('Score')


# In[36]:


#select * from cust where Gender=='Female' order by Score desc.
cust[cust.Gender=='Female'].sort_values('Score', ascending=False)


# In[43]:


#select Gender, Age, count(*) from cust group by Gender, Age
cust.groupby(['Gender','Age']).size()


# In[44]:


cust.groupby(['Gender','Age']).size().to_frame('Count')


# In[46]:


#select Gender, Age , count(*) from cust group by Gender, Age order by Age desc
cust.groupby(['Gender','Age']).size().to_frame('Count').reset_index().sort_values('Age', ascending=False)


# In[48]:


#Select * from cust where age in (20,30,40)
cust[cust.Age.isin([20,30,40])]


# In[50]:


#select * from cust where age not in (20,30,40)
cust[~cust.Age.isin([20,30,40])]


# In[51]:


#select * from cust order by Score desc limit 10
cust.nlargest(10, columns='Score')


# In[52]:


# leave first 10 records give the next 10.
#select * from cust order by Score desc limit 10 offset 10
cust.nlargest(10, columns='Score').tail(10)


# In[53]:


shop=pd.read_csv('E:\Python\datasets1/shopping_customers.csv')
shop


# In[55]:


#select * from cust Income>50 union all select * from shop where Income<45
pd.concat([cust[cust.Income>50],shop[shop.Income<45]])


# In[56]:


#)select * from cust Income>50 union select * from shop where Income<45
pd.concat([cust[cust.Income>50],shop[shop.Income<45]]).drop_duplicates()


# In[70]:


#insert into table cust values(500,'Male', 50, 30, 20)
'''cust=cust.append({'ID':500,'Gender':'Female','Age':50,'Income':30,'Score':20},ignore_index=True)
cust'''


# In[67]:


#update cust set  Score =11 where score= 10
cust.loc[cust['Score']==10,'Score']=11
cust[cust.Score==11]


# In[68]:


#delete from cust where Score=11
cust=cust.drop(cust[cust.Score==11].index)


# In[69]:


cust[cust.Score==11]


# In[ ]:




