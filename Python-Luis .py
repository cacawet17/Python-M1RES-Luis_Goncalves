#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import numpy as np

snapshot = pd.read_csv('mower_market_snapshot.csv',sep=';')

total_nan_values = snapshot.isnull().sum()
total_nan_values


# In[32]:


snapshot


# In[14]:


total_nan_values = snapshot.isnull().sum().sum()
total_nan_values


# In[21]:


data = data.replace('unknown', np.nan)

snapshot['prod_cost'] = pd.to_numeric(data['prod_cost'])
print(data['prod_cost'])
data['prod_cost'] = data['prod_cost'].replace(np.nan, data['prod_cost'].mean())
print(data['prod_cost'])


# In[22]:


def warranty():
    data = pd.read_csv('mower_market_snapshot.csv', sep=";")
    data['warranty'] = pd.to_numeric(data['warranty'].str[0])
    print(data['warranty'])
    
warranty()


# In[24]:


df = pd.read_csv('mower_market_snapshot.csv', sep=";")
df = pd.get_dummies(df.product_type, prefix='product_type')
df.head()


# In[28]:


def product_type():
    data = pd.read_csv('mower_market_snapshot.csv', sep=";")
    data.product_type = pd.Categorical(data.product_type)
    print(data['product_type'])

product_type()


# In[31]:


for numbers in data.price:
        if numbers <= float(300):
            print(numbers, "1")
        elif numbers >= float(301) and numbers <= float(500):
    


# In[ ]:




