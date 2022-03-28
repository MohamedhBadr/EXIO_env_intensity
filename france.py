
"""
Analysing he Carbon intensity of French Agricultural Products

Here we will just explore the data relevant to the Agricultural sector in France. 
We are expecially interested with the carbon intesity of agricultural products in France 
and how they have changed over time. 

France was chosen given that it has a significant agricultural sector compared to the rest
of Europe

Note: The loading and parsining of the EXIOBASE input output tables can take some time. 
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
#Load EXIOBASE 1996
exio3_1996 = pymrio.parse_exiobase3(path='IOT_1996_pxp.zip')
exio3_1996.calc_all()
#Load EXIOBASE 1997
exio3_1997 = pymrio.parse_exiobase3(path='IOT_1997_pxp.zip')
exio3_1997.calc_all()
#Load EXIOBASE 1998
exio3_1998 = pymrio.parse_exiobase3(path='IOT_1998_pxp.zip')
exio3_1998.calc_all()
#load EXIOBASE 1999
exio3_1999 = pymrio.parse_exiobase3(path='IOT_1999_pxp.zip')
exio3_1999.calc_all()
#Load EXIOBASE 2000
exio3_2000 = pymrio.parse_exiobase3(path='IOT_2000_pxp.zip')
exio3_2000.calc_all()
#Load EXIOBASE 2001
exio3_2001 = pymrio.parse_exiobase3(path='IOT_2001_pxp.zip')
exio3_2001.calc_all()
#Load EXIOBASE 2002
exio3_2002 = pymrio.parse_exiobase3(path='IOT_2002_pxp.zip')
exio3_2002.calc_all()
#Load EXIOBASE 2003
exio3_2003 = pymrio.parse_exiobase3(path='IOT_2003_pxp.zip')
exio3_2003.calc_all()
#Load EXIOBASE 2004
exio3_2004 = pymrio.parse_exiobase3(path='IOT_2004_pxp.zip')
exio3_2004.calc_all()
#Load EXIOBASE 2005
exio3_2005 = pymrio.parse_exiobase3(path='IOT_2005_pxp.zip')
exio3_2005.calc_all()
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
#load EXIOBASE 2022
exio3_2022 = pymrio.parse_exiobase3(path='IOT_2022_pxp.zip')
exio3_2022.calc_all()

# %%

# %%

# %%
#Sattelite Accounts
FR_Multipliers_1995 = exio3_1995.satellite.M[Country]
FR_Multipliers_1996 = exio3_1996.satellite.M[Country]
FR_Multipliers_1997 = exio3_1997.satellite.M[Country]
FR_Multipliers_1998 = exio3_1998.satellite.M[Country]
FR_Multipliers_1999 = exio3_1999.satellite.M[Country]
FR_Multipliers_2000 = exio3_2000.satellite.M[Country]
FR_Multipliers_2001 = exio3_2001.satellite.M[Country]
FR_Multipliers_2002 = exio3_2002.satellite.M[Country]
FR_Multipliers_2003 = exio3_2003.satellite.M[Country]
FR_Multipliers_2004 = exio3_2004.satellite.M[Country]
FR_Multipliers_2005 = exio3_2005.satellite.M[Country]
FR_Multipliers_2008 = exio3_2008.satellite.M[Country]
FR_Multipliers_2011 = exio3_2011.satellite.M[Country]
FR_Multipliers_2016 = exio3_2016.satellite.M[Country]
FR_Multipliers_2020 = exio3_2020.satellite.M[Country]
FR_Multipliers_2022 = exio3_2022.satellite.M[Country]



# %%

#Get Agriculture multipliers
# It is my understanding that Agricultural products are located 
#in the first 17 columns (should double check)

FR_Agr_M_1995 = FR_Multipliers_1995.iloc[:, 0:17]
FR_Agr_M_1996 = FR_Multipliers_1996.iloc[:, 0:17]
FR_Agr_M_1997 = FR_Multipliers_1997.iloc[:, 0:17]
FR_Agr_M_1998 = FR_Multipliers_1998.iloc[:, 0:17]
FR_Agr_M_1999 = FR_Multipliers_1999.iloc[:, 0:17]
FR_Agr_M_2000 = FR_Multipliers_2000.iloc[:, 0:17]
FR_Agr_M_2001 = FR_Multipliers_2001.iloc[:, 0:17]
FR_Agr_M_2002 = FR_Multipliers_2002.iloc[:, 0:17]
FR_Agr_M_2003 = FR_Multipliers_2003.iloc[:, 0:17]
FR_Agr_M_2004 = FR_Multipliers_2004.iloc[:, 0:17]
FR_Agr_M_2005 = FR_Multipliers_2005.iloc[:, 0:17]
FR_Agr_M_2008 = FR_Multipliers_2008.iloc[:, 0:17]
FR_Agr_M_2011 = FR_Multipliers_2011.iloc[:, 0:17]
FR_Agr_M_2016 = FR_Multipliers_2016.iloc[:, 0:17]
FR_Agr_M_2020 = FR_Multipliers_2020.iloc[:, 0:17]
FR_Agr_M_2022 = FR_Multipliers_2022.iloc[:, 0:17]


# %%

#Comparing carbon intensities of of the French agricultural sector from 1995-2011

df1 = FR_Agr_M_1995.loc[Stressor]
df2 = FR_Agr_M_1996.loc[Stressor]
df3 = FR_Agr_M_1997.loc[Stressor]
df4 = FR_Agr_M_1998.loc[Stressor]
df5 = FR_Agr_M_1999.loc[Stressor]
df6 = FR_Agr_M_2000.loc[Stressor]
df7 = FR_Agr_M_2001.loc[Stressor]
df8 = FR_Agr_M_2002.loc[Stressor]
df9 = FR_Agr_M_2003.loc[Stressor]
df10 = FR_Agr_M_2004.loc[Stressor]
df11 = FR_Agr_M_2005.loc[Stressor]
df12 = FR_Agr_M_2008.loc[Stressor]
df13 = FR_Agr_M_2011.loc[Stressor]
df14 = FR_Agr_M_2016.loc[Stressor]
df15 = FR_Agr_M_2020.loc[Stressor]
df16 = FR_Agr_M_2022.loc[Stressor]

dfs = [df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14, df15, df16]

Merged_df = pd.concat(dfs, join='outer', axis=1).fillna(0)
Merged_df = Merged_df.reset_index()
Merged_df.columns.values[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]] = ['1995','1996', '1997','1998', '1999','2000', '2001', '2002','2003','2004', '2005','2008','2011','2016','2020','2022']
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
#Define French Final Demand
Fr_Y = exio3_1995.Y.loc[Country]
Fr_agr_Y = Fr_Y[0:17] #agricultural French final demand


# %%
#Lets get Carbon footprint for 1995 from french Agriculture
#Using D= M@Y (Needs another Look)
D = FR_Agr_M_1995@Fr_agr_Y
D

# %%

#uncomment bellow if you want to save data

#file_name = 'trial_df.xlsx'
#Trial_df.to_excel(file_name)
#print('DataFrame is written to Excel File successfully.')

# %%
SecondTrial = Trial_df.T
SecondTrial.plot.line(figsize=(15,15))
