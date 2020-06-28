#!/usr/bin/env python
# coding: utf-8

# In[51]:


import numpy as np
import matplotlib.pyplot as plt


x = []

fig, ax = plt.subplots()
line1, = ax.plot(x, years, '--', linewidth=2,
                 label='Dashes set retroactively')
ax.legend(loc='lower right')
plt.show()


# In[50]:


import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# Example data
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = [1,2,3,4,5]
x_pos = [10, 15, 20, 5, 25]

ax.barh(y_pos, x_pos, align='center',
        color='green', ecolor='black')

ax.set_yticks(y_pos)
ax.set_yticklabels(people)

ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')

print(plt.show())


# In[48]:


import pandas as pd

data = {'India':['Delhi', 1.4, 2000], 'China':['Beijing', 1.6, 1000]}
df1 = pd.DataFrame(data, index = ('Capital', 'Population', 'PD'))
df1 = df1.transpose()
print(df1[df1.Capital == 'Delhi']['Population'].values)


# In[25]:


import pandas as pd

data = {'India':['Delhi', 1.4, 2000], 'China':['Beijing', 1.6, 1000]}
df1 = pd.DataFrame(data, index = ('Capital', 'Population', 'PD'))
print(df1['India']['Capital'])

df1['India']['Population'] = 1.5 # updation
#del df1['China'] # Deletion
df1['Brazil'] = ['Rio', .8, 1500] # Add a new coloum
#print(df1.India) # Pull any specific Coluoum
print(df1.iloc[1].sum())
print(df1.iloc[1].mean())
print(df1.iloc[1].std())

print(df1.loc['Population'].sum())
print(df1.loc['Population'].mean())
print(df1.loc['Population'].std())

print(df1.ix['Population'].sum())
print(df1.ix['Population'].mean())
print(df1.ix['Population'].std())


# In[ ]:





# In[11]:


import pandas as pd

data = {'one':pd.Series([1,2,3], index=['a', 'b', 'c']),
        'two':pd.Series([1,2], index=['a', 'b'])}

df1 = pd.DataFrame(data)
df2 = pd.DataFrame(data, index=['a', 'b'])

print(df1)
print(df2)


# In[7]:


import pandas as pd

data = [{'India':'Delhi', 'China':'Beijing'},
        {'India':1.4, 'China':1.6},
        {'India':2000, 'China':1000}]
df1 = pd.DataFrame(data, index=['Capital', 
                                'Population', 'PD'], 
                   columns=['India'])
print(df1)


# In[4]:


import pandas as pd

data = {'India':{'Capital':'Delhi', 'Population':1.4, 'PD':2000},
        'China':{'Capital':'Beijing', 'Population':1.6, 'PD':1000}}
df1 = pd.DataFrame(data)
print(df1)


# In[ ]:





# In[3]:


import pandas as pd

data = {'India':['Delhi', 1.4, 2000], 'China':['Beijing', 1.6, 1000]}
df1 = pd.DataFrame(data, index = ('Capital', 'Population', 'PD'))
print(df1)


# In[ ]:




