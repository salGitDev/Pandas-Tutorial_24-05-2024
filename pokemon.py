import pandas as pd
df = pd.read_csv('pokemon_data.csv')
headData = df.head(3)
tailData = df.tail(3)
df_xlsx = pd.read_excel('pokemon_data.xlsx')
df_txt = pd.read_csv('pokemon_data.txt', delimiter = "\t")
three_cols = df_txt[['Name', 'Type 1', 'HP']]
row_loc1 = df_txt.iloc[1]
first_4rows = df_txt.iloc[0:4]
print(first_4rows)


