
"""
Analysing he Carbon intensity of French Agricultural Products

Here we will just explore the data relevant to the Agricultural sector in France. 
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
#Load EXIOBASE 2003
exio3_2003 = pymrio.parse_exiobase3(path='IOT_2003_pxp.zip')
exio3_2003.calc_all()
#Load EXIOBASE 2008
exio3_2008 = pymrio.parse_exiobase3(path='IOT_2008_pxp.zip')
exio3_2008.calc_all()
#Load EXIOBASE 2011
exio3_2011 = pymrio.parse_exiobase3(path='exiobase3.4_iot_2011_pxp.zip')
exio3_2011.calc_all()
#Load EXIOBASE 2016
exio3_2016 = pymrio.parse_exiobase3(path='IOT_2016_pxp.zip')
exio3_2016.calc_all()
#load EXIOBASE 2020
exio3_2020 = pymrio.parse_exiobase3(path='IOT_2020_pxp.zip')
exio3_2020.calc_all()


# %%
#Sattelite Accounts
FR_Multipliers_1995 = exio3_1995.satellite.M[Country]
FR_Multipliers_2003 = exio3_2003.satellite.M[Country]
FR_Multipliers_2008 = exio3_2008.satellite.M[Country]
FR_Multipliers_2011 = exio3_2011.satellite.M[Country]
FR_Multipliers_2016 = exio3_2016.satellite.M[Country]
FR_Multipliers_2020 = exio3_2020.satellite.M[Country]


# %%
#Visualize M Matrix changes regarding Co2 Air combustion
#Air = FR_Multipliers_1995.loc[Stressor]
#Air.plot(figsize=(20,20), kind='barh')

# %%

#Get Agriculture multipliers
# It is my understanding that Agricultural products are located 
#in the first 17 columns (should double check)

FR_Agr_M_1995 = FR_Multipliers_1995.iloc[:, 0:17]
FR_Agr_M_2003 = FR_Multipliers_2003.iloc[:, 0:17]
FR_Agr_M_2008 = FR_Multipliers_2008.iloc[:, 0:17]
FR_Agr_M_2011 = FR_Multipliers_2011.iloc[:, 0:17]
FR_Agr_M_2016 = FR_Multipliers_2016.iloc[:, 0:17]
FR_Agr_M_2020 = FR_Multipliers_2020.iloc[:, 0:17]


# %%

#Comparing carbon intensities of of the French agricultural sector from 1995-2011

df1 = FR_Agr_M_1995.loc[Stressor]
df2= FR_Agr_M_2003.loc[Stressor]
df3= FR_Agr_M_2008.loc[Stressor]
df4 = FR_Agr_M_2011.loc[Stressor]
df5 = FR_Agr_M_2016.loc[Stressor]
df6 = FR_Agr_M_2020.loc[Stressor]

dfs = [df1, df2, df3, df4, df5, df6]

Merged_df = pd.concat(dfs, join='outer', axis=1).fillna(nan_value)
Merged_df = Merged_df.reset_index()
Merged_df.columns.values[[1, 2, 3, 4, 5, 6]] = ['1995','2003', '2008','2011','2016','2020']
Merged_df = Merged_df.set_index('sector')


# %%

#Visualize the findings

#wool has a massive carbon intensity
Merged_df.plot(kind = 'bar')

 #The value of Wool is too high and distorts the vizualization
 #Need to look more into this

Trial_df = Merged_df.drop(index = 'Wool, silk-worm cocoons')
Trial_df.plot(figsize=(15,15), kind='bar')

# %%
"""
From the above analyisis we can see that there is a general trend towards decorbonising the
agricultural sector in France (with the exception of wool). 
Keeping in mind that the indicator chosen here was 'C02- combustion- air'

I use the years 1995, 2008, 2011, and 2020, I think it could be interesting to witness the effects 
of global economic shocks (2008 financial crisis, and 2020 covid) on carbon intensities.

From this very primitive analysis we can say that there is a general decorbonisation trend within 
French Agriculture, however some sectors such as Paddy rice, Sugar cane, plant based fibers are 
very sensitive to economic shocks.It could be explained by prices of primary goods going up 
which hence decrease emissions per euro/dollar.  

#Follow up question: Despite a general trend of decarbonisation, is this offset by and increase in final demand? 
"""

# %%
"""
From the above analyisis we can see that there is a general trend towards decorbonising the
agricultural sector in France (with the exception of wool). 
Keeping in mind that the indicator chosen here was 'C02- combustion- air'

I use the years 1995, 2008, 2011, and 2020, I think it could be interesting to witness the effects 
of global economic shocks (2008 financial crisis, and 2020 covid) on carbon intensities.

"""
# %%
