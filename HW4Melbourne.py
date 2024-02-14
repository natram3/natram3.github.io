# %%

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# %% Load data

# Set path of your working directory - change yours here!
# Load data
#Changed data path from Data/ to within same folder (Documents/266G)



DKeno = pd.read_excel('KlamathDischargeatKeno.xlsx', skiprows= range(1,2))
dfKeno = pd.DataFrame(DKeno, columns= ['month_nu','mean_va'])
# Unit conversion
cfs_to_tafd = 2.29568411 * 10 ** -5 * 86400 / 1000  # unit conversion of

# Create variables for each

dischargeKeno = dfKeno['mean_va'] * cfs_to_tafd  # TAF/d

plt.plot(dischargeKeno, label='Discharge')
# plt.plot(inflow, label='Inflow')
plt.xlabel('Months since Nov 1960')
plt.ylabel('Discharge (TAF)')
plt.title("Time Series of Discharge at Keno")
plt.ylim([0, 25])
plt.legend()
plt.show()

DIronGate = pd.read_excel('IronGateDischarge.xlsx', skiprows= range(1,2))
dfIronGate = pd.DataFrame(DIronGate, columns= ['month_nu','mean_va'])
# Unit conversion
cfs_to_tafd = 2.29568411 * 10 ** -5 * 86400 / 1000  # unit conversion of

# Create variables for each

dischargeIronGate = dfIronGate['mean_va'] * cfs_to_tafd  # TAF/d

# plot the time series of storage
# plt.plot(storage)
# plt.xlabel('Days since Oct 1 2000')
# plt.ylabel('Storage (TAF)')
# plt.title("Time Series of Storage")
# plt.ylim([0, 725])
# plt.show()

# # plot time series of inflow and outflow on the same plot
plt.plot(dischargeIronGate, label='Discharge')
# plt.plot(inflow, label='Inflow')
plt.xlabel('Months since Nov 1960')
plt.ylabel('Discharge (TAF)')
plt.title("Time Series of Discharge at Iron Gate")
plt.ylim([0, 25])
plt.legend()
plt.show()

# plot an exceedance plot of the log of daily streamflow values
# an exceedance plot shows the range of log streamflow (inflow) values on the vertical axis
# on the horizontal axis, it shows the frequency with which the log streamflow (inflow?) values
# in the historical record are less than or equal to that value
# see assignment for an example of an exceedance plot
# use ONLY numpy and matplotlib functions
# P = m / (n+1)

#
# inflow_sort = np.sort(inflow)
# rev_inflow = inflow_sort[::-1]
# rank = np.arange(1, len(inflow) + 1)
#
# EP = rank / (np.size(rev_inflow) + 1) * 100
#
# plt.plot(EP, rev_inflow, label="Inflow")
# plt.yscale('log')
# plt.xlabel('Exceedance Probability (%)')
# plt.ylabel('Flow (TAF/d)')
# plt.title("Exceedance Plot of the log of Daily Streamflow Values")
# plt.legend()
# plt.show()
#
# # plot historical storage for folsom, oroville, and shasta on the same graph
# # These datasets are available in the "FOL.csv", "ORO.csv", and "SHA.csv" files respectively
# # use a for loop so that the commands "np.loadtxt" and "plt.plot" only appear once in your code
# # be sure to include axis labels and a legend
#
# files = ["FOL", "ORO", "SHA"]
# loop_plot = plt.figure()
#
# for file in files:
#     load = np.loadtxt(file + ".csv", delimiter=',',
#                       skiprows=1, usecols=[1, 2, 3, 4])
#     storage = load[:, 0]  # TAF
#     plt.plot(storage, label=file)
# plt.xlabel('Days since Oct 1 2000')
# plt.ylabel('Storage (TAF)')
# plt.title("Historical Storage, all Data Sets")
# plt.legend()
# plt.ylim([0, 5000])
# loop_plot.savefig("HW1.pdf")
# plt.show()
#
# # save your last figure as a pdf
#
#
# # %% Problem 2: Pandas, Numpy, and Matplotlib
#
# import pandas as pd
#
# # load data
# dailyQ = pd.read_csv('SHA.csv')
#
# # change first column name to 'date'
# dailyQ = dailyQ.rename(columns={'datetime': 'date'})
#
# # convert first column to date
# dailyQ['date'] = pd.to_datetime(dailyQ['date'], format="%Y-%m-%d")
#
# # add a column to dailyQ called 'year' with the year of each data point
# dailyQ['year'] = dailyQ['date'].dt.year
#
# # print a list of the unique years in the dataset
# years = np.unique(dailyQ['year'])
# print(years)
#
# # drop all columns except date, year, storage, inflow, outflow
#
# dailyQ = dailyQ[['date', 'year', 'storage', 'inflow', 'outflow']]
#
# # print a list of the column names in dailyQ
#
# list(dailyQ.columns)
#
# # make a new variable called "annQ" with the mean annual inflow
# annQ = np.array(dailyQ.groupby('year').mean()['inflow'])
#
# # make a bar plot of annQ by year
# plt.figure()
# plt.bar(years, annQ)
# plt.ylabel('Annual mean inflow (TAF/d)')
# plt.xlabel('Year')
# plt.show()
#
# # edit your bar plot to highlight drought years in orange
# # define drought years as years with <5000 TAF/d in mean inflow)
# # be sure to include a legend
# # apply an inequality to get a T/F for the whole array
# # then plot if true
#
# drought = annQ < 5000
#
# plt.figure()
# plt.bar(years[drought], annQ[drought], color='orange', label="Drought Year")
# plt.bar(years[~drought], annQ[~drought], label="Non-drought Year")
# plt.ylabel('Annual mean inflow (TAF/d)')
# plt.xlabel('Year')
# plt.legend()
# plt.show()
#
# # add a new column called "month" to daily Q with the month of each data point
#
# dailyQ['month'] = dailyQ['date'].dt.month
#
# # Make a new variable called "monthS" with the mean monthly storage level
#
#
# monthS = np.array(dailyQ.groupby('month').mean()['storage'])
#
# # Write a function called "wet_spring" that returns "True" if the highest mean storage level
# # occurs in March, April, or May and returns "False" otherwise
# # dailyQ['date'] = pd.to_datetime(dailyQ['date'], format="%m").dt.month_name()
# # false?
# spring = [2, 3, 4]
#
#
# def wet_spring(monthS):
#     max_storage_index = monthS.argmax()
#     if max_storage_index in spring:
#         return True
#     else:
#         return False
#
#
# # Apply the function to monthS and print the result
#
# print(wet_spring(monthS))
#
# # make a bar plot of the mean monthly reservoir storage level
# # Be sure to include axis labels with units
# # label each month with the first letter of the month (J F M A M J J A S O N D)
# x = list(range(12))
# letters = ['J', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D']
# plt.figure()
# plt.xticks(x, letters)
# plt.bar(x, monthS)
# plt.xlabel("Months")
# plt.ylabel('Mean Reservoir Storage Level (TAF/d)')
# plt.show()
