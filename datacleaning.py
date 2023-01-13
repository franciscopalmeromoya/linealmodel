# Import packages
import pandas as pd

# Read file
df = pd.read_csv('data.txt', sep = ' ')
df.head()

# Change column type to str
df['Temperature'] = df['Temperature'].apply(lambda x: str(x) + 'ºC')

# Save the df in a csv file
df.to_csv('datacat.csv', index = False)