
# coding: utf-8

# In[1]:


import numpy as np
from collections import Counter


# In[66]:


with open("clean.txt") as file:
    contents = file.read()


# In[67]:


characters = set(contents)
table = {}


# In[68]:


np.random.seed(76)
for c in characters:
    table[c] = np.random.choice([0, 1], size=(100000,), p=[1999./2000, 1./2000])


# In[69]:


count = Counter(contents)


# In[70]:


summation = np.zeros(100000)


# In[71]:


for t in table:
    summation = np.add(summation, np.multiply(count[t], table[t]))


# In[72]:


temp = ' '
x = np.dot(summation, table[temp])
x / np.sum(table[temp]) / count[temp]


# In[73]:


freq_est = {}
for t in table:
    x = np.dot(summation, table[t])
    freq_est[t] = x / np.sum(table[t]) / count[t]


# In[74]:


avg = 0
for t in table:
    avg += freq_est[t]
avg / len(table)


# In[75]:


freq_est

