import pandas as pd

df = pd.read_csv('salaries_by_college_major.csv')
#printing out the first 5 rows
data = df.head()
print(data)

#printing out the number of rows
num_of_rows = df.shape
print(num_of_rows)

#printing out the number of columns
num_of_columns = df.columns
print(num_of_columns)

#finding out the cells with empty values
empty_cell = df.isna()
print(empty_cell)

#checkinng out couple of rows
couple_of_rows = df.tail()
print(couple_of_rows)

#deleting the last row
clean_df = df.dropna()
last_row = clean_df.tail()

#individual columns
print(clean_df['Starting Median Salary'].idxmax())

print(clean_df['Undergraduate Major'].loc[43])
print(clean_df['Undergraduate Major'][43])
print(clean_df.loc[43])

#challege
print(clean_df['Mid-Career Median Salary'].max())
print(clean_df['Mid-Career Median Salary'].idxmax())
print(clean_df['Undergraduate Major'][8])

print(clean_df['Starting Median Salary'].min())
print(clean_df['Starting Median Salary'].idxmin())
print(clean_df['Undergraduate Major'].loc[49])

print(clean_df.loc[clean_df['Mid-Career Median Salary'].idxmin()])

spread_col = clean_df['Mid-Career 90th Percentile Salary'].subtract(clean_df['Mid-Career 10th Percentile Salary'])
clean_df.insert(1, 'Spread', spread_col)
clean_df.head()

low_risk = clean_df.sort_values('Spread')
low_risk[['Undergraduate Major', 'Spread']].head()

print(clean_df.groupby('Group').count())
