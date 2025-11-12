import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="Solar Data Explorer",
    page_icon="☀️",
    layout="wide"
)

# -----------------------------
# Sidebar - Options
# -----------------------------

# Map countries to actual CSV files
country_files = {
    "Benin": "app/data/benin_clean.csv",
    "Togo": "app/data/togo_clean.csv",
    "Sierra Leone": "app/data/sierraleone_clean.csv"
}
selected_country = st.sidebar.selectbox("Select Country", list(country_files.keys()))

metric_options = ["GHI", "DNI", "Temperature", "Wind Speed"]
selected_metric = st.sidebar.selectbox("Select Metric", metric_options)

uploaded_file = st.sidebar.file_uploader("Upload CSV file (optional)", type="csv")

# -----------------------------
# Load CSV
# -----------------------------
try:
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.success(f"Uploaded CSV: {uploaded_file.name} ({uploaded_file.size/1e6:.2f} MB)")  # <- single line
    else:
        df = pd.read_csv(country_files[selected_country])
        st.success(f"Loaded default CSV for {selected_country}")  # <- single line
except Exception as e:
    st.error(f"Could not load CSV: {e}")
    st.stop()

# -----------------------------
# Convert Date column if exists
# -----------------------------
if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# -----------------------------
# Dataset Preview
# -----------------------------
st.subheader(f"Dataset Preview ({selected_country})")
st.dataframe(df.head())

# -----------------------------
# Metric Summary
# -----------------------------
if selected_metric in df.columns:
    st.subheader(f"{selected_metric} Summary")
    mean_val = df[selected_metric].mean()
    median_val = df[selected_metric].median()
    min_val = df[selected_metric].min()
    max_val = df[selected_metric].max()

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Mean", f"{mean_val:.2f}")
    col2.metric("Median", f"{median_val:.2f}")
    col3.metric("Min", f"{min_val:.2f}")
    col4.metric("Max", f"{max_val:.2f}")

# -----------------------------
# Metric Distribution
# -----------------------------
st.subheader(f"{selected_metric} Distribution ({selected_country})")
if selected_metric in df.columns:
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.histplot(df[selected_metric], kde=True, ax=ax, color="orange")
    ax.set_xlabel(selected_metric)
    ax.set_ylabel("Frequency")
    st.pyplot(fig)

# -----------------------------
# Correlation Heatmap
# -----------------------------
st.subheader(f"Correlation Heatmap ({selected_country})")
numeric_cols = df.select_dtypes(include="number").columns
if len(numeric_cols) >= 2:
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(
        df[numeric_cols].corr(),
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        vmin=-1,
        vmax=1,
        annot_kws={"size": 10},
        linewidths=0.5,
        ax=ax
    )
    st.pyplot(fig)
else:
    st.info("Not enough numeric columns to display heatmap.")

# -----------------------------
# Time Series Plot
# -----------------------------
if "Date" in df.columns and selected_metric in df.columns:
    st.subheader(f"{selected_metric} Over Time ({selected_country})")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=df, x="Date", y=selected_metric, ax=ax)
    ax.set_xlabel("Date")
    ax.set_ylabel(selected_metric)
    st.pyplot(fig)

# -----------------------------
# End of App
# -----------------------------
st.write("🌞 End of Solar Data Explorer App")
