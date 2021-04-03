#google play store

import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio

pio.renderers.default = 'png'

df_apps = pd.read_csv('apps.csv')

#How many rows and columns does df_apps have
#rows
num_of_rows = df_apps.shape
print(num_of_rows)
#colums
num_of_columns = df_apps.columns
print(num_of_columns)

#Remove the columns called Last_Updated and Android_Version
# from the DataFrame.
# We will not use these columns
clean_df = df_apps.drop(['Last_Updated','Android_Ver'], axis=1, inplace=True)
print(clean_df)

# What are the column names?
# What does the data look like?
# Look at a random sample of 5 different rows with
google_data = df_apps.head()
print(google_data)

#How many rows have a NaN value (not-a-number) in the Rating column?
nan_row = df_apps[df_apps.Rating.isna()]
nan_row.head()
print(nan_row)

# Create DataFrame called df_apps_clean that does not include these rows
df_apps_clean = df_apps.dropna()
df_apps_clean.shape
print(df_apps_clean)

#Are there any duplicates in data? Check for duplicates using the .duplicated() function.
# How many entries can you find for the "Instagram" app?
duplicated_rows = df_apps_clean[df_apps_clean.duplicated()]
df_apps_clean[df_apps_clean.App == 'Instagram']
print(duplicated_rows.shape)
duplicated_rows.head()

# Use .drop_duplicates() to remove any duplicates from df_apps_clean
dropped = df_apps_clean.drop_duplicates()
dropped = df_apps_clean.drop_duplicates(subset=['App', 'Type', 'Price'])
df_apps_clean[df_apps_clean.App == 'Instagram']
print(dropped)

# Identify which apps are the highest rated.
highest_rating = df_apps_clean.sort_values('Rating', ascending=False).head()
print(highest_rating)

# What problem might you encounter if you rely exclusively on ratings alone to determine the quality of an app?
highest_rating1 = df_apps_clean.sort_values('Size_MBs', ascending=False).head()
print(highest_rating1)
highest_rating2 = df_apps_clean.sort_values('Reviews', ascending=False).head(50)
print(highest_rating2)

ratings = df_apps_clean.Content_Rating.value_counts()
print(ratings)

fig = go.pie(labels=ratings.index,
             values=ratings.values,
             title="Content Rating",
             names=ratings.index,
             hole=0.6,
             )
fig.update_traces(textposition='inside', textfont_size=15, textinfo='percent')
fig.show()

# How many apps had over 1 billion (that's right - BILLION) installations?
# How many apps just had a single install?
#steps

#Check the datatype of the Installs column.
df_apps_clean.Installs.describe()
#or
df_apps_clean.info()

#Count the number of apps at each level of installations.
df_apps_clean.Installs = df_apps_clean.Installs.astype(str).str.replace(',', "")
df_apps_clean.Installs = pd.to_numeric(df_apps_clean.Installs)
df_apps_clean[['App', 'Installs']].groupby('Installs').count()

#Convert the number of installations (the Installs column) to a numeric data type. Hint: this is a
#2-step process. You'll have to make sure you remove non-numeric characters first.

#Convert the price column to numeric data.
#Then investigate the top 20 most expensive apps in the dataset
df_apps_clean.Price.describe()
df_apps_clean.Price = df_apps_clean.Price.astype(str).str.replace('$', "")
df_apps_clean.Price = pd.to_numeric(df_apps_clean.Price)
df_apps_clean.sort_values('Price', ascending=False).head(20)

#working out the highest grossing paid apps now
df_apps_clean['Revenue_Estimate'] = df_apps_clean.Installs.mul(df_apps_clean.Price)
df_apps_clean.sort_values('Revenue_Estimate', ascending=False)[:10]


df_apps_clean.Category.nunique()
top10_category = df_apps_clean.Category.value_counts()[:10]

bar = go.bar(
    x = top10_category.index,
    y = top10_category.values
)

bar.show()

category_installs = df_apps_clean.groupby('Category').agg({'Installs': pd.Series.sum})
category_installs.sort_values('Installs', ascending=True, inplace=True)

h_bar = go.bar(x=category_installs.Installs,
               y=category_installs.index,
               orientation='h',
               title='Category Popularity')
h_bar.update_layout(xaxis_title='Number of Downloads', yaxis_title='Category')
h_bar.show()

#let’s use plotly to create a scatter plot

cat_number = df_apps_clean.groupby('Category').agg({'App': pd.Series.count})
cat_merged_df = pd.merge(cat_number, category_installs, on='Category', how="inner")
print(f'The dimensions of the DataFrame are: {cat_merged_df.shape}')
cat_merged_df.sort_values('Installs', ascending=False)

scatter = go.scatter(cat_merged_df,  # data
                     x='App',  # column name
                     y='Installs',
                     title='Category Concentration',
                     size='App',
                     hover_name=cat_merged_df.index,
                     color='Installs')

scatter.update_layout(xaxis_title="Number of Apps (Lower=More Concentrated)",
                      yaxis_title="Installs",
                      yaxis=dict(type='log'))

scatter.show()

#How many different types of genres are there?
#Can an app belong to more than one genre?
stack = df_apps_clean.Genres.str.split(';', expand=True).stack()
print(f'We now have a single column with shape: {stack.shape}')
num_genres = stack.value_counts()
print(f'Number of genres: {len(num_genres)}')

#Can you create this chart with the Series containing the genre data?
bar = go.bar(x=num_genres.index[:15],  # index = category name
             y=num_genres.values[:15],  # count
             title='Top Genres',
             hover_name=num_genres.index[:15],
             color=num_genres.values[:15],
             color_continuous_scale='Agsunset')

bar.update_layout(xaxis_title='Genre',
                  yaxis_title='Number of Apps',
                  coloraxis_showscale=False)

bar.show()

#Grouped Bar Charts and Box Plots with Plotly
df_apps_clean.Type.value_counts()
df_free_vs_paid = df_apps_clean.groupby(["Category", "Type"], as_index=False).agg({'App': pd.Series.count})
df_free_vs_paid.head()

#Use the plotly express bar chart examples and the .bar() API reference to create this bar chart:
g_bar = go.bar(df_free_vs_paid,
               x='Category',
               y='App',
               title='Free vs Paid Apps by Category',
               color='Type',
               barmode='group')

g_bar.update_layout(xaxis_title='Category',
                    yaxis_title='Number of Apps',
                    xaxis={'categoryorder': 'total descending'},
                    yaxis=dict(type='log'))

g_bar.show()

#Create a box plot that shows the number of Installs for free versus paid apps.
# How does the median number of installations compare? Is the difference large or small?
box = go.box(df_apps_clean,
             y='Installs',
             x='Type',
             color='Type',
             notched=True,
             points='all',
             title='How Many Downloads are Paid Apps Giving Up?')

box.update_layout(yaxis=dict(type='log'))

box.show()
#Looking at the hover text, how much does the median app earn in the Tools category?
# If developing an Android app costs $30,000 or thereabouts, does the average photography app recoup its development costs?
df_paid_apps = df_apps_clean[df_apps_clean['Type'] == 'Paid']
box = go.box(df_paid_apps,
             x='Category',
             y='Revenue_Estimate',
             title='How Much Can Paid Apps Earn?')

box.update_layout(xaxis_title='Category',
                  yaxis_title='Paid App Ballpark Revenue',
                  xaxis={'categoryorder': 'min ascending'},
                  yaxis=dict(type='log'))

box.show()

#What is the median price for a paid app? Then compare pricing by category by creating another box plot.
# But this time examine the prices (instead of the revenue estimates) of the paid apps.
# I recommend using {categoryorder':'max descending'} to sort the categories.

df_paid_apps.Price.median()
box = go.box(df_paid_apps,
             x='Category',
             y="Price",
             title='Price per Category')

box.update_layout(xaxis_title='Category',
                  yaxis_title='Paid App Price',
                  xaxis={'categoryorder': 'max descending'},
                  yaxis=dict(type='log'))

box.show()