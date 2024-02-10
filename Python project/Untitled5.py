#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_csv('E:\Python\Python project/world_alcohol_comsumption.csv')


# In[3]:


df


# In[42]:


#to find and display bar chart to out the alcohol consumption details in the year 1986 or 1989 where who rgionis 'Americas'and 'Europ'
res1=df[((df['Year']==1986)|(df['Year']==1989))].where((df['WHO region']=='Americas')|(df['WHO region']=='Europe'))
res1


# In[9]:


#To find the alcohol consumption details in 1987 or 1989
df[(df.Year==1987)|(df.Year==1989)]


# In[44]:


plt.bar("Beverage Type","Display Value",data=res1,label='1987 data',color='yellow')
plt.xlabel('alcohol Consumption')
plt.ylabel('Western Pasific, Vietnam')
plt.show


# In[49]:


res1=df[((df['Year']==1986)|(df['Year']==1989))].where((df['WHO region']=='Americas')|(df['WHO region']=='Europe'))[['WHO region','Country','Beverage Types']]
res1=res1.dropna()
res1


# In[50]:


'''Find the records where consumption of beverages per person average >=5 and Beverage Types is beer'''
res=df[(df['Display Value']>=5)&(df['Beverage Types']=='Beer')]
res


# In[55]:


'''find out and display the pie chart of the records where consumption of beverages per person average>=4 and Beverage type= beer,wine,spirits'''
res1=df[(df['Display Value']>=4)&(df['Beverage Types']=='Beer')]['Display Value']
res1
res2=df[(df['Display Value']>=4)&(df['Beverage Types']=='Wine')]['Display Value']
res2
res3=df[(df['Display Value']>=4)&(df['Beverage Types']=='Spirits')]['Display Value']
res3
plt.pie(res1,shadow=True,autopct='%.1f%%')
plt.show()
plt.pie(res2,shadow=True,autopct='%.1f%%')
plt.show()
plt.pie(res3,shadow=True,autopct='%.1f%%')
plt.show()


# In[56]:


df.loc[0:15,['WHO region','Beverage Types']]


# In[59]:


#filter those records where WHO region contains "Ea" substring.
res=df['WHO region']
res
res[res.str.contains('Ea')]


# In[61]:


df[res.str.contains('Ea')]
res=df[res.str.contains('Ea')]
n=len(res)
n


# In[62]:


#filrer those records where who region matches with multiple values(Africa, Eastern Maiterranean, europe)

df1=df.rename(columns={'WHO region':'WHO_region'})
df1


# In[63]:


df1.query("WHO_region in ['Africa','Eastern Mediterranean','Europe']")


# In[64]:


df1.query("WHO_region not in ['Africa','Eastern Mediterranean','Europe']")


# In[65]:


#find average consumption of wine per person greater than 2
df[(df['Beverage Types']=='Wine')&(df['Display Value']>2)]


# In[70]:


#filter the rows, based on row numbers ended with 0,like0,10,20,30
lst=list(range(0,len(df),10))#len(df)=no of total rows
lst
rows=df.loc[lst,:]
rows


# In[72]:


rows=df.loc[0:9,['Year','Country']]
rows


# In[75]:


#to filter all columns where all enteries present, check which rows and columns having nan values and finally drop rows with any nNS
df.isnull().sum()
df.dropna(inplace=True)
df


# In[76]:


#to filter all records Starting from the year column,access every other column
r=range(0,len(df.columns),2)
lst=list(r)
df.iloc[:,lst]


# In[77]:


#filter all records sTarting from 2nd row ,access every 5th row
r= range(2,len(df),5)
lst=list(r)
df.loc[lst,:]


# In[82]:


df.rename(columns=
    {'Year':'_Year','WHO region':'who_region'},inplace=True)


# In[83]:


df


# In[ ]:





# In[31]:


#display horizontal bar chart the alcohol consumption in year '1986' where WHO regein is 'Western Pacific' and country is vietnam from dataset
import matplotlib.pyplot as plt
res=df[df.Year==1987].where((df['WHO region']=='Western Pacific') & (df['Country']=='Viet Nam'))
res
res= res.dropna()
res
plt.bar("Beverage Type","Display Value",data=res,label='1987 data',color='yellow')
plt.xlabel('alcohol Consumption')
plt.ylabel('Western Pasific, Vietnam')
plt.show

