#!/usr/bin/env python
# coding: utf-8

# In[1]:


# modules we'll use
import pandas as pd
import numpy as np

# helpful character encoding module
import charset_normalizer

# set seed for reproducibility
np.random.seed(0)


# In[2]:


# start with a string
before = "This is the euro symbol: €"

# check to see what datatype it is
type(before)


# In[3]:


# encode it to a different encoding, replacing characters that raise errors
after = before.encode("utf-8", errors="replace")

# check the type
type(after)


# In[4]:


# take a look at what the bytes look like
after


# In[5]:


# convert it back to utf-8
print(after.decode("utf-8"))


# In[6]:


# try to decode our bytes with the ascii encoding
print(after.decode("ascii"))


# In[7]:


# start with a string
before = "This is the euro symbol: €"

# encode it to a different encoding, replacing characters that raise errors
after = before.encode("ascii", errors = "replace")

# convert it back to utf-8
print(after.decode("ascii"))

# We've lost the original underlying byte string! It's been 
# replaced with the underlying byte string for the unknown character :(


# In[10]:


# try to read in a file not in UTF-8
kickstarter_2018 = pd.read_csv(r"C:\Users\slmnp\Downloads\ks-projects-201801-utf8.csv")


# In[13]:


# look at the first ten thousand bytes to guess the character encoding
with open(r"C:\Users\slmnp\Downloads\ks-projects-201801-utf8.csv", 'rb') as rawdata:
    result = charset_normalizer.detect(rawdata.read(10000))

# check what the character encoding might be
print(result)


# In[20]:


# read in the file with the encoding detected by charset_normalizer
kickstarter_2018 = pd.read_csv(r"C:\Users\slmnp\Downloads\ks-projects-201801-utf8.csv", encoding='Windows-1252')

# look at the first few lines
kickstarter_2018.head()

