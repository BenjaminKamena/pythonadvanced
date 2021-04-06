import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd_reveue = pd.read_csv('cost_revenue_dirty.csv')
#How many rows and columns does the dataset contain?
#rows
num_of_rows = pd_reveue.shape
print(num_of_rows)

#columns
num_of_columns = pd_reveue.columns
print(num_of_columns)

# Are there any NaN values present?
nan_value = pd_reveue.isna().values.any()
print(nan_value)

# Are there any duplicate rows?
duplicate_rows = pd_reveue.duplicated().values.any()
print(duplicate_rows)

# What are the data types of the columns?
print(pd_reveue.dtypes)

#Convert the USD_Production_Budget,
# USD_Worldwide_Gross, and
# USD_Domestic_Gross columns to a numeric format by removing $ signs and ,
pd_reveue.info()

chars_to_remove = [',', '$']
columns_to_clean = [
    'USD_Production_Budget',
    'USD_Worldwide_Gross',
    'USD_Domestic_Gross'
]
for col in columns_to_clean:
    for char in chars_to_remove:
        pd_reveue[col] = pd_reveue[col].astype(str).str.replace(char, "")
    pd_reveue[col] = pd.to_numeric(pd_reveue[col])

#To convert the Release_Date column to a DateTime object
pd_reveue.Release_Date = pd.to_datetime(pd_reveue.Release_Date)
pd_reveue.head()
pd_reveue.info()

#What is the average production budget of the films in the data set?
print(pd_reveue.describe())
# What is the average worldwide gross revenue of films?
# What were the minimums for worldwide and domestic revenue?
# Are the bottom 25% of films actually profitable or do they lose money?
# What are the highest production budget and highest worldwide gross revenue of any film?
# How much revenue did the lowest and highest budget films make?

print(pd_reveue[pd_reveue.USD_Production_Budget == 1100.00])
print(pd_reveue[pd_reveue.USD_Production_Budget == 425000000.00])

#How many films grossed $0 domestically (i.e., in the United States)?
# What were the highest budget films that grossed nothing?
zero_demostic = pd_reveue[pd_reveue.USD_Domestic_Gross == 0]
print(f'Number of films that grossed $0 domestically {len(zero_demostic)}')
zero_demostic.sort_values('USD_Production_Budget', ascending=False)

#How many films grossed $0 worldwide?
# What are the highest budget films that had no revenue internationally (i.e., the biggest flops)?
zero_worldwide = pd_reveue[pd_reveue.USD_Worldwide_Gross == 0]
print(f'Number of films that grossed $0 domestically {len(zero_worldwide)}')
zero_worldwide.sort_values('USD_Production_Budget', ascending=False)

international_releases = pd_reveue.loc[(pd_reveue.USD_Domestic_Gross == 0) &
                                       (pd_reveue.USD_Worldwide_Gross != 0)]
print(international_releases)

international_releases = pd_reveue.query('USD_Domestic_Gross == 0 and USD_Worldwide_Gross != 0')
print(f'Number of international releases: {len(international_releases)}')
international_releases.tail()

#Identify which films were not released yet as of the time of data collection (May 1st, 2018).
# How many films are included in the dataset that have not yet had a chance to be screened in the box office?
# Create another DataFrame called data_clean that does not include these films.
scrape_date = pd.Timestamp('2018-5-1')
future_releases = pd_reveue[pd_reveue.Release_Date >= scrape_date]
print(f'Number of unreleased movies: {len(future_releases)}')
data_clean = pd_reveue.drop(future_releases.index)

money_losing = data_clean.loc[data_clean.USD_Production_Budget > data_clean.USD_Worldwide_Gross]
len(money_losing)/len(data_clean)
#or the .query() function

money_losing = data_clean.query('USD_Production_Budget > USD_Worldwide_Gross')
money_losing.shape[0]/data_clean.shape[0]

plt.figure(figsize=(8, 4), dpi=200)
with sns.axes_style('darkgrid'):
    ax = sns.scatterplot(data = data_clean,
                x='Release_Date',
                y = 'USD_Production_Budget',
                hue='USD_Worldwide_Gross',
                size='USD_Worldwide_Gross')
    ax.set(ylim=(0, 3000000000),
           xlim=(data_clean.Release_Date.min(), data_clean.Release_Date.max()),
           xlabel='Year',
           ylabel='Budget in $100 millions')
plt.show()