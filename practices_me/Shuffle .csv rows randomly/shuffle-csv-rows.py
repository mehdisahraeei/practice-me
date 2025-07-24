import pandas as pd

# Read data from the CSV file
df = pd.read_csv('info.csv')

# Shuffle all rows randomly (different order each run)
df_shuffled = df.sample(frac=1).reset_index(drop=True)

# Save the shuffled data to a new CSV file
df_shuffled.to_csv('shuffled_output.csv', index=False)



print(df_shuffled)
