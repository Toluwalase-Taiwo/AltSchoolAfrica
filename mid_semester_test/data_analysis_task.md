## Mid-Semester Break Assignment
#### AltSchool of Data Science Tinyuka 2024 First Semester Python Programming Language IV Mid-Semester Break Assignment In Progress 

- Load the energy data from the file Energy Indicators.xls, a list of indicators of energy supply and renewable electricity production from the United Nations for the year 2013. It should be put into a data frame with the variable name “Energy.”

- Remember that this is an Excel file and not a comma-separated values file. Also, exclude the footer and header information from the data file. The first two columns are unnecessary, so you should get rid of them, and you should change the column labels so that the columns are:

[‘Country’, ‘Energy Supply’, ‘Energy Supply per Capita’, ‘% Ren`ewable]

- Convert Energy Supply to gigajoules (Note: are 1,000,000 gigajoules in a petajoule). For all countries with missing data (e.g., data with “…”), ensure this is reflected as np.NaN values.

- Rename the following list of countries (for use in later questions):

“United States of America”: “United States”,

“United Kingdom of Great Britain and Northern Ireland”: “United Kingdom”,

“China, Hong Kong Special Administrative Region”: “Hong Kong”“`

- Several countries also have numbers and/or parenthesis in their name. Be sure to remove these, e.g., ’Bolivia (Plurinational State of)’ should be ’Bolivia’. ’Switzerland17’ should be ’Switzerland’.

- Next, load the GDP data from the file world_bank.csv, which is a CSV containing countries’ GDP from 1960 to 2015 from World Bank. Call this DataFrame GDP.

- Make sure to skip the header and rename the following list of countries:

“`”Korea, Rep.”: “South Korea”,

“Iran, Islamic Rep.”: “Iran”,

“Hong Kong SAR, China”: “Hong Kong”“`

- Finally, load the Sciamgo Journal and Country Rank data for Energy Engineering and Power Technology from the file scimagojr-3.xlsx, which ranks countries based on their journal contributions in the area above. Call this DataFrame ScimEn.

- Join the three datasets, GDP, Energy, and ScimEn, into a new dataset (using the intersection of country names). Use only the GDP data from the last 10 years (2006-2015) and the top 15 countries by Scimagojr ‘Rank’ (Rank 1 through 15).

- The index of this DataFrame should be the name of the country, and the columns should be [‘Rank’, ‘Documents’, ‘Citable documents’, ‘Citations’, ‘Self-citations’,

   ‘Citations per document’, ‘H index’, ‘Energy Supply’,

   ‘Energy Supply per Capita’, ‘% Renewable’, ‘2006’, ‘2007’, ‘2008’,

   ‘2009’, ‘2010’, ‘2011’, ‘2012’, ‘2013’, ‘2014’, ‘2015’].
- This function should return a DataFrame with 20 columns and 15 entries, and the rows of the DataFrame should be sorted by “Rank”.

### Submission Instructions:

- Submit as a Jupyter Notebook Your Jupyter notebook should be your name It should be submitted a day before resumption. Focus Areas:

- Proper documentation: Use PEP8 Guidelines, Notebook Mackdown, etc. Explain the intuition of your code when and where necessary.
