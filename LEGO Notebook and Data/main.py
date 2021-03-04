import pandas as pd
import matplotlib.pyplot as plt

colors = pd.read_csv('data/colors.csv')

colors.head()
colors['name'].nunique()
colors.groupby('is_trans').count()

sets = pd.read_csv('data/sets.csv')
sets.head()
sets.tail()
sets.sort_values('year').head()
sets[sets['year'] == 1949]

sets.sort_values('num_parts', ascending=False).head()
sets_by_year = sets.groupby('year').count()
sets_by_year['set_num'].head()
sets_by_year['set_num'].tail()

