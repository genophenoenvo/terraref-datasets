#!/usr/bin/env python
# coding: utf-8

# ### Phenotype Table for Initial Set of Training Data

# In[1]:


import datetime
import pandas as pd
import numpy as np


# #### Import dataset downloaded from betydb in R

# In[2]:


df_0 = pd.read_csv('../data/raw/mac_season_4.csv')
df_0.head()


# In[3]:


df_0.columns


# In[4]:


df_1 = df_0.drop(labels=['Unnamed: 0', 'checked', 'citation_id', 'city', 'scientificname', 'commonname', 'genus',
                        'species_id', 'author', 'citation_year', 'trait_description', 'units', 'n', 'statname',
                        'stat', 'access_level', 'view_url', 'edit_url'], axis=1)

df_1.head()


# #### Extract Range and Column Values

# In[5]:


df_2 = df_1.copy()


# In[6]:


df_2['range'] = df_2['sitename'].str.extract("Range (\d+)").astype(int)
df_2['column'] = df_2['sitename'].str.extract("Column (\d+)").astype(int)


# #### Convert table to wide format
# * Each trait should have its own column
# * Rename `mean` column to `value` for easier understanding

# In[10]:


df_3 = df_2.rename({'mean': 'value'}, axis=1)


# In[13]:


traits_to_keep = ['leaf_temperature', 'ambient_humidity', 'proximal_air_temperature', 'surface_temperature',
                  'aboveground_dry_biomass', 'canopy_height', 'flag_leaf_emergence_time', 'flowering_time',
                  'canopy_cover']

empty_df = pd.DataFrame(data=df_3, index=df_3.index, columns=traits_to_keep)


# In[18]:


df_4 = pd.concat([df_3, empty_df.reindex(df_3.index)], axis=1)


# In[21]:


timestamp = datetime.datetime.now().replace(microsecond=0).isoformat()
output_filename = f'pheno-table_{timestamp}.csv'.replace(':', '')
df_4.to_csv(f'../data/processed/{output_filename}', index=False)


# In[ ]:




