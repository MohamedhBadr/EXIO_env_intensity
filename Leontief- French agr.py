#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Get libraries 

from matplotlib.pyplot import title
import pymrio
import pandas 
import numpy as np
import pandas as pd


#Write Input for analysis 

#two letter code for country 
Country = 'FR'

ghg = 'GHG emissions (GWP100) | Problem oriented approach: baseline (CML, 2001) | GWP100 (IPCC, 2007)'


# ## Get the Leonfeif Inverse and merge into one dataframe to compare, get top 20 values

# In[5]:


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


# In[8]:


##Define Leonteif inverse for Each each year

#L matrix For 1996
L_1996 = exio3_1996.L[Country]
L_1998 = exio3_1998.L[Country]
L_2000 = exio3_2000.L[Country]
L_2002 = exio3_2002.L[Country]
L_2004 = exio3_2004.L[Country]
L_2006 = exio3_2006.L[Country]
L_2008 = exio3_2008.L[Country]
L_2010 = exio3_2010.L[Country]
L_2012 = exio3_2012.L[Country]
L_2014 = exio3_2014.L[Country]
L_2016 = exio3_2016.L[Country]
L_2018 = exio3_2018.L[Country]
L_2020 = exio3_2020.L[Country]
L_2022 = exio3_2022.L[Country]


# In[34]:


#get Leontief for agriculture
L_Agr_1996 = L_1996.iloc[:, 0:15]
L_Agr_1998 = L_1998.iloc[:, 0:15]
L_Agr_2000 = L_2000.iloc[:, 0:15]
L_Agr_2002 = L_2002.iloc[:, 0:15]
L_Agr_2004 = L_2004.iloc[:, 0:15]
L_Agr_2006 = L_2006.iloc[:, 0:15]
L_Agr_2008 = L_2008.iloc[:, 0:15]
L_Agr_2010 = L_2010.iloc[:, 0:15]
L_Agr_2012 = L_2012.iloc[:, 0:15]
L_Agr_2014 = L_2014.iloc[:, 0:15]
L_Agr_2016 = L_2016.iloc[:, 0:15]
L_Agr_2018 = L_2018.iloc[:, 0:15]
L_Agr_2020 = L_2020.iloc[:, 0:15]
L_Agr_2022 = L_2022.iloc[:, 0:15]


# In[72]:


#L_Agr_1996.groupby('sector')['Paddy rice'].nlargest(20)

sector = 'Oil seeds'

#1996
d = L_Agr_1996[sector].nlargest(10)
d = pd.DataFrame(data=d)
d.plot(kind='bar',title = sector +' Leontief Matrix- 1996', fontsize= 10)


# In[73]:


#2022
d2 = L_Agr_2022[sector].nlargest(10)
d2 = pd.DataFrame(data=d2)
d2.plot(kind='bar',title = sector +' Leontief Matrix- 2022', fontsize= 10)


# In[100]:


#Total Intermediate demand for 1996 per sector
France_output = exio3_1996.Z.loc[Country]
France_Agr_output = France_output.iloc[0:15]
Total_Intermediate_1996 = France_Agr_output.sum(axis=1)

#Total final demad 1996
Final_demand_FR = exio3_1996.Y.loc[Country]
Final_demand_FR_agr = Final_demand_FR.iloc[0:15]
Total_Finaldemand_1996 = Final_demand_FR_agr.sum(axis=1)

#merge and plot
data_Z =  { 'Intermediate':Total_Intermediate_1996, 'Final Demand':Total_Finaldemand_1996}
Compare = pd.DataFrame(data=data_Z )
Compare.plot(kind='bar', title = 'Intermediate vs Final Demand- 1996')


# In[139]:


#Total Intermediate demand for 2022 per sector
France_output_22 = exio3_2022.Z.loc[Country]
France_Agr_output22 = France_output_22.iloc[0:15]
Total_Intermediate_2022 = France_Agr_output22.sum(axis=1)

#Total final demad 2022
Final_demand_FR22 = exio3_2022.Y.loc[Country]
Final_demand_FR_agr22 = Final_demand_FR22.iloc[0:15]
Total_Finaldemand_2022 = Final_demand_FR_agr22.sum(axis=1)

#merge and plot
data_Z22 =  { 'Intermediate':Total_Intermediate_2022, 'Final Demand':Total_Finaldemand_2022}
Compare22 = pd.DataFrame(data=data_Z22 )
Compare22.plot(kind='bar', title = 'Intermediate vs Final Demand- 2022')


# In[141]:


#Find Exports as a percentage of total output of French Agriculture 1996

#1996 total ouptput
X_1996 = Total_Intermediate_1996 + Total_Finaldemand_1996

#calculate french intermediate consumption
France_output = exio3_1996.Z.loc[Country]
France_agr_Z = France_output[Country]
FZ_96 = France_agr_Z.iloc[0:15].sum(axis=1)

#calculate french final demand consumption
French_Y =  exio3_1996.Y.loc[Country]
French_Y = French_Y[Country]
French_Y_agr = French_Y.iloc[0:15].sum(axis=1)

#Calculate french consumption as a portion of total agricultural output -1996
consumption = French_Y_agr + FZ_96
ratio_1996 = consumption/X_1996
ratio_1996


# In[142]:


#Find Exports as a percentage of total output of French Agriculture - 2022

#2022 total ouptput
X_2022 = Total_Finaldemand_2022 + Total_Intermediate_2022

#calculate french intermediate consumption
France_output = exio3_2022.Z.loc[Country]
France_agr_Z = France_output[Country]
FZ_22 = France_agr_Z.iloc[0:15].sum(axis=1)

#calculate french final demand consumption
French_Y =  exio3_2022.Y.loc[Country]
French_Y = French_Y[Country]
French_Y_agr22 = French_Y.iloc[0:15].sum(axis=1)

#Calculate french consumption as a portion of total agricultural output -1996
consumption22 = French_Y_agr22 + FZ_22
ratio_2022 = consumption22/X_2022


# In[144]:


#Percentage of Total Domestic consumption of French agriculture goods

#merge and plot
consumptiondata =  { '1996':ratio_1996, '2022':ratio_2022}
Consumption_agr = pd.DataFrame(data=consumptiondata )
Consumption_agr.plot(kind='bar', title = 'Portion of Domestic Consumption for French Agricultural Products')


# In[ ]:




