import pandas as pd
import glob
import os

# Path to cleaned CSVs
path = "data/cleaned/"
all_files = glob.glob(os.path.join(path, "*_clean.csv"))

# Read and concatenate all files
df_list = []
for f in all_files:
    df = pd.read_csv(f)
    country_name = os.path.basename(f).split("_")[0].capitalize()
    df['country'] = country_name  # Add country column
    df_list.append(df)

# Combine all DataFrames
df_all = pd.concat(df_list, ignore_index=True)

# Fix for column name 'Timestamp'
if 'Timestamp' in df_all.columns:
    df_all['Timestamp'] = pd.to_datetime(df_all['Timestamp'])
else:
    print("⚠️ 'Timestamp' column not found!")

# Sort
df_all = df_all.sort_values(by=['country', 'Timestamp'])

# Export consolidated dataset
os.makedirs("data/cleaned", exist_ok=True)
df_all.to_csv("data/cleaned/cleaned_solar_data_all_countries.csv", index=False)
print("✅ Consolidated cleaned dataset saved at data/cleaned/cleaned_solar_data_all_countries.csv")
