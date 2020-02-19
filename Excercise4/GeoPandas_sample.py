# coding: utf-8

# In[1]:


import geopandas as gpd


# In[2]:


shp01 = gpd.read_file(r"C:\Users\mymt_akck\Documents\microbase\training3\h27ka13101.shp")


# In[3]:


shp02 = gpd.read_file(r"C:\Users\mymt_akck\Documents\microbase\training3\h27ka13102.shp")


# In[4]:


shp03 = gpd.read_file(r"C:\Users\mymt_akck\Documents\microbase\training3\h27ka13103.shp")


# In[5]:


shp01.append(shp02) #単純に縦方向にたす。


# In[6]:


shp01.append(shp03)


# In[7]:


shp01.to_file(r"C:\Users\mymt_akck\Documents\microbase\training3\training03.shp")


# In[8]:


"ok"

