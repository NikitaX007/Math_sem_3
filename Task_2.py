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


# Возможные варианты: a) 2 из 2 белые и 1 из 4 белый, b) 1 из 2х белый и 2 из 4 белые, c)0 из 2х белые и 3 из 4 белые


# In[4]:


t1=combinations(8, 2)


# In[5]:


t2=combinations(12, 4)


# In[6]:


#a)


# In[7]:


a1=combinations(5, 2)


# In[8]:


a2=combinations(5, 1)


# In[9]:


b2=combinations(7, 3)


# In[10]:


p1=a1/t1


# In[11]:


p2=(a2*b2)/t2


# In[12]:


pa=p1*p2


# In[13]:


print("2 из 2 белые и 1 из 4 белый =",pa)


# In[14]:


#b)


# In[15]:


a1=combinations(5, 1)


# In[16]:


b1=combinations(3, 1)


# In[17]:


a2=combinations(5, 2)


# In[18]:


b2=combinations(7, 2)


# In[19]:


p1=(a1*b1)/t1


# In[20]:


p2=(a2*b2)/t2


# In[21]:


pb=p1*p2


# In[22]:


print("1 из 2х белый и 2 из 4 белые =",pb)


# In[23]:


#c)


# In[24]:


a1=combinations(3, 2)


# In[25]:


a2=combinations(5, 3)


# In[26]:


b2=combinations(7, 1)


# In[27]:


p1=a1/t1


# In[28]:


p2=(a2*b2)/t2


# In[29]:


pc=p1*p2


# In[30]:


print("0 из 2х белые и 3 из 4 белые =",pc)


# In[31]:


p=pa+pb+pc


# In[32]:


print("Вероятность того, что 3 мяча белые =",p)

