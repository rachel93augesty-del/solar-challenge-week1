import pandas as pd
import glob
import os

# Path to cleaned CSVs
path = "data/cleaned/"
all_files = glob.glob(os.path.join(path, "*_clean.csv"))

# Read and concatenate all files
df_list = [pd.read_csv(f) for f in all_files]
df_all = pd.concat(df_list, ignore_index=True)

# Ensure datetime is in proper format
df_all['datetime'] = pd.to_datetime(df_all['datetime'])
df_all = df_all.sort_values(by=['country', 'datetime'])

# Export consolidated cleaned dataset
os.makedirs("data/cleaned", exist_ok=True)
df_all.to_csv("data/cleaned/cleaned_solar_data_all_countries.csv", index=False)
print("Consolidated cleaned dataset saved at data/cleaned/cleaned_solar_data_all_countries.csv")
