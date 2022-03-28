# The Change in the Carbon intensity of French Agricultural Products
### Mohamed Badr & Molly Strimbeck Bazilchuk 

Comparison of the carbon intensity of French agricultural production (1995-2022) using EXIOBASE3

Throughout this analysis the Pymrio python library is used to parse and read in EXIOBASE3
https://pymrio.readthedocs.io/en/latest/intro.html#

**Research question(s):** How much have the multipliers of French agricultural products decreased from 1995 with regards to C02. More so, has this decrease resulted in the overall decrease in carbon emmisions from Agriculture, or has this decrease been offset by a growth in consumption?


**Downloading the Data**

For this analysis we need to download EXIOBASE from: https://exiobase.eu/index.php/data-download/exiobase3mon?limit=20&limitstart=20 . You can also find instructions on how to download in the pymrio documentation. 

How do consumption related impact multipliers (i.e., the environmental intensity of purchasing 1EUR of a sectors product) change over time? To what extent is the multiplier reduced over time, and will this rate be enough to achieve substantial reductions in environmental impacts if the current trends, including increases in consumption, continue? Which sectors are particularly relevant, and will there be a limit to how much individual sectors, or the whole economy, can become less intensive? Make a choice of indicator (carbon, land, biodiversity, materials) and regions.

Current Prgress: until now the Pymrio library is used to parse EXIOBASE. Pymrio offers automated calculations of all matrices. Using the calc_all() function we can get the M matrix (multipliers) which we can then use for our analysis. We still need to choose indicators and regions.

**Basic Findings:**
For now using this code I can produce this visuallization which is jsut a comparision of multiplier intensitiy between 1995 and 2020.There is a general downwards trend with regards to carbon intensity of French agricultural products. We can also see that in the years 2008 and 2020 there is a general reduction in multiplier value for most agricultural products. This can be explained by the increase of in prices of primary goods at times of global recession. 

![latest output](https://user-images.githubusercontent.com/62759252/160396834-5fc3c567-8c28-4e80-8186-7445c4e39481.png)


A Time series viualization showing change in multiplier value over time. 
![lineplot](https://user-images.githubusercontent.com/62759252/160396698-8f1d5909-d037-492b-855d-8d493e764ea1.png)


