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


sal = np.array([100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150])


# In[4]:


sa=sal.sum()/sal.size


# In[5]:


sa_=sal.mean()


# In[6]:


saq=(sal-sa)**2


# In[7]:


std=(saq.sum()/sal.size)**.5


# In[8]:


stdd=(saq.sum()/(sal.size-1))**.5


# In[9]:


std_=sal.std()


# In[10]:


stdd_=sal.std(ddof=1)


# In[11]:


var=saq.sum()/sal.size


# In[12]:


var_=sal.var()


# In[13]:


vard=saq.sum()/(sal.size-1)


# In[14]:


vard_=sal.var(ddof=1)


# In[15]:


print("Среднее арифметическое =",sa_)


# In[16]:


print("Cреднее квадратичное отклонение =",std_)


# In[17]:


print("Дисперсия смещенная оценка =",var_)


# In[21]:


print("Дисперсия несмещенная оценка =",vard_)

