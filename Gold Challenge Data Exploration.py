#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import regex as re


# In[2]:


df=pd.read_csv('data.csv',encoding='ISO-8859-1')
df.head()


# In[3]:


df.info()


# In[4]:


df.isnull().sum()


# In[16]:


import numpy as np
import matplotlib.pyplot as plt


# In[17]:


get_ipython().run_line_magic('matplotlib', 'inline')
target_HS = ("Individual", "Group")
HS1 = (3575, 1986)

plt.figure(figsize=(6,7))
plt.bar(target_HS, HS1, color='lightcoral')

plt.title('HS Target', size=18)
plt.ylabel('Sum', size=12)
plt.xticks(size=12)
plt.yticks(size=12)

plt.show()


# In[6]:



jenis_HS = df[["Tweet", "HS", "HS_Individual", "HS_Group", "HS_Religion", "HS_Race", "HS_Physical", "HS_Gender", "HS_Other", "HS_Weak", "HS_Moderate", "HS_Strong"]]
jenis_HS.sum() 


# In[7]:



get_ipython().run_line_magic('matplotlib', 'inline')

type_HS = ["HS_Religion", "HS_Race", "HS_Physical", "HS_Gender", "HS_Other"]
count = [793, 566, 323, 306, 3740]


plt.figure(figsize=(12,7))
plt.bar(type_HS, count)

plt.title('HS Type', size=18)
plt.ylabel('Sum', size=14)
plt.xticks(size=12)
plt.yticks(size=12)

plt.show()


# In[8]:


get_ipython().run_line_magic('matplotlib', 'inline')

power_HS = ["Weak", "Moderate", "Strong"]
phs = [3383, 1705, 473]


plt.figure(figsize=(12,7))
plt.bar(power_HS, phs, color="darkred")

plt.title('HS Power', size=18)
plt.ylabel('Sum', size=14)
plt.xticks(size=12)
plt.yticks(size=12)

plt.show()


# In[9]:


range(df.shape[0])


# In[10]:


df_alay=pd.read_csv('new_kamusalay.csv',encoding='ISO-8859-1')
df_alay.head()


# In[11]:


df_abusive=pd.read_csv('abusive.csv',encoding='ISO-8859-1')
df_abusive.head()


# In[13]:


kamus_alay = pd.read_csv('new_kamusalay.csv', encoding='ISO-8859-1', header=None)
kamus_alay = kamus_alay.rename(columns={0: 'Sebelum', 1: 'Sesudah'})
kamus_alay.head()

