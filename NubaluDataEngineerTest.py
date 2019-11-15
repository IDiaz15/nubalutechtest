#!/usr/bin/env python
# coding: utf-8


# In[ ]:


import csv, requests, json

CSV_URL = 'https://www.ine.es/jaxiT3/files/t/es/csv_sc/22356.csv?nocab=1'

#Getting CSV file
with requests.Session() as s:
    download = s.get(CSV_URL)

    decoded_content = download.content.decode('utf-8')

    csvObject = csv.reader(decoded_content.splitlines(), delimiter=';')


# In[ ]:


#Getting Data types
[next(csvObject) for _ in range(5)]
dataTypes = next(csvObject)
dataTypes = list(filter(None, dataTypes))


# In[ ]:


#Getting Periods
periods = next(csvObject)
periods = periods[1:-1]


# In[ ]:


#Getting Provinces, Subgroups and Values
count = 0
provinces = []
subgroups = []
allSubGroups = []
values = []

for line in csvObject:
    if count == 0:
        provinces.append(line[0])
    else:
        subgroups.append(line[0].replace("    ",""))
        values.append(line[1:-1])
        
    count = count + 1
    if count == 44:
        count = 0
        allSubGroups.append(subgroups)
        subgroups = []
    
       
provinces = provinces[:-1]
#allSubGroups = allSubGroups[:-2]
values = values[:-2]


# In[ ]:


#Filling periods with values
numPeriods = len(periods)
numDataTypes = len(dataTypes)
numValues = len(values)

allPeriods = []
periodsList = {}
for x in range(numValues):
    for y in range(numPeriods):
        periodsList[periods[y]] = values[x][y]
        
        if y%(numPeriods/numDataTypes) == 0 and y != 0:
            allPeriods.append(periodsList)
            periodsList = {}

    allPeriods.append(periodsList)
    periodsList = {}
            


# In[ ]:


#Filling data types with periods
differentPeriods = round(numPeriods/numDataTypes)
allDataTypes = []
dataTypesList = {}
iterator = 0

for x in range(len(allPeriods)):
    dataTypesList[dataTypes[iterator]] = allPeriods[x]
    
    iterator = iterator + 1
    if iterator == numDataTypes:
        iterator = 0
        allDataTypes.append(dataTypesList)
        dataTypesList = {}


# In[ ]:


#Filling subgroups with data types
numSubGroups = len(allSubGroups[0])
numProvinces = len(allSubGroups)
allSubGroupsList = {}
allSubGroupsFilled = []
iterator = 0

for x in range(len(allDataTypes)):
    allSubGroupsList[allSubGroups[0][iterator]] = allDataTypes[x]
    
    iterator = iterator + 1
    if iterator == numSubGroups:
        iterator = 0
        allSubGroupsFilled.append(allSubGroupsList)
        allSubGroupsList = {}


# In[ ]:


#Filling provinces with subgroups
finalData = {}
for x in range(numProvinces):
    finalData[provinces[x]] = allSubGroupsFilled[x]


# In[ ]:


#Exporting JSON object to JSON file
jsonFilePath = 'exportedJson.json'

with open(jsonFilePath,'w') as jsonFile:
    jsonFile.write(json.dumps(finalData))


# In[ ]:


finalData["02 Albacete"]["011 Alimentos"]["Índice"]["2019M01"]


# In[ ]:




