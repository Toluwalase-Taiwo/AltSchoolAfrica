# Importing necessary libraries
import pandas as pd
import numpy as np

# Loading the Energy data into a dataframe
# exclude the header and footer information from the data
# use relevant columns and discard irrelevant columns
# change the column labels as specified
# change missing data "..." to NaN values

Energy = pd.read_excel('Energy Indicators.xls', 
                       header = 16, 
                       usecols = [2,3,4,5], 
                       skipfooter = 38,
                       names = ['Country', 'Energy Supply', 'Energy Supply per Capita', '%Renewable'],
                       skiprows = 1,
                       na_values = '...')
Energy.head()

#converting Energy Supply from pentajoules to gigajoules 
Energy['Energy Supply']= Energy['Energy Supply'] * 1_000_000
Energy.head()

#removing numbers from strings in the Country column and
#replace with an empty string using regex
#\d means any digit
#+ means one or more digits
Energy['Country'] = Energy['Country'].str.replace(r'\d+','',regex = True)

#replace parenthesis and special characters with an empty string
#\W for White spaces
Energy['Country'] = Energy['Country'].str.replace(r'\W+\(.*\)','',regex = True)
print(Energy['Country'].unique())

#Replace countries with specified labels

Energy['Country'] = Energy['Country'].replace({'United States of America':'United States',
                                               'United Kingdom of Great Britain and Northern Ireland':'United Kingdom',
                                               'China, Hong Kong Special Administrative Region':'Hong Kong'})
Energy['Country'].unique()

#Loading the GDP data
#exclude the header
GDP = pd.read_csv('world_bank.csv',header = 4)
GDP.head().T

#Rename some countries to the specified name
GDP['Country Name'] = GDP['Country Name'].replace({'Korea, Rep.':'South Korea',
                                                   'Iran, Islamic Rep.':'Iran',
                                                   'Hong Kong SAR, China':'Hong Kong'})
GDP.head()

#checking for all unique entries in the Country Name column
GDP['Country Name'].unique()

#load the Sciamgo Journal and Country Rank data for Energy Engineering and Power Technology
ScimEn = pd.read_excel('scimagojr-3.xlsx')
ScimEn.head()

#Use the top 15 countries by Scimagojr ‘Rank’ (Rank 1 through 15).

ScimEn = ScimEn[['Rank', 'Country','Documents',
                 'Citable documents','Citations',
                 'Self-citations','Citations per document',
                 'H index']].head(15)
ScimEn

#set index to Country
ScimEn.set_index('Country', inplace = True)
ScimEn

#Use only the GDP data from the last 10 years (2006-2015)
#create a df containing only the specified columns
GDP = GDP[['Country Name','2006',
           '2007', '2008', '2009',
           '2010', '2011', '2012', 
           '2013','2014', '2015']]
GDP.head()

#rename the column Country Name to Country
#allows for common column when merging with other dfs
GDP = GDP.rename(columns = {'Country Name':'Country'})

# First merge ScimEn with Energy df, then merge the result with GDP
merged_df = ScimEn.merge(Energy, on='Country').merge(GDP, on = 'Country')
merged_df

#set the index of the merged df to Country
merged_df.set_index('Country', inplace = True)
merged_df
