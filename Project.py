#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('classic')

Tasks to perform

# In[3]:


#reading dataset 
data = pd.read_csv('C:\ProgramData\Anaconda3\pubg.csv')
data


# In[5]:


data.columns


# In[5]:


#data type of columns
type(data.columns)


# In[6]:


#avarage player kill how many players
data['kills'].mean
sam = data['kills'].sum()
average = sam/999
print(round(average, 2))


# In[7]:


#maximum number of player killed

data['kills'].max()


# In[13]:


#Print all the columns of the dataframe

data


# In[20]:


#comment on walked distance

sns.distplot(data['walkDistance'])


# In[22]:


sns.distributions


# In[11]:


#comment on distribution of match duration
sns.distplot(data['matchDuration'])


# In[39]:


#plot distribution one below other
plt.subplot(2,1,1)
plt.plot(data['matchDuration'], data['walkDistance']);
plt.subplot(2,1,2)
plt.plot(data['matchDuration'], data['walkDistance']);


# In[40]:


#plot distribution side by side

plt.subplot(1,2,1)
plt.plot(data['matchDuration'], data['walkDistance'])
plt.subplot(1,2,2)
plt.plot(data['matchDuration'], data['walkDistance'])


# In[9]:


#Pairplot the dataframe. Comment on kills vs damage dealt
sns.pairplot(data, x_vars=['kills'], y_vars=['damageDealt'])


# In[10]:


data.columns


# In[16]:


#Comment on maxPlace vs numGroups

sns.pairplot(data, x_vars=['maxPlace'], y_vars=['numGroups'])


# In[20]:


#How many unique values are there in 'matchType' and what are their counts

uni = data['matchType'].unique()
cnt = data['matchType'].value_counts()
print(uni)
print()
print(cnt)


# In[43]:


#Plot a barplot of ‘matchType’ vs 'killPoints'. Write your inferences.
#sns.barplot(data['matchType'], data['killPoints'], data=data)


# In[ ]:


#Plot a barplot of ‘matchType’ vs ‘weaponsAcquired’. Write your inferences
#sns.barplot(data['matchType'], data['weaponsAcquired'], data=data)


# In[65]:


#catogorical columns
cat = []
num = data.describe().columns
col = data.columns

for i in col:
    if i not in num:
        cat.append(i)

print(cat)
print(col)


# In[12]:


#Plot a boxplot of ‘matchType’ vs ‘winPlacePerc’. Write your inferences

sns.boxplot(x=data['matchType'], y=data['winPlacePerc'], data=data)


# In[14]:


#Plot a boxplot of ‘matchType’ vs ‘matchDuration’. Write your inferences
sns.boxplot(x=data['matchType'], y=data['matchDuration'], data=data)


# In[18]:


#Change the orientation of the above plot to horizontal
sns.boxplot(y=data['matchType'], x=data['matchDuration'], data=data,)


# In[20]:


#Add a new column called ‘KILL’ which contains the sum of following columns viz. headshotKills,
#teamKills, roadKills

data['KILL'] = data['headshotKills'] + data['teamKills'] + data['roadKills']

print(data['KILL'])


# In[21]:


#Round off column ‘winPlacePerc’ to 2 decimals
round(data['winPlacePerc'], 2)


# In[58]:


#Take a sample of size 50 from the column damageDealt for 100 times and calculate its mean. Plot
#it on a histogram and comment on its distribution.

size = []
for i in data['damageDealt']:
    if i == 50:
        size.append(i)

for i in range(99):
    size.append(50.0)

total = pd.DataFrame(size).sum()
mean  = total/100
print(mean)

sns.distplot(size)
sns.distributions

