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

df = pd.read_excel('Economic Data.xlsx', sheet_name='ez', header=None, skiprows= 4, usecols="G:SV")
df_gdp = pd.read_excel('Economic Data.xlsx', sheet_name='ez', header=None, skiprows= 4, usecols="F:DM")

# iloc for moving to specific row of data
# iloc[0] for dates
# iloc[1] for Retail sales

dates = df.iloc[0].tolist() 
data = df.iloc[1].tolist()

# UnComment the lines you want to plot, simple it is, and then run python code.
line1, = plt.plot(dates, newdata, label = "Consumer Confid Flash")

# line2, = plt.plot(dates, df.iloc[2].tolist(), label = "Markit Comp PMI")

# line3, = plt.plot(dates, df.iloc[3].tolist() , label = "Markit Mfg PMI")

# line4, = plt.plot(dates, df.iloc[4].tolist() ,label = "Markit Serv PMI")
# line5, = plt.plot(dates, df.iloc[5].tolist() ,label = "HICP ex F,E,A&T Final YY")

# line6, = plt.plot(dates, df.iloc[6].tolist() ,label = "HICP Final YY")
# line7, = plt.plot(dates, df.iloc[7].tolist() ,label = "Retail Sales MM")

# line8, = plt.plot(dates, df.iloc[8].tolist() ,label = "Unemployment Rate")

# line11, = plt.plot(dates, df.iloc[9].tolist()  , label = "EZ Deposit Rate")
# line12, = plt.plot(dates, df.iloc[10].tolist() ,label = "Zew Survey")
# line13, = plt.plot(dates, df.iloc[11].tolist() , label = "IFO Buz Climate")


gdp_dates = df_gdp.iloc[13].tolist()
gdp_qq_data = df_gdp.iloc[14].tolist()
gdp_yy_data = df_gdp.iloc[15].tolist()

# lineGDP_qq, = plt.plot(gdp_dates , gdp_qq_data,  label = "GDP Flash Estimate QQ")
# lineGDP_yy, = plt.plot(gdp_dates , gdp_yy_data,  label = "GDP Flash Estimate YY")

plt.title('Graph 10 : US Non-farm payrolls')
plt.xlabel('Year')
leg = plt.legend(loc='upper center')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()