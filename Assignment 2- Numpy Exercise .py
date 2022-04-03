#!/usr/bin/env python
# coding: utf-8

# # NumPy Exercises 
# 
# Now that we've learned about NumPy let's test your knowledge. We'll start off with a few simple tasks, and then you'll be asked some more complicated questions.

# #### Import NumPy as np

# In[1]:


import numpy as np


# #### Create an array of 10 zeros 

# In[2]:


np.zeros(10)


# #### Create an array of 10 ones

# In[3]:


np.ones(10)


# #### Create an array of 10 fives

# In[4]:


np.ones(10)*5


# #### Create an array of the integers from 10 to 50

# In[5]:


np.arange(10,51)


# #### Create an array of all the even integers from 10 to 50

# In[19]:


x = np.arange(10,51)
y = (x%2 == 0)
z = x[y]
print(z)


# #### Create a 3x3 matrix with values ranging from 0 to 8

# In[8]:


np.arange(0,9).reshape((3,3))


# #### Create a 3x3 identity matrix

# In[20]:


np.arange(0,9).reshape((3,3))


# #### Use NumPy to generate a random number between 0 and 1

# In[21]:


np.random.randint(0,1)


# #### Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution

# In[22]:


np.linspace(0,1,20)


# #### Create the following matrix:

# In[32]:


np.arange(1,101).reshape(10,10) / 100


# ## Numpy Indexing and Selection
# 
# Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:

# In[23]:


mat = np.arange(1,26).reshape(5,5)
mat


# In[ ]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[24]:


mat[2: ,1:]


# In[ ]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[25]:


mat[3,4]


# In[ ]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[26]:


mat[0:3,1:2]


# In[ ]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[27]:


mat[4]


# In[ ]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[28]:


mat[3:]


# ### Now do the following

# #### Get the sum of all the values in mat

# In[29]:


mat.sum()


# #### Get the standard deviation of the values in mat

# In[30]:


mat.std()


# #### Get the sum of all the columns in mat

# In[31]:


mat.sum(axis=1)


# 
