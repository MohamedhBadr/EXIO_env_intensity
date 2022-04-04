# The Change in the Carbon intensity of French Agricultural Products
### Mohamed Badr & Molly Strimbeck Bazilchuk 

Comparison of the carbon intensity of French agricultural production (1996-2022) using EXIOBASE3

Throughout this analysis the Pymrio python library is used to parse and read in EXIOBASE3
https://pymrio.readthedocs.io/en/latest/intro.html#

**Research question(s):** How much have the multipliers of French agricultural products decreased from 1996 with regards to GHG emissions. More so, has this decrease resulted in the overall decrease in carbon emmisions from Agriculture, or has this decrease been offset by a growth in consumption?


**Downloading the Data**

For this analysis we need to download EXIOBASE from: https://exiobase.eu/index.php/data-download/exiobase3mon?limit=20&limitstart=20 . You can also find instructions on how to download in the pymrio documentation. 

Current Prgress: until now the Pymrio library is used to parse EXIOBASE. Pymrio offers automated calculations of all matrices. Using the calc_all() function we can get the M matrix (multipliers) which we can then use for our analysis. We choose the GHG emissions (gwp100) indicator, and look at the Agricultural sector in France given its significance in Europe. 

**Basic Findings:**
For now, using this code I can produce this visuallization which is just a comparision of multiplier intensitiy between 1996 and 2022. There is a general downwards trend with regards to carbon intensity of French agricultural products. We continue this analysis by exploring consumption based accounting (CBA) of the sector. We find that despite a reduction in multiplier intensity from 1996-2022, this has been largely offset by a growth in consumption. 

Bar plot of change in GHG intensities per products of french agriculture
![Bar_ghg](https://user-images.githubusercontent.com/62759252/161522259-05342f1f-eebf-4723-82db-5ab89a6e6844.png)


A Time series viualization showing change in multiplier value over time (using GHG). 
![line_ghg](https://user-images.githubusercontent.com/62759252/161522208-0478b956-66ed-4f21-ace0-53057aa0316a.png)


Change in D_cba (Impacts from Consumption based accounting from 1996-2022). We can see that despite multiplier reduction from 1996 to 2022, due to increase consumption the total impacts from the consumption of French agricultural products has increased in most sectors. 

![cba divergence](https://user-images.githubusercontent.com/62759252/161279446-c1cef288-8938-4ac4-a723-cba780c5be6e.png)


**Sector Analysis**

Here we can see how much the CBA footprint of a given sector has changed within the time frame. Values are normalized to the reference year 1996. 

![normalized_ghg_sector_bar](https://user-images.githubusercontent.com/62759252/161567579-5cbfe49a-97c2-4a86-86c9-1091d8f2bacc.png)



