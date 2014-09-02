
# coding: utf-8

# # pandas Lab

# _This is a quiz given in Roger Peng [Coursera](https://www.coursera.org) class [Computing for Data Analysis](https://www.coursera.org/course/compdata).  _
# 
# _Sourced from [Research Computing MeetUp's](https://github.com/ResearchComputing/Meetup-Fall-2013) Python course._
# 

# In[267]:

import pandas as pd
import os

data = pd.read_csv(os.path.join('data', 'ozone.csv'))


# In[268]:

print data.head()


# Print the column names of the dataset to the screen, one column name per line.  

# In[46]:

for i in data.columns.values:
    print i


# Extract the first 2 rows of the data frame and print them to the console. What does the output
# look like?

# In[92]:

tmp = data.ix[0:1]
tmp


# How many observations (i.e. rows) are in this data frame?

# In[48]:

len(data)


# Extract the last 2 rows of the data frame and print them to the console. What does the output
# look like?

# In[49]:

data.tail(2)


# What is the value of Ozone in row 47?

# In[50]:


data.ix[45:49]
data['Ozone'][47]


# How many missing values are in the Ozone column of this data frame?

# In[84]:

data['Ozone'].isnull().sum()


# What is the mean of the Ozone column in this dataset?

# In[52]:

data['Ozone'].mean()


# Extract the subset of rows of the data frame where Ozone values are above 31 and Temp values
# are above 90. What is the mean of Solar.R in this subset?

# In[53]:

data[ (data['Ozone'] > 31) & (data['Temp'] > 90) ]['Solar.R'].mean()


# What is the mean of "Temp" when "Month" is equal to 6?

# In[54]:

data[data['Month'] == 6]['Temp'].mean()


# What was the maximum ozone value in the month of May (i.e. Month = 5)?

# In[124]:

data[data['Month'] == 5]['Ozone'].max()


# ## Part 2

# Kaggle has a nice challenge based on titanic passenger data. We'll use the training set from [Kaggle](http://www.kaggle.com/c/titanic-gettingStarted/data), located in the data directory of this lesson.

# In[11]:

# TODO Import pandas under the alias 'pd'
import pandas as pd
import os


# In[12]:

df = pd.read_csv(os.path.join('data', 'train.csv'))
df


# In[8]:

# TODO what proportion of people survived?
for i in df.columns.values:
    print i
len(df)


# In[11]:

# TODO Read the data using pd.read_csv()
df


# In[4]:

from collections import defaultdict
df.shape


# In[5]:

df[df.Survived ==1].sum() / len(df) * 100


# In[17]:

df['Survived'].value_counts()


# In[6]:

Not_Survived = df['Survived'].value_counts(0)
print Not_Survived.astype(float)



# Now write a function that returns a dictionary of the number of `survived`, `not survived`, and `unknown`.  Here is the example function call:
# ```python
# print titanic_function(data)
# 
# {'survived': 342, 'not survived': 549, 'unknown': 1}
# 
# ```
# Hint: look at `collections.defaultdict`

# In[9]:

from collections import defaultdict
data = df['Survived']
def titanic_function(data):
    tmp = defaultdict(int)
    for d in data:
        try:
            if int(d) == 1:
                tmp['Survived'] += 1
            else:
                tmp['not survived'] += 1
        except ValueError:
                tmp['unknown'] += 1
    return tmp

print titanic_function(data)


# In[271]:




# ### What percentage of the men survived? What percentage of the women survived?
# Hint: execute `from __future__ import division` to force Python to return real-valued quotients for integer division.

# In[10]:

from __future__ import division

print len(df[ (df.Sex == 'male') & (df.Survived == 1) ]) / len(df[df.Sex == 'male']) * 100
print len(df[ (df.Sex == 'female') & (df.Survived == 1) ]) / len(df[df.Sex == 'female']) * 100


# # Next Steps
# 
# **Recommended Resources**
# 
# Name | Description
# --- | ---
# [Official Pandas Tutorials](http://pandas.pydata.org/pandas-docs/stable/tutorials.html) | Wes & Company's selection of tutorials and lectures
# [Julia Evans Pandas Cookbook](https://github.com/jvns/pandas-cookbook) | Great resource with eamples from weather, bikes and 311 calls
# [Learn Pandas Tutorials](https://bitbucket.org/hrojas/learn-pandas) | A great series of Pandas tutorials from Dave Rojas
# [Research Computing Python Data PYNBs](https://github.com/ResearchComputing/Meetup-Fall-2013/tree/master/python) | A super awesome set of python notebooks from a meetup-based course exclusively devoted to pandas
