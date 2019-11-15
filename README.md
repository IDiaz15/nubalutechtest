# Nubalu Technical Test

Small project that contains the necessary files to meet the following requirements:

1. Go to this [INE data source](https://www.ine.es/jaxiT3/Tabla.htm?t=22356&L=0) and extract (non manual download) all available data of Indice de Precios de Consumo. Base 2016 (all provinces, subgroups, data types and months).
2. Give some logic structure to this data aiming to posterior querying by province.
3. Export structured data into a JSON file.

### Included files

The repository contains the following files:

* _**NubaluDataEngineerTest.ipynb**_ - Contains the code for the Python script to be executed in Jupyter
* _**NubaluDataEngineerTest.py**_ - Contains the code for the Python script to be executed using the Python compiler
* _**exportedJSON.gz**_ - Contains the exported structured JSON in a .gzip file because is higher than 25MB (limit in GitHub)
* _**README.md**_ - Markdown file that contains the documentation of the project

### Summary

The script uses _csv_ and _requests_ modules to get the CSV file which contains all the required information from INE data source.

The csv is splitted to store the values of (provinces, subgroups, type of data, periods and values). Once, all the values are extracted, they are used to create a new JSON Object with the structure required. This will allow the user to execute queries as in the INE portal. To perform a query is required to use the correct _**keys**_ for each column, this will display an output with the final _**value**_ that contains the CSV file for that filter.

Finally, the JSON object is exported into a JSON file in the same directory where the script is executed.
