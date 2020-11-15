#!/usr/bin/env python
# coding: utf-8

# In[31]:


import numpy as np
arr = np.arange(2, 50, 3)
print(arr)


# In[21]:


lst1 = []
lst2 = []

for i in range(5):
    value1 = int(input())
    value2 = int(input())
    lst1.append(value1)
    lst2.append(value2)

arr1 = np.array(lst1)
arr2 = np.array(lst2)
print(arr1)
print(arr2)
print()
concatinated = arr1+arr2
print(concatinated)
print()
print(np.sort(arr1))
print(np.sort(arr2))


# In[3]:


new_arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
#we use .shape to find dimension
print(new_arr.shape)
print(new_arr.size)


# In[24]:


one_arr = np.array([1,3,4])
print(one_arr)
print(one_arr.shape)
two = one_arr[np.newaxis, :]
print(two)
print(two.shape)


# In[30]:


first_arr = np.array([1,2,3])
second_arr = np.array([4,5,6])

first_square = np.square(first_arr)
second_square = np.square(second_arr)
print(first_square)
print(second_square)
print()
print(np.vstack(first_square))
print(np.hstack(first_square))
print()
print(np.vstack(second_square))
print(np.hstack(second_square))


# In[32]:


arr = np.array([1,1,1,2,2,3,3,4,5,5,4,5,4,5,10])
np.unique(arr)


# In[ ]:




