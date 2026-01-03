from src.data_processing.clean_data import clean_data
import pandas as pd

# Example raw data
data = {'A': [1, None, 3], 'B': [None, 5, 6]}
df = pd.DataFrame(data)

print("Raw Data:")
print(df)

# Clean data using your function
df_clean = clean_data(df)

print("\nCleaned Data:")
print(df_clean)
    