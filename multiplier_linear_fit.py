# %%
import pandas as pd
import numpy as np

df = pd.read_csv('normalizedMultipliers.csv', index_col=[0])
year = np.array(df.columns.astype(float))

slopes = []
for index, row in df.iterrows():
  current = np.array(row)
  slope, intercept = np.polyfit(year, current, 1)
  slopes.append(slope)
    

df['slopes'] = slopes
average = df.loc[:,'slopes'].mean()
deviation = df.loc[:,'slopes'].std()
print("The average slope from linear regression is: ", average)
print("Standard deviation: ", deviation)
# Here I get 0.022, which I guess means on average the multiplier is increasing 2% per year
# %%
df['slopes']