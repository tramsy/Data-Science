#!/usr/bin/env python
# coding: utf-8

# In[86]:


#question 1

import pandas as pd
print(pd.__version__)


# In[87]:


#question 2
import numpy as np
arr = np.array([1,2,4,5,5,2121,4323])
series = pd.Series(arr)
print(series)


# In[10]:


#question 3

ind = series.index
pd.DataFrame(ind)


# In[11]:


#question 4

import seaborn as sns


# In[12]:


dset = sns.load_dataset('mpg')


# In[13]:


dset


# In[16]:


#question 5

origins = dset['origin'].unique()
print(origins)


# In[97]:


#question 6 

dset[dset['origin']=='usa']

