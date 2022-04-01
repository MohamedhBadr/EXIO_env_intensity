
"""
Analysing he Carbon intensity of French Agricultural Products

Here we will just explore the data relevant to the Agricultural sector in France. 
We are expecially interested with the carbon intesity of agricultural products in France 
and how they have changed over time. 

France was chosen given that it has a significant agricultural sector compared to the rest
of Europe

Note: The loading and parsining of the EXIOBASE input output tables can take some time.
so we use every other year 
"""

# %%
# Load Libraries
import pymrio
import pandas 
import numpy as np
import pandas as pd


#Write Input for analysis 

#two letter code for country 
Country = 'FR'
Stressor = 'CO2 - combustion - air'

# %%
#load data

#Load EXIOBASE 1996
exio3_1996 = pymrio.parse_exiobase3(path='IOT_1996_pxp.zip')
exio3_1996.calc_all()
#Load EXIOBASE 1998
exio3_1998 = pymrio.parse_exiobase3(path='IOT_1998_pxp.zip')
exio3_1998.calc_all()
#Load EXIOBASE 2000
exio3_2000 = pymrio.parse_exiobase3(path='IOT_2000_pxp.zip')
exio3_2000.calc_all()
#Load EXIOBASE 2002
exio3_2002 = pymrio.parse_exiobase3(path='IOT_2002_pxp.zip')
exio3_2002.calc_all()
#Load EXIOBASE 2004
exio3_2004 = pymrio.parse_exiobase3(path='IOT_2004_pxp.zip')
exio3_2004.calc_all()
#Load EXIOBASE 2006
exio3_2006 = pymrio.parse_exiobase3(path='IOT_2006_pxp.zip')
exio3_2006.calc_all()
#Load EXIOBASE 2008
exio3_2008 = pymrio.parse_exiobase3(path='IOT_2008_pxp.zip')
exio3_2008.calc_all()
#Load EXIOBASE 2010
exio3_2010 = pymrio.parse_exiobase3(path='IOT_2010_pxp.zip')
exio3_2010.calc_all()
#Load EXIOBASE 2012
exio3_2012 = pymrio.parse_exiobase3(path='IOT_2012_pxp.zip')
exio3_2012.calc_all()
#Load EXIOBASE 2014
exio3_2014 = pymrio.parse_exiobase3(path='IOT_2014_pxp.zip')
exio3_2014.calc_all()
#Load EXIOBASE 2016
exio3_2016 = pymrio.parse_exiobase3(path='IOT_2016_pxp.zip')
exio3_2016.calc_all()
#Load EXIOBASE 2018
exio3_2018 = pymrio.parse_exiobase3(path='IOT_2018_pxp.zip')
exio3_2018.calc_all()
#load EXIOBASE 2020
exio3_2020 = pymrio.parse_exiobase3(path='IOT_2020_pxp.zip')
exio3_2020.calc_all()
#load EXIOBASE 2022
exio3_2022 = pymrio.parse_exiobase3(path='IOT_2022_pxp.zip')
exio3_2022.calc_all()


# %%
#Sattelite Accounts
FR_Multipliers_1996 = exio3_1996.satellite.M[Country]
FR_Multipliers_1998 = exio3_1998.satellite.M[Country]
FR_Multipliers_2000 = exio3_2000.satellite.M[Country]
FR_Multipliers_2002 = exio3_2002.satellite.M[Country]
FR_Multipliers_2004 = exio3_2004.satellite.M[Country]
FR_Multipliers_2006 = exio3_2006.satellite.M[Country]
FR_Multipliers_2008 = exio3_2008.satellite.M[Country]
FR_Multipliers_2010 = exio3_2010.satellite.M[Country]
FR_Multipliers_2012 = exio3_2012.satellite.M[Country]
FR_Multipliers_2014 = exio3_2014.satellite.M[Country]
FR_Multipliers_2016 = exio3_2016.satellite.M[Country]
FR_Multipliers_2018 = exio3_2018.satellite.M[Country]
FR_Multipliers_2020 = exio3_2020.satellite.M[Country]
FR_Multipliers_2022 = exio3_2022.satellite.M[Country]



# %%

#Get Agriculture multipliers
# It is my understanding that Agricultural products are located 
#in the first 17 columns (should double check)

FR_Agr_M_1996 = FR_Multipliers_1996.iloc[:, 0:15]
FR_Agr_M_1998 = FR_Multipliers_1998.iloc[:, 0:15]
FR_Agr_M_2000 = FR_Multipliers_2000.iloc[:, 0:15]
FR_Agr_M_2002 = FR_Multipliers_2002.iloc[:, 0:15]
FR_Agr_M_2004 = FR_Multipliers_2004.iloc[:, 0:15]
FR_Agr_M_2006 = FR_Multipliers_2006.iloc[:, 0:15]
FR_Agr_M_2008 = FR_Multipliers_2008.iloc[:, 0:15]
FR_Agr_M_2010 = FR_Multipliers_2010.iloc[:, 0:15]
FR_Agr_M_2012 = FR_Multipliers_2012.iloc[:, 0:15]
FR_Agr_M_2014 = FR_Multipliers_2014.iloc[:, 0:15]
FR_Agr_M_2016 = FR_Multipliers_2016.iloc[:, 0:15]
FR_Agr_M_2018 = FR_Multipliers_2018.iloc[:, 0:15]
FR_Agr_M_2020 = FR_Multipliers_2020.iloc[:, 0:15]
FR_Agr_M_2022 = FR_Multipliers_2022.iloc[:, 0:15]


# %%

#Comparing carbon intensities of of the French agricultural sector from 1995-2011

df1 = FR_Agr_M_1996.loc[Stressor]
df2 = FR_Agr_M_1998.loc[Stressor]
df3 = FR_Agr_M_2000.loc[Stressor]
df4 = FR_Agr_M_2002.loc[Stressor]
df5 = FR_Agr_M_2004.loc[Stressor]
df6 = FR_Agr_M_2006.loc[Stressor]
df7 = FR_Agr_M_2008.loc[Stressor]
df8 = FR_Agr_M_2010.loc[Stressor]
df9 = FR_Agr_M_2012.loc[Stressor]
df10 = FR_Agr_M_2014.loc[Stressor]
df11 = FR_Agr_M_2016.loc[Stressor]
df12 = FR_Agr_M_2018.loc[Stressor]
df13 = FR_Agr_M_2020.loc[Stressor]
df14 = FR_Agr_M_2022.loc[Stressor]

dfs = [df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14]

Merged_df = pd.concat(dfs, join='outer', axis=1).fillna(0)
Merged_df = Merged_df.reset_index()
Merged_df.columns.values[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]] = ['1996','1998', '2000','2002', '2004','2006', '2008', '2010','2012','2014', '2016','2018','2020','2022']
Merged_df = Merged_df.set_index('sector')


# %%

#Visualize the findings

#wool has a massive carbon intensity
Merged_df.plot(kind = 'bar')

 #The value of Wool is too high and distorts the vizualization
 #Need to look more into this

Trial_df = Merged_df.drop(index = 'Wool, silk-worm cocoons')
Trial_df.plot(figsize=(15,15), kind='bar')

SecondTrial = Trial_df.T
SecondTrial.plot.line(figsize=(15,15))

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

"""
From the D_cba matrix we can look at the GHG emissions per country
and plot accordingly 
 
"""
# %%

#GET Total GHG emissions

charact_table = pd.read_csv('public_char_factors (1).csv',  sep='\t')
ghg = 'GHG emissions (GWP100) | Problem oriented approach: baseline (CML, 2001) | GWP100 (IPCC, 2007)'

#Get GHG impacts in From French agriculture 1996
impacts_1996 = exio3_1996.satellite.characterize(charact_table, name="impacts")
ghg_1996 = impacts_1996.F.loc[[ghg]]
ghg_1996 = ghg_1996[Country]
ghg_1996 = ghg_1996.iloc[:, 0:15]
ghg_1996

#Get GHG impacts in From French agriculture 1998
impacts_1998 = exio3_1998.satellite.characterize(charact_table, name="impacts")
ghg_1998 = impacts_1998.F.loc[[ghg]]
ghg_1998 = ghg_1998[Country]
ghg_1998 = ghg_1998.iloc[:, 0:15]
ghg_1998

#Get GHG impacts in From French agriculture 2000
impacts_2000 = exio3_2000.satellite.characterize(charact_table, name="impacts")
ghg_2000 = impacts_2000.F.loc[[ghg]]
ghg_2000 = ghg_2000[Country]
ghg_2000 = ghg_2000.iloc[:, 0:15]
ghg_2000

#Get GHG impacts in From French agriculture 2002
impacts_2002 = exio3_2002.satellite.characterize(charact_table, name="impacts")
ghg_2002 = impacts_2002.F.loc[[ghg]]
ghg_2002 = ghg_2002[Country]
ghg_2002 = ghg_2002.iloc[:, 0:15]
ghg_2002

#Get GHG impacts in From French agriculture 2004
impacts_2004 = exio3_2004.satellite.characterize(charact_table, name="impacts")
ghg_2004 = impacts_2004.F.loc[[ghg]]
ghg_2004 = ghg_2004[Country]
ghg_2004 = ghg_2004.iloc[:, 0:15]
ghg_2004

#Get GHG impacts in From French agriculture 2006
impacts_2006 = exio3_2006.satellite.characterize(charact_table, name="impacts")
ghg_2006 = impacts_2006.F.loc[[ghg]]
ghg_2006 = ghg_2006[Country]
ghg_2006 = ghg_2006.iloc[:, 0:15]
ghg_2006

#Get GHG impacts in From French agriculture 2008
#impacts_2008 = exio3_2008.satellite.characterize(charact_table, name="impacts")
#ghg_2008 = impacts_2008.F.loc[[ghg]]
#ghg_2008 = ghg_2008[Country]
#ghg_2008 = ghg_2008.iloc[:, 0:15]
#ghg_2008

#Get GHG impacts in From French agriculture 2010
impacts_2010 = exio3_2010.satellite.characterize(charact_table, name="impacts")
ghg_2010 = impacts_2010.F.loc[[ghg]]
ghg_2010 = ghg_2010[Country]
ghg_2010 = ghg_2010.iloc[:, 0:15]
ghg_2010

#Get GHG impacts in From French agriculture 2012
impacts_2012 = exio3_2012.satellite.characterize(charact_table, name="impacts")
ghg_2012 = impacts_2012.F.loc[[ghg]]
ghg_2012 = ghg_2012[Country]
ghg_2012 = ghg_2012.iloc[:, 0:15]
ghg_2012

#Get GHG impacts in From French agriculture 2014
impacts_2014 = exio3_2014.satellite.characterize(charact_table, name="impacts")
ghg_2014 = impacts_2014.F.loc[[ghg]]
ghg_2014 = ghg_2014[Country]
ghg_2014 = ghg_2014.iloc[:, 0:15]
ghg_2014

#Get GHG impacts in From French agriculture 2016
impacts_2016 = exio3_2016.satellite.characterize(charact_table, name="impacts")
ghg_2016 = impacts_2016.F.loc[[ghg]]
ghg_2016 = ghg_2016[Country]
ghg_2016 = ghg_2016.iloc[:, 0:15]
ghg_2016

#Get GHG impacts in From French agriculture 2018
impacts_2018 = exio3_2018.satellite.characterize(charact_table, name="impacts")
ghg_2018 = impacts_2018.F.loc[[ghg]]
ghg_2018 = ghg_2018[Country]
ghg_2018 = ghg_2018.iloc[:, 0:15]
ghg_2018

#Get GHG impacts in From French agriculture 2020
#impacts_2020 = exio3_2020.satellite.characterize(charact_table, name="impacts")
#ghg_2020 = impacts_2020.F.loc[[ghg]]
#ghg_2020 = ghg_2020[Country]
#ghg_2020 = ghg_2020.iloc[:, 0:15]
#ghg_2020

#Get GHG impacts in From French agriculture 2022
impacts_2022 = exio3_2022.satellite.characterize(charact_table, name="impacts")
ghg_2022 = impacts_2022.F.loc[[ghg]]
ghg_2022 = ghg_2022[Country]
ghg_2022 = ghg_2022.iloc[:, 0:15]

# %%
#Visualize

data = [ghg_1996,ghg_1998,ghg_2000,ghg_2002,ghg_2004,ghg_2006,ghg_2010,ghg_2012,ghg_2014,ghg_2016,ghg_2018,ghg_2022]

ghg_df = pd.concat(dfs, join='outer', axis=1).fillna(0)
ghg_df = ghg_df.reset_index()
ghg_df.columns.values[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]] = ['1996','1998', '2000','2002', '2004','2006','2010','2012','2014','2016','2018','2022']
ghg_df = ghg_df.set_index('sector')

#With Wool
ghg_df.plot(figsize=(15,15), kind='bar')

#without Wool
Trial_ghg_df = ghg_df.drop(index = 'Wool, silk-worm cocoons')
Trial_ghg_df.plot(figsize=(15,15), kind='bar')

#Line plot not including wool
ghg_t = Trial_ghg_df.T
ghg_t.plot.line(figsize=(15,15))

### NOTE:
## For some reason the characterization factors function
## Doesn't work on the years 2008 and 2020 
## does this have to do with the recession

# %%

#GET Total impacts from consumption based accounting

#1996
FR_D_cba_1996 = exio3_1996.impacts.D_cba[Country]
FR_D_cba_agr_1996 = FR_D_cba_1996.iloc[:, 0:15]
FR_D_cba_agr_ghg_1996 = FR_D_cba_agr_1996.loc[ghg]
FR_D_cba_agr_ghg_1996

#2000
FR_D_cba_2000 = exio3_2000.impacts.D_cba[Country]
FR_D_cba_agr_2000 = FR_D_cba_2000.iloc[:, 0:15]
FR_D_cba_agr_ghg_2000 = FR_D_cba_agr_2000.loc[ghg]
FR_D_cba_agr_ghg_2000

#2010
FR_D_cba_2010 = exio3_2010.impacts.D_cba[Country]
FR_D_cba_agr_2010 = FR_D_cba_2010.iloc[:, 0:15]
FR_D_cba_agr_ghg_2010 = FR_D_cba_agr_2010.loc[ghg]
FR_D_cba_agr_ghg_2010


#2014
FR_D_cba_2014 = exio3_2014.impacts.D_cba[Country]
FR_D_cba_agr_2014 = FR_D_cba_2014.iloc[:, 0:15]
FR_D_cba_agr_ghg_2014 = FR_D_cba_agr_2014.loc[ghg]
FR_D_cba_agr_ghg_2014

#2018
FR_D_cba_2018 = exio3_2018.impacts.D_cba[Country]
FR_D_cba_agr_2018 = FR_D_cba_2018.iloc[:, 0:15]
FR_D_cba_agr_ghg_2018 = FR_D_cba_agr_2018.loc[ghg]
FR_D_cba_agr_ghg_2018

#2022
FR_D_cba_2022 = exio3_2022.impacts.D_cba[Country]
FR_D_cba_agr_2022 = FR_D_cba_2022.iloc[:, 0:15]
FR_D_cba_agr_ghg_2022 = FR_D_cba_agr_2022.loc[ghg]
FR_D_cba_agr_ghg_2022



# %%

#Bar Plot
D_cba_data = [FR_D_cba_agr_ghg_1996,FR_D_cba_agr_ghg_2000,FR_D_cba_agr_ghg_2010,FR_D_cba_agr_ghg_2014,FR_D_cba_agr_ghg_2018,FR_D_cba_agr_ghg_2022]

D_cba_data_t = pd.concat(D_cba_data, join='outer', axis=1).fillna(0)
D_cba_data_t = D_cba_data_t.reset_index()
D_cba_data_t.columns.values[[1, 2,3,4,5,6]] = ['1996','2000','2010','2014','2018','2022']
D_cba_data_t = D_cba_data_t.set_index('sector')
D_cba_data_t.plot(figsize=(10,10),kind = 'bar')
