
# coding: utf-8

# In[2]:


import re


# In[3]:


with open("alice.txt") as file:
    alice = file.read()


# In[4]:


set(alice)


# In[5]:


wonder = alice.lower()


# In[7]:


wonder = re.sub('\n', ' ', wonder)
wonder = re.sub('[*]', '', wonder)
wonder = re.sub('[[]', '', wonder)
wonder = re.sub(']', '', wonder)
wonder = re.sub('_', '', wonder)


# In[9]:


set(wonder)


# In[10]:


wonder


# In[11]:


with open("clean.txt", "w") as text_file:
    text_file.write(wonder)


# In[12]:


len(set(wonder))

