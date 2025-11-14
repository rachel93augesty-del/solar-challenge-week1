import pandas as pd

# Path to your large CSV
input_file = "data/cleaned/cleaned_solar_data_all_countries.csv"

# Read the CSV
df = pd.read_csv(input_file)

# Split in half
mid = len(df) // 2
part1 = df.iloc[:mid]
part2 = df.iloc[mid:]

# Save smaller CSVs
part1.to_csv("data/cleaned/cleaned_solar_data_part1.csv", index=False)
part2.to_csv("data/cleaned/cleaned_solar_data_part2.csv", index=False)

print("CSV split complete:")
print("Part 1:", part1.shape)
print("Part 2:", part2.shape)
