#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from scipy.stats import  binom
from scipy.stats import  poisson


# In[2]:


def combinations(n, k):
    return (np.math.factorial(n)/(np.math.factorial(k)*np.math.factorial(n-k)))


# In[3]:


qa=0.25


# In[4]:


qb=0.25


# In[5]:


qc=0.5


# In[6]:


pa=0.8


# In[7]:


pb=0.7


# In[8]:


pc=0.9


# In[9]:


pt=qa*pa+qb*pb+qc*pc


# In[10]:


print("Доля сдавщих студентов от общего количества поступивших =",pt)


# In[11]:


p=qa*pa/pt


# In[12]:


print("Вероятность, что он учится из факультета A =",p)


# In[13]:


p=qb*pb/pt


# In[14]:


print("Вероятность, что он учится из факультета B =",p)


# In[15]:


p=qc*pc/pt


# In[16]:


print("Вероятность, что он учится из факультета C =",p)

