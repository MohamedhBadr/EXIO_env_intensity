# %%

#load libraries
import pymrio
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %%
#Question: 10
# Comparison of environmental intensity of economic production over time.
# Database: EXIOBASE


#Load EXIOBASE 1995
exio3_1995 = pymrio.parse_exiobase3(path='exiobase3.4_iot_1995_pxp.zip')
exio3_1995.calc_all()

# %%
#Load EXIOBASE 2011
exio3_2011 = pymrio.parse_exiobase3(path='exiobase3.4_iot_2011_pxp.zip')
exio3_2011.calc_all()


# %%
#a visualization of the A matrix of 2011

plt.figure(figsize=(15,15))
plt.imshow(exio3_2011.A, vmax=1E-3)
plt.xlabel('Countries - sectors')
plt.ylabel('Countries - sectors')
plt.show()

# %%
#Get the Multiplier Matrix for the years 1995 and 2011 
Multipliers_2011 = exio3_2011.satellite.M
Multipliers_1995 = exio3_1995.satellite.M

# %%
#If we would like to select air for example we can select all rows in the M matrix containing "air"
indicator = ' air'
Air_mulitpliers_2011 = Multipliers_2011[[indicator in s for s in Multipliers_2011.index]]
Air_mulitpliers_1995 = Multipliers_1995[[indicator in s for s in Multipliers_1995.index]]

# %%
#from that we can get specific regions
Country_code = 'US'
US_2011_air = Air_mulitpliers_2011[Country_code]
US_1995_air = Air_mulitpliers_1995[Country_code]

# %%
#Visualizing he most significant stressors on Air in the US using the M matrix
pd.set_option('display.precision', 2)
US_2011_air.style.background_gradient(cmap ='Blues')
# %%

#Lets see the largest contributers to Co2 combustion- air
US_1995_air.loc['CO2 - combustion - air'].plot(figsize=(100,100), kind='barh')
# %%
#Can we merge the two plots of Co2 emissions on air in the US and compare between 1995 and 2011?
df1 = US_1995_air.loc['CO2 - combustion - air']
df2= US_2011_air.loc['CO2 - combustion - air']
df3 = pd.merge(df1, df2, left_index=True, right_index=True)
df3= df3.rename({'CO2 - combustion - air_x':'1995', 'CO2 - combustion - air_y': '2011'}, axis='columns')

# %%
#in the bellow plot we can see that in most cases the multiplier intensities have gone down for most industries from 1995-2011
df3.plot(figsize=(100,100), kind='barh')

# %%
#If this works fine we can move on to load the rest of the years from exiobase and specifiying the region, stressor, and maybe sector. 
