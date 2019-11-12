#!/usr/bin/env python
# coding: utf-8


# In[ ]:


import pandas as pd
import json

#Reading CSV file from INE web    
df = pd.read_csv("https://www.ine.es/jaxiT3/files/t/es/csv/22356.csv?nocab=1", delimiter='\t', header=5, skipfooter=3)


# In[ ]:


#Parsing CSV file to create a list of provinces and values
numPeriods = round(df.shape[0]/44)
provinces = []
values = []

for x in range(numPeriods):
    row = x*44
    provinces.append(df.loc[row][0])
    values.append(df[row+1:row+44])
    


# In[ ]:


#Creating a JSON object with values per province
jsonData = {}
count = 0

for j in provinces:
    jsonData[j] = values[count].to_json()
    count = count + 1
    


# In[ ]:


#Exporting JSON object to JSON file
jsonFilePath = 'exportedJson.json'

with open(jsonFilePath,'w') as jsonFile:
    jsonFile.write(json.dumps(jsonData))


# In[ ]:




