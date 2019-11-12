# Nubalu Technical Test

Small project that contains the necessary files to meet the following requirements:

1. Go to this [INE data source](https://www.ine.es/jaxiT3/Tabla.htm?t=22356&L=0) and extract (non manual download) all available data of Indice de Precios de Consumo. Base 2016 (all provinces, subgroups, data types and months).
2. Give some logic structure to this data aiming to posterior querying by province.
3. Export structured data into a JSON file.

### Included files

The repository contains the following files:

* _**DataEngineerTest.ipynb**_ - Contains the code for the Python script to be executed in Jupyter
* _**DataEngineerTest.py**_ - Contains the code for the Python script to be executed using the Python compiler
* _**exportedJSON.gz**_ - Contains the exported structured JSON in a .gzip file because is higher than 25MB (limit in GitHub)
* _**README.md**_ - Markdown file that contains the documentation of the project

### Summary

The script uses Pandas module to get the CSV file which contains all the required information from INE data source.

As there are 43 subgroups, the CSV file is splitted in parts of 44 rows, first row is the Province and the other 43 rows the values for that province. So, a JSON object is built, each _**key**_ is the name of the Province and each _**value**_ is another JSON object with all the values for subgroups and in every period.

Finally, the JSON object is exported into a JSON file in the same directory where the script is executed.
