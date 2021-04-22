import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df_yearly = pd.read_csv('annual_deaths_by_clinic.csv')
print(df_yearly.head())
print(df_yearly.shape)
print(df_yearly.describe())
print(df_yearly.isna().values.any())
print(df_yearly.info())
print(df_yearly.duplicated())
print(df_yearly.mean(axis=0))
print(df_yearly.mean(axis=1))

df_monthly = pd.read_csv('monthly_deaths.csv')
print(df_monthly.head())
print(df_monthly.shape)
print(df_monthly.describe())
print(df_monthly.isna().values.any())
print(df_monthly.info())
print(df_monthly.duplicated())
print(df_monthly.mean(axis=0))
print(df_monthly.mean(axis=1))

prob = df_yearly.deaths.sum()/ df_yearly.births.sum() * 100
print(f'Chances of dying in the 1840s in Vienna: {prob:.3}%')

plt.figure(figsize=(14, 8), dpi=200)
plt.title('Total Number of Monthly Births and Deaths', fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(fontsize=14, rotation=45)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel('Births', color='skyblue', fontsize=18)
ax2.set_ylabel('Deaths', color='crimson', fontsize=18)

years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter('%Y')

ax1.set_xlim([df_monthly.date.min(), df_monthly.date.max()])
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)

ax1.grid(color='grey', linestyle='--')

ax1.plot(df_monthly.date,
         df_monthly.births,
         color='skyblue',
         linewidth=3)

ax2.plot(df_monthly.date,
         df_monthly.deaths,
         color='crimson',
         linewidth=2,
         linestyle='--')
line = plt.plot(
    df_yearly,
    x='year',
    y='births',
    color='clinic',
    title='Total Yearly Births by Clinic'
)
line = plt.plot(
    df_yearly,
    x='year',
    y='deaths',
    color='clinic',
    title='Total Yearly Births by Clinic'
)

line.show()
plt.show()