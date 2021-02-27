import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Programming_Languages.csv", names=["DATE", "TAG", "POSTS"], header=0)

data = df.head()
data1 = df.tail()

num_of_rows = df.shape

entry_columns = df.count()

num_of_posts = df.groupby('TAG').sum()

num_of_posts_mothly = df.groupby('TAG').count()

df.DATE = pd.to_datetime(df.DATE)
fixed_date = df.head()

reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
num_rows = reshaped_df.shape

num_columns = reshaped_df.columns

all_entries = reshaped_df.head()

all_counts = reshaped_df.count()

all_empty = reshaped_df.fillna(0, inplace=True)
all_empty = reshaped_df.isna().values.any()
#all_empty = reshaped_df.head()

plt.figure(figsize=(16, 10))  # make chart larger
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)

plt.plot(reshaped_df.index, reshaped_df.java)
plt.plot(reshaped_df.index, reshaped_df.python)