# compare_dashboard.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.data_processing import load_clean_data, compute_summary_stats

# Streamlit page config
st.set_page_config(page_title="Solar Data Dashboard", layout="wide")

# Sidebar: country selection
country = st.sidebar.selectbox("Select Country", ["Benin", "Sierra Leone", "Togo"])

# Load cleaned data dynamically
df = load_clean_data(country)

# Display summary statistics
st.header(f"Summary Statistics - {country}")
stats = compute_summary_stats(df)
st.dataframe(stats)

# Time Series Plots
st.header(f"Time Series Analysis - {country}")
variables = ['GHI', 'DNI', 'DHI', 'Tamb']
for var in variables:
    st.subheader(f"{var} over Time")
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(pd.to_datetime(df['Timestamp']), df[var])
    ax.set_xlabel("Timestamp")
    ax.set_ylabel(var)
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Cleaning Impact: average ModA & ModB pre/post-clean
st.header(f"Cleaning Impact - {country}")
clean_avg = df.groupby('Cleaning')[['ModA','ModB']].mean().reset_index()
fig, ax = plt.subplots(figsize=(8,4))
clean_avg.plot(x='Cleaning', y=['ModA','ModB'], kind='bar', ax=ax)
ax.set_ylabel("Average Value")
ax.set_title("ModA & ModB Pre/Post Cleaning")
st.pyplot(fig)

# Correlation Heatmap
st.header(f"Correlation Heatmap - {country}")
corr_vars = ['GHI','DNI','DHI','TModA','TModB']
fig, ax = plt.subplots(figsize=(8,6))
sns.heatmap(df[corr_vars].corr(), annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)

# Scatter Plots
st.header(f"Scatter Plots - {country}")
fig, ax = plt.subplots(figsize=(8,6))
ax.scatter(df['WS'], df['GHI'], alpha=0.5)
ax.set_xlabel("Wind Speed (WS)")
ax.set_ylabel("GHI")
ax.set_title("WS vs. GHI")
st.pyplot(fig)

fig, ax = plt.subplots(figsize=(8,6))
ax.scatter(df['RH'], df['Tamb'], alpha=0.5, color='orange')
ax.set_xlabel("Relative Humidity (RH)")
ax.set_ylabel("Temperature (Tamb)")
ax.set_title("RH vs. Tamb")
st.pyplot(fig)

# Bubble Chart: GHI vs Tamb sized by RH
st.header(f"Bubble Chart - {country}")
fig, ax = plt.subplots(figsize=(8,6))
scatter = ax.scatter(df['GHI'], df['Tamb'], s=df['RH'], alpha=0.5, c=df['RH'], cmap='viridis')
ax.set_xlabel("GHI")
ax.set_ylabel("Tamb")
ax.set_title("GHI vs Tamb (Bubble size = RH)")
fig.colorbar(scatter, ax=ax, label='RH')
st.pyplot(fig)

# Country Comparison (for multiple countries)
st.header("Cross-Country Comparison")
df_benin = load_clean_data("Benin")
df_sierra = load_clean_data("Sierra Leone")
df_togo = load_clean_data("Togo")

combined = pd.concat([
    df_benin.assign(Country="Benin"),
    df_sierra.assign(Country="Sierra Leone"),
    df_togo.assign(Country="Togo")
])

# Boxplots of GHI, DNI, DHI by country
metrics = ['GHI','DNI','DHI']
for metric in metrics:
    st.subheader(f"{metric} Comparison")
    fig, ax = plt.subplots(figsize=(8,6))
    sns.boxplot(x='Country', y=metric, data=combined, ax=ax)
    ax.set_title(f"{metric} Distribution by Country")
    st.pyplot(fig)

# Summary Table: mean, median, std
st.subheader("Summary Table - Mean, Median, Std")
summary_table = combined.groupby('Country')[['GHI','DNI','DHI']].agg(['mean','median','std'])
st.dataframe(summary_table)

# Optional: Statistical Testing (ANOVA)
from scipy.stats import f_oneway, kruskal
st.subheader("Statistical Testing (ANOVA & Kruskal-Wallis) on GHI")
f_stat, p_val = f_oneway(df_benin['GHI'], df_sierra['GHI'], df_togo['GHI'])
h_stat, p_kw = kruskal(df_benin['GHI'], df_sierra['GHI'], df_togo['GHI'])
st.write(f"One-way ANOVA: F-statistic = {f_stat:.2f}, p-value = {p_val:.5f}")
st.write(f"Kruskal-Wallis: H-statistic = {h_stat:.2f}, p-value = {p_kw:.5f}")

# Bonus: average GHI bar chart
st.subheader("Average GHI by Country")
avg_ghi = combined.groupby('Country')['GHI'].mean().sort_values(ascending=False)
fig, ax = plt.subplots(figsize=(6,4))
avg_ghi.plot(kind='bar', ax=ax, color='skyblue')
ax.set_ylabel("Average GHI")
ax.set_title("Country Ranking by Average GHI")
st.pyplot(fig)