#!/usr/bin/env python
# coding: utf-8

# # Steps to Create a Plot

# ## Step 1: Import the required libraries

# In[7]:


import numpy as np


# In[8]:


import matplotlib.pyplot as plt


# In[9]:


from matplotlib import style 


# In[10]:


get_ipython().run_line_magic('matplotlib', 'inline')


# - numpy: used generated random numbers
# 
# - pyplot: used the plot numbers
# 
# - style : this class used for setting the grid style
# 
# - %matplotlib inline: required to display the plot within Jupyter Notebook

# ## Step 2: Generate Random Numbers

# In[11]:


#generate random numers(total 10)


# In[12]:


randomNumber= np.random.rand(10)


# In[13]:


#view them


# In[15]:


print(randomNumber)


# ## Step 3: Set the Plot Numbers

# In[17]:


#Select the style of the plot

style.use('ggplot')


# In[18]:


#plot the random number

plt.plot(randomNumber, 'g', label= 'line one', linewidth=2)


# In[21]:


# x axis is number of random numbers(index)

plt.xlabel('Range')


# In[22]:


# y axis is actual random number

plt.ylabel('Numbers')


# In[23]:


# Title of the plot

plt.title('First Plot')


# ## Step 4: Display the Created Plot

# In[27]:


plt.legend()
plt.show()


# In[ ]:




