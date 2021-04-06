import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df_tesla = pd.read_csv('TESLA Search Trend vs Price.csv')

print(df_tesla.shape)

print(df_tesla.head())

print(df_tesla.describe())

print(f'Largest value for Tesla in Web Search: {df_tesla.TSLA_WEB_SEARCH.max()}')
print(f'Smallest value for Tesla in Web Search: {df_tesla.TSLA_WEB_SEARCH.min()}')

df_unemployment = pd.read_csv('UE Benefits Search vs UE Rate 2004-19.csv')
print(df_unemployment.shape)
print(df_unemployment.head())
print('Largest value for "Unemployment Benefits" ' f'in Web Search: {df_unemployment.UE_BENEFITS_WEB_SEARCH.max()}')

df_btc_price = pd.read_csv('Daily Bitcoin Price.csv')
print(df_btc_price.shape)
print(df_btc_price.head())


df_btc_search = pd.read_csv('Bitcoin Search Trend.csv')
print(df_btc_search.shape)
print(df_btc_search.head)

print(f'largest BTC News Search {df_btc_search.BTC_NEWS_SEARCH.max()}')


print(f'Missing values for Tesla?: {df_tesla.isna().values.any()}')
print(f'Missing values for U/E?: {df_unemployment.isna().values.any()}')
print(f'Missing values for BTC Search?: {df_btc_search.isna().values.any()}')
print(f'Missing values? for BTC price?: {df_btc_price.isna().values.any()}')
print(f'Number of missing values: {df_btc_price.isna().values.sum()}')
df_btc_price[df_btc_price.CLOSE.isna()]
df_btc_price = df_btc_price.dropna(inplace=True)

df_tesla.MONTH = pd.to_datetime(df_tesla.MONTH)
df_btc_search.MONTH = pd.to_datetime(df_btc_search.MONTH)
df_unemployment.MONTH = pd.to_datetime(df_unemployment.MONTH)
#df_btc_price.DATE = pd.to_datetime(df_btc_price.DATE)

#df_btc_monthly = df_btc_price.resample('M', on='DATE').last()
#df_btc_monthly = df_btc_price.resample('M', on='DATE').mean()

plt.figure(figsize=(14, 8), dpi=120)
plt.title('Tesla Web Search vs Price', fontsize=18)
plt.title('Bitcoin News Search vs Resampled Price', fontsize=18)

# Increase the size and rotate the labels on the x-axis
plt.xticks(fontsize=14, rotation=45)

ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.set_ylabel('BTC Price', color='#F08F2E', fontsize=14)
ax1.set_ylabel('TSLA Stock Price', color='#E6232E', fontsize=14)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)

# Set the minimum and maximum values on the axes
ax1.set_ylim([0, 600])
ax1.set_xlim([df_tesla.MONTH.min(), df_tesla.MONTH.max()])

ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, color='#E6232E', linewidth=3)
ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH, color='skyblue', linewidth=3)

years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter('%Y')

plt.show()