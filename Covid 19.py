#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from scipy import stats


# In[2]:


data = pd.read_csv('data\covid_19.csv')


# In[3]:


data


# In[4]:


data.count()


# In[5]:


data.isnull()


# In[6]:


data.isnull().sum()


# In[7]:


import seaborn as sns


# In[8]:


import matplotlib.pyplot as plt


# In[9]:


sns.heatmap(data.isnull())
plt.show()


# In[10]:


data.head(2)


# In[11]:


data.groupby('Region')


# In[12]:


data.groupby('Region').sum()


# In[13]:


data.groupby('Region').sum().head(20)


# In[14]:


data.groupby('Region')['Confirmed'].sum()


# In[15]:


data.groupby('Region')['Confirmed'].sum().sort_values(ascending=False)


# In[16]:


data.groupby('Region')['Confirmed'].sum().sort_values(ascending=False).head(10)


# In[17]:


data.groupby('Region')['Confirmed','Recovered'].sum()


# In[18]:


data.head(2)


# In[19]:


data[data.Confirmed<10]


# In[20]:


data=data[~(data.Confirmed<10)]


# In[21]:


data.head(20)


# In[22]:


data.head(2)


# In[23]:


data.groupby('Region').Confirmed.sum()


# In[24]:


data.groupby('Region').Confirmed.sum().sort_values(ascending=False)


# In[25]:


data.groupby('Region').Confirmed.sum().sort_values(ascending=False).head(20)


# In[26]:


data.head(2)


# In[27]:


data.groupby('Region').Deaths.sum()


# In[28]:


data.groupby('Region').Deaths.sum().sort_values(ascending=True).head(50)


# In[29]:


data.head(2)


# In[30]:


data[data.Region=='India']


# In[31]:


data[data.Region=='Yemen']


# In[32]:


data[data.Region=='US']


# In[33]:


data.head(2)


# In[38]:


data.sort_values(by=['Confirmed'],ascending=True)


# In[39]:


data.sort_values( by=['Recovered'])


# In[40]:


data.sort_values( by=['Recovered'],ascending=False).head(50)


# In[ ]:




