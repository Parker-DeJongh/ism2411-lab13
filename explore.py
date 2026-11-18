# Self-Assessment
#1.) A boolean filter works to filter data based off of a condition. 
# It will keep the rows that meet the condition and will remove the 
# rows that do not meet that condition.
#2.) df["revenue"] returns a single column of data known as a Series. 
# df[["revenue"]] returns a DataFrame with keeps the data in a table 
# format. This matters when you are working with multiple data 
# columns or functions that may require a DataFrame as input.
#3.) I would choose and use pandas due to how fast it works. You can 
# quickly filter, organize, and calculate information without having 
# to do everything manually like in Excel.



print("--- Exercise 1 ---")

import pandas as pd
df = pd.read_csv('data/retail_sales.csv')

print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)

print("--- Exercise 2 ---")

south = df[df['region'] == 'South']

print(len(south))
print(south.head())

print("--- Exercise 3 ---")

top_revenue = df.sort_values('revenue', ascending=False).head(5)

print(top_revenue)

print("--- Exercise 4 ---")

big_south = df[(df['region'] == 'South') & (df['revenue'] > 1000)]

print(len(big_south))
print(big_south.head())

print("--- Exercise 5 ---")

df['per_unit'] = df['revenue'] / df['quantity']

print(df.head())
print(df['per_unit'].mean())

print("--- Exercise 6 ---")

print(df['region'].unique())
print(df['region'].value_counts())

print("--- Exercise 7 ---")

select_columns= df[['region', 'product', 'revenue']]

print(select_columns.shape)

print("--- Exercise 8 ---")

df.to_csv('data/explored.csv', index=False)
