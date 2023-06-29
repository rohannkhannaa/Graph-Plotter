# Code written by :
#       Rohan Khanna
#       2020csb1117@iitrpr.ac.in
#       Futures First Assignment 1 

# Importing lobraries
import pandas as pd
import matplotlib.pyplot as plt

# Read excel sheet name : Economic Data.xlsx, sheet_name set to UK
# Data is from coloum E to SU
# Code is changed here itself to plot specific data.
# To test graph, make sure EconomicData.xlsx file is in same directory of python code

df = pd.read_excel('Economic Data.xlsx', sheet_name='uk', header=None, skiprows=3, usecols="E:SU")
df_gdp = pd.read_excel('Economic Data.xlsx', sheet_name='uk', header=None, skiprows=3, usecols="F:FS")

# iloc for moving to specific row of data
# iloc[0] for dates
# iloc[1] for Retail sales

dates = df.iloc[0].tolist() 

# UnComment the lines you want to plot, simple it is, and then run python code.

line2, = plt.plot(dates, df.iloc[2].tolist(), label = "Avg Wk Earnings 3M YY")
line1, = plt.plot(dates, df.iloc[1].tolist(), label = "Avg Earnings (Ex-Bonus)")

line3, = plt.plot(dates, df.iloc[3].tolist() , label = "ILO Unemployment Rate")

line4, = plt.plot(dates, df.iloc[4].tolist() ,label = "Core CPI MM")
line5, = plt.plot(dates, df.iloc[5].tolist() ,label = "Core CPI YY")

line6, = plt.plot(dates, df.iloc[6].tolist() ,label = "CPI MM")
line7, = plt.plot(dates, df.iloc[7].tolist() ,label = "CPI YY")

line8, = plt.plot(dates, df.iloc[8].tolist() ,label = "GfK Consumer Confidence")

line11, = plt.plot(dates, df.iloc[9].tolist()  , label = "Markit/CIPS Cons PMI")
line12, = plt.plot(dates, df.iloc[10].tolist() ,label = "Markit/CIPS Mfg PMI")
line13, = plt.plot(dates, df.iloc[11].tolist() , label = "Markit/CIPS Serv PMI")

line14, = plt.plot(dates, df.iloc[12].tolist() ,label = "BRC Retail Sales YY")
line10, = plt.plot(dates, df.iloc[13].tolist() ,  label = "Retail Sales Ex-Fuel MM")
line14, = plt.plot(dates, df.iloc[14].tolist() ,label = "Retail Sales MM")

line15, = plt.plot(dates, df.iloc[15].tolist() ,label = "UK Bank Rate")

line19, = plt.plot(dates, df.iloc[16].tolist() ,label = "UK GDP Monthly")


gdp_dates = df_gdp.iloc[19].tolist()
gdp_qq_data = df_gdp.iloc[20].tolist()
gdp_yy_data = df_gdp.iloc[21].tolist()

lineGDP_qq, = plt.plot(gdp_dates , gdp_qq_data,  label = "GDP QQ")
lineGDP_yy, = plt.plot(gdp_dates , gdp_yy_data,  label = "GDP YY")

plt.title('Graph 22 : UK GDP')
plt.xlabel('Year')
# leg = plt.legend(loc='upper center')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()