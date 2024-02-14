# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# %%

# Load Cumberland MD daily precip (inches)
data = pd.read_csv('cumberland_md_daily_precip.txt', sep='\t', usecols=['datetime', 'precip'])

# Fill NaNs with zeros
data.fillna(0, inplace=True)

# Make date strings into datetime format so we can calculate dates
data['datetime'] = pd.to_datetime(data['datetime'])

# Add a new column indicating whether there is precip or not
data['wet'] = np.zeros_like(data['precip'])
data.loc[data['precip'] > 0, 'wet'] = 1

# Add a new column indicating whether there is precip the previous day
data['wet_prev'] = data['wet'].shift()

# b
data['wet_.5'] = np.zeros_like(data['precip'])
data.loc[data['precip'] > .5, 'wet_.5'] = 1
print(sum(data['wet_.5']))
# 147

# c

print(data['precip'].mean())
# .09

data_conditional = data[data['precip'] > 0]
print(data_conditional['precip'].mean())
# .284

# d
print(data['wet'].mean())
#.3272

data_conditional2 = data[data['wet_prev'] == 1]
print(data_conditional2['wet'].mean())
#.525

# %%

data_14 = data[data['datetime'].dt.year == 2014]
days = range(len(data_14))

# %%
plt.bar(days, data_14['precip'], label='Precipitation')
plt.xlabel('Days since March 3 2014')
plt.ylabel('Precipitation (inches)')
plt.title('Daily Precipitation Data 2014')
plt.show()
