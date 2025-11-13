import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- Load Data ---
DATA_PATH = "data/cleaned/cleaned_solar_data_all_countries.csv"
df = pd.read_csv(DATA_PATH, parse_dates=['Timestamp'])

print("✅ Data loaded successfully!")
print(df.head())

# --- Create output folder for visuals ---
os.makedirs("outputs/visuals", exist_ok=True)

# --- Plot 1: Global Horizontal Irradiance (GHI) Over Time by Country ---
plt.figure(figsize=(12, 6))
for country in df['country'].unique():
    subset = df[df['country'] == country]
    plt.plot(subset['Timestamp'], subset['GHI'], label=country)
plt.title("Global Horizontal Irradiance (GHI) Over Time")
plt.xlabel("Timestamp")
plt.ylabel("GHI")
plt.legend()
plt.tight_layout()
plt.savefig("outputs/visuals/ghi_over_time.png")
plt.close()

# --- Plot 2: Direct Normal Irradiance (DNI) Over Time by Country ---
plt.figure(figsize=(12, 6))
for country in df['country'].unique():
    subset = df[df['country'] == country]
    plt.plot(subset['Timestamp'], subset['DNI'], label=country)
plt.title("Direct Normal Irradiance (DNI) Over Time")
plt.xlabel("Timestamp")
plt.ylabel("DNI")
plt.legend()
plt.tight_layout()
plt.savefig("outputs/visuals/dni_over_time.png")
plt.close()

# --- Plot 3: Diffuse Horizontal Irradiance (DHI) Over Time by Country ---
plt.figure(figsize=(12, 6))
for country in df['country'].unique():
    subset = df[df['country'] == country]
    plt.plot(subset['Timestamp'], subset['DHI'], label=country)
plt.title("Diffuse Horizontal Irradiance (DHI) Over Time")
plt.xlabel("Timestamp")
plt.ylabel("DHI")
plt.legend()
plt.tight_layout()
plt.savefig("outputs/visuals/dhi_over_time.png")
plt.close()

# --- Plot 4: Correlation Heatmap ---
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
corr = df[numeric_cols].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=False, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap of Solar Parameters")
plt.tight_layout()
plt.savefig("outputs/visuals/correlation_heatmap.png")
plt.close()

print("✅ All visuals saved in 'outputs/visuals/' folder!")
