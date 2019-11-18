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


# #### Extract Range and Column Values

# In[5]:


df_2 = df_1.copy()


# In[6]:


df_2['range'] = df_2['sitename'].str.extract("Range (\d+)").astype(int)
df_2['column'] = df_2['sitename'].str.extract("Column (\d+)").astype(int)


# #### Convert table to wide format
# * Each trait should have its own column
# * Rename `mean` column to `value` for easier understanding

# In[7]:


df_3 = df_2.rename({'mean': 'value'}, axis=1)


# In[8]:


traits_to_keep = ['leaf_temperature', 'ambient_humidity', 'proximal_air_temperature', 'surface_temperature',
                  'aboveground_dry_biomass', 'canopy_height', 'flag_leaf_emergence_time', 'flowering_time',
                  'canopy_cover']


# In[9]:


empty_df = pd.DataFrame(data=df_3, index=df_3.index, columns=traits_to_keep)


# In[10]:


df_4 = pd.concat([df_3, empty_df.reindex(df_3.index)], axis=1)


# #### Drop more unecessary (at this time) columns

# In[11]:


df_5 = df_4.drop(labels=['result_type', 'treatment_id', 'treatment', 'dateloc'], axis=1)


# #### Populate empty columns with available values

# In[12]:


# This is very slow - needs refactoring for .py script and reproducible notebook 

# run_slow_stuff = False

# if run_slow_stuff:

counter = 0

for index, row in df_5.iterrows():
    if counter % 1000 == 0:
        print(counter)            
        counter += 1
    for trait in traits_to_keep:
        if row['trait'] == trait:                
            df_5.loc[index, [trait]] = row['value']


# In[13]:


df_6 = df_5.set_index('sitename')


# #### Drop some columns that are redundant or can be explained in data dictionary
# * `month`
# * `year`
# * `notes`
# * `trait` - now have trait values in wide format (one column per trait requested for this iteration of dataset)
# * `method_name`
# * `notes` 

# In[14]:


df_6.drop(labels=['month', 'year', 'notes', 'trait', 'method_name', 'notes'], axis=1, inplace=True)


# #### Read in `df_6` 

# In[15]:


# df_6 = pd.read_csv(('../data/processed/pheno-table_populated_traits_2019-11-18T071126.csv')


# #### Add growing degree days

# #### Add max canopy height

# #### Re-order column names

# #### Change plots to index

# #### Add planting date column

# In[ ]:





# In[16]:


# Update df_* 
# df_6 will be renamed

timestamp = datetime.datetime.now().replace(microsecond=0).isoformat()
output_filename = f'pheno-table_{timestamp}.csv'.replace(':', '')
df_6.to_csv(f'../data/processed/{output_filename}')

