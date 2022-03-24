
"""
Here I will just explore the data relevant to the Agricultural sector in France. 
We are expecially interested with the carbon intesity of agricultural products in France 
and how they have changed over time. 

France was chosen given that it has a significant agricultural sector compared to the rest
of Europe

"""

# %%
# Load Libraries
import pymrio
import pandas 
import numpy
import pandas as pd


#Write Input for analysis 

#two letter code for country 
Country = 'FR'
Stressor = 'CO2 - combustion - air'

# %%
#load data

#Load EXIOBASE 1995
exio3_1995 = pymrio.parse_exiobase3(path='exiobase3.4_iot_1995_pxp.zip')
exio3_1995.calc_all()
#Load EXIOBASE 2011
exio3_2011 = pymrio.parse_exiobase3(path='exiobase3.4_iot_2011_pxp.zip')
exio3_2011.calc_all()

# %%

#Get the Z matrix for France
FR_Z = exio3_2011.Z[Country].loc[[Country]]

# %%
#Sattelite Accounts
FR_Multipliers_2011 = exio3_2011.satellite.M[Country]
FR_Multipliers_1995 = exio3_1995.satellite.M[Country]


# %%
#Visualize M Matrix changes regarding Co2 Air combustion
Air = FR_Multipliers_1995.loc[Stressor]
Air.plot(figsize=(100,100), kind='barh')

# %%

#Get Agriculture multipliers
# It is my understanding that Agricultural products are located 
#in the first 17 columns (should double check)

FR_Agr_M_1995 = FR_Multipliers_1995.iloc[:, 0:17]
FR_Agr_M_2011 = FR_Multipliers_2011.iloc[:, 0:17]


# %%

#Comparing carbon intensities of of the French agricultural sector from 1995-2011

df1 = FR_Agr_M_1995.loc[Stressor]
df2= FR_Agr_M_2011.loc[Stressor]
df3 = pd.merge(df1, df2, left_index=True, right_index=True)
df3= df3.rename({'CO2 - combustion - air_x':'1995', 'CO2 - combustion - air_y': '2011'}, axis='columns')
df3.plot(figsize=(10,10), kind='barh')


# %%
"""
From the above analyisis we can see that there is a general trend towards decorbonising the
agricultural sector in France (with the exception of wool). 
Keeping in mind that the indicator chosen here was 'C02- combustion- air'

To get a more wholisitic view more analysis is needed. 

"""
