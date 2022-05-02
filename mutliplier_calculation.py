# %%
# Load Libraries
import pymrio
import numpy as np
import pandas as pd

# Define Inputs
Country = 'FR'
charact_table = pd.read_csv('public_char_factors.csv',  sep='\t')
ghg = 'GHG emissions (GWP100) | Problem oriented approach: baseline (CML, 2001) | GWP100 (IPCC, 2007)'

years = [str(year) for year in [*range(1996, 2024, 2)]]

# %%
# Next we iterate over the year range
for year in years:
  currentpath = 'IOT_'+year+'_pxp.zip'
  # Load data
  print('Loading data for ', year)
  current_exio = pymrio.parse_exiobase3(path=currentpath)
  # Calculate system
  print('Calculating data for ', year)
  current_exio.calc_all()
  # Characterize system
  print('Characterizing data for ', year)
  current_multiplier = current_exio.impacts.M[Country].loc[[ghg]].iloc[:, 0:15]
  # Store relevant multipliers
  current_multiplier.to_excel('multipliers'+year+'.xlsx')
  print('Calculation for year ', year, ' complete')
