# Evolution of CO2e multipliers over time: the case of French agriculture
### Mohamed Badr & Molly Strimbeck Bazilchuk 

Comparison of the carbon intensity of French agricultural production (1996-2022) using EXIOBASE3

Throughout this analysis the Pymrio python library is used to parse, read and analyse EXIOBASE3
https://pymrio.readthedocs.io/en/latest/intro.html#

**Research question(s):**  How have the multipliers of French agricultural sectors changed since 1995 with regards to GHG emissions? More so, has this decrease resulted in the overall decrease in carbon emmisions from Agriculture, or has this decrease been offset by a growth in consumption?

**Downloading the Data**

For this analysis we need to download EXIOBASE from: https://exiobase.eu/index.php/data-download/exiobase3mon?limit=20&limitstart=20 . You can also find instructions on how to download in the pymrio documentation. 

Current Prgress: until now the Pymrio library is used to parse EXIOBASE. Pymrio offers automated calculations of all matrices. Using the calc_all() function we can get the M matrix (multipliers) which we can then use for our analysis. We choose the GHG emissions (gwp100) indicator, and look at the Agricultural sector in France given its significance in Europe. 

**Methods:**
We use EXIOBASE3 input-ouptut tables (pymrio). We keep the original sector resolution of the 15 agricultural products. We use FAOSTAT data to create deflators and adjust according to consumer price index. 

**Basic Findings:**
There is a general downwards trend with regards to multiplier value in the sector. However, when adjusting to inflation we find that the multiplier values tend to increase with time. We also find that the total Carbon Footprint from French agriculture has not decreased from 1996 most likely due to a growth in consumption.  

Bar plot of change in GHG intensities per products (multiplier value) of french agriculture. After adjusting to inflation we find that the multiplier values tend to go up. Inflation is determined on the base year of 2015 as per FAOSTAT data. 
![presentation](https://user-images.githubusercontent.com/62759252/165483957-c1936ebf-fce6-4193-b058-04fbbe947caa.jpg)



Normalized GHG values (Normalized on the reference year of 1996. 
![normalized](https://user-images.githubusercontent.com/62759252/165484219-5d7336fc-8ddc-452e-9f04-43273db033d6.jpg)




