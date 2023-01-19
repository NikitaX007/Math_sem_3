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


p1=0.1
p2=0.2
p3=0.25
q1=1-p1
q2=1-p2
q3=1-p3


# In[4]:


p=p1*p2*p3


# In[5]:


print("Вероятность выхода из строя всех деталей =",p)


# In[6]:


p12=p1*p2*q3
p13=p1*q2*p3
p23=q1*p2*p3
pt2=p12+p13+p23


# In[7]:


print("Вероятность выхода из строя 2х деталей =",pt2)


# In[8]:


pn=q1*q2*q3
p=1-pn


# In[9]:


print("Вероятность выхода хотябы 1й детали =",p)


# In[10]:


p1=p1*q2*q3
p2=q1*p2*q3
p3=q1*q2*p3
p=p1+p2+p3+pt2


# In[11]:


print("Вероятность выхода из строя 1-2х деталей =",p)

