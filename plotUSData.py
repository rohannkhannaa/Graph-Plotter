# Code written by :
#       Rohan Khanna
#       2020csb1117@iitrpr.ac.in
#       Futures First Assignment 1 

# Importing lobraries
import pandas as pd
import matplotlib.pyplot as plt

# Read excel sheet name : Economic Data.xlsx, sheet_name can be US, UK or EZ
# Data is from coloum F to SV
# Code is changed here itself to plot specific data.
# To test graph, make sure Economic Data.xlsx file is in same directory of python code

df = pd.read_excel('Economic Data.xlsx', sheet_name='us', header=None, skiprows=3, usecols="F:SV")
df_gdp = pd.read_excel('Economic Data.xlsx', sheet_name='us', header=None, skiprows=3, usecols="F:FS")

# iloc for moving to specific row of data
# iloc[0] for dates
# iloc[1] for Retail sales

dates = df.iloc[0].tolist() 

# UnComment the lines you want to plot, simple it is, and then run python code.

# line2, = plt.plot(dates, df.iloc[2].tolist(),label = "Retail Sales MM")
# line1, = plt.plot(dates, df.iloc[1].tolist(), label = "Retail Sales Ex-Autos MM")

# # line3, = plt.plot(dates, df.iloc[3].tolist() ,label = "Building Permits Number")

# line4, = plt.plot(dates, df.iloc[4].tolist() ,label = "Consumer Confidence")

line5, = plt.plot(dates, df.iloc[5].tolist() ,label = "ISM Manufacturing PMI")
line6, = plt.plot(dates, df.iloc[6].tolist() ,label = "ISM Non-Manufacturing PMI")

# line11, = plt.plot(dates, df.iloc[11].tolist()  , label = "Core CPI MM, SA")
# line7, = plt.plot(dates, df.iloc[7].tolist() ,label = "Core PCE MM")

# line8, = plt.plot(dates, df.iloc[8].tolist() ,label = "Core PCE YY")
# line12, = plt.plot(dates, df.iloc[12].tolist() ,label = "Core CPI YY, NSA")

# line13, = plt.plot(dates, df.iloc[13].tolist() ,  label = "CPI MM, SA")
# line9, = plt.plot(dates, df.iloc[9].tolist() ,label = "PCE MM")

# line10, = plt.plot(dates, df.iloc[10].tolist() ,label = "PCE YY")
# line14, = plt.plot(dates, df.iloc[14].tolist() ,label = "CPI YY, NSA")

# line15, = plt.plot(dates, df.iloc[15].tolist() ,label = "Unemployment Rate")

line19, = plt.plot(dates, df.iloc[19].tolist() ,label = "Non-Farm Payrolls")

# line16, = plt.plot(dates, df.iloc[16].tolist() ,label = "Average Earnings MM")
# line17, = plt.plot(dates, df.iloc[17].tolist() ,label = "Average Earnings YY")
# line18, = plt.plot(dates, df.iloc[18].tolist() ,label = "Average Workweek Hrs")
# line20, = plt.plot(dates, df.iloc[20].tolist() , label = "Fed Rate Lower bound", alpha = 0.7)
# line21, = plt.plot(dates, df.iloc[21].tolist() , label = "Fed Rate Upper bound", alpha = 0.7)

gdp_dates = df_gdp.iloc[26].tolist()
gdp_data = df_gdp.iloc[27].tolist()
# lineGDP, = plt.plot(gdp_dates , gdp_data,  label = "GDP Final")

plt.title('Graph 10 : US Nonfarm payrolls')
plt.xlabel('Year')
leg = plt.legend(loc='upper right')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()