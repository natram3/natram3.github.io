import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('KenoDamDailyData.csv', delimiter=',', skiprows=2, usecols=[2,3])

df['date'] = pd.to_datetime(df['date'],'%Y-%m-%d')

df_1 = df.loc[(df['date'] >= '2020-03-01') & (df['date'] < '2020-07-31')]