
"""
Analysing he Carbon intensity of French Agricultural Products

Here we will just explore the data relevant to the Agricultural sector in France. 
and adjust to inflation to see its effect on multiplier value. 

"""

# %%
# Load Libraries
import pymrio
import pandas 
import numpy as np
import pandas as pd

# Define Inputs
Country = 'FR'
charact_table = pd.read_csv('public_char_factors (1).csv',  sep='\t')
ghg = 'GHG emissions (GWP100) | Problem oriented approach: baseline (CML, 2001) | GWP100 (IPCC, 2007)'


# Load Data

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
#Get the GHG equivilent multipliers

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
impacts_2008 = exio3_2008.satellite.characterize(charact_table, name="impacts")
ghg_2008 = impacts_2008.F.loc[[ghg]]
ghg_2008 = ghg_2008[Country]
ghg_2008 = ghg_2008.iloc[:, 0:15]
ghg_2008

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
impacts_2020 = exio3_2020.satellite.characterize(charact_table, name="impacts")
ghg_2020 = impacts_2020.F.loc[[ghg]]
ghg_2020 = ghg_2020[Country]
ghg_2020 = ghg_2020.iloc[:, 0:15]


#Get GHG impacts in From French agriculture 2022
impacts_2022 = exio3_2022.satellite.characterize(charact_table, name="impacts")
ghg_2022 = impacts_2022.F.loc[[ghg]]
ghg_2022 = ghg_2022[Country]
ghg_2022 = ghg_2022.iloc[:, 0:15]

# %%
#Visualize

data = [ghg_1996,ghg_1998,ghg_2000,ghg_2002,ghg_2004,ghg_2006,ghg_2008, ghg_2010,ghg_2012,ghg_2014,ghg_2016,ghg_2018,ghg_2020,ghg_2022]

ghg_df = pd.concat(data).fillna(0)
ghg_df.index.values[[0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,12,13]] = ['1996','1998', '2000','2002', '2004','2006','2008', '2010','2012','2014', '2016','2018','2020','2022']
ghg_df = ghg_df.T
ghg_df.plot(figsize = (10,10), kind='bar', title = 'GHG emissions')

#With Wool
ghg_df.plot(figsize=(15,15), kind='bar')

#without Wool
Trial_ghg_df = ghg_df.drop(index = 'Wool, silk-worm cocoons')
Trial_ghg_df.plot(figsize=(15,15), kind='bar',title='French Agriculture Multiplier Value - GHG')

#Line plot not including wool
ghg_t = Trial_ghg_df.T
ghg_t.plot.line(figsize=(15,15),title='French Agriculture Multiplier Value- GHG')


# %%
#get Total impacts from consumption based accounting

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

#2006
FR_D_cba_2006 = exio3_2006.impacts.D_cba[Country]
FR_D_cba_agr_2006 = FR_D_cba_2006.iloc[:, 0:15]
FR_D_cba_agr_ghg_2006 = FR_D_cba_agr_2006.loc[ghg]
FR_D_cba_agr_ghg_2006

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
D_cba_data = [FR_D_cba_agr_ghg_1996,FR_D_cba_agr_ghg_2000,FR_D_cba_agr_ghg_2006,FR_D_cba_agr_ghg_2010,FR_D_cba_agr_ghg_2014,FR_D_cba_agr_ghg_2018,FR_D_cba_agr_ghg_2022]

D_cba_data_t = pd.concat(D_cba_data, join='outer', axis=1).fillna(0)
D_cba_data_t = D_cba_data_t.reset_index()
D_cba_data_t.columns.values[[1, 2,3,4,5,6,7]] = ['1996','2000','2006','2010','2014','2018','2022']
D_cba_data_t = D_cba_data_t.set_index('sector')
D_cba_data_t.plot(figsize=(10,10),kind = 'bar',title='Consumption Based accounts')


"""
For more details and the data sources feel free to explore the github repository:
github.com/MohamedhBadr/EXIO_env_intensity 

The inflation script/data is also on the same github repository. 

"""