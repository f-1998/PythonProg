import pandas as pd

df = pd.read_csv('squirell_data.csv')

desired_column = df['Primary Fur Color']
value_counts = desired_column.value_counts()

xy = pd.DataFrame(value_counts)
xy.to_csv()