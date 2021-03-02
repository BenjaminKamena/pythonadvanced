import pandas as pd

colors = pd.read_csv('data/colors.csv')

colors.head()
colors['name'].nunique()
colors.groupby('is_trans').count()
