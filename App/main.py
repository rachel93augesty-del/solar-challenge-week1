import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_processing import load_clean_data, compute_summary_stats


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_processing import load_clean_data, compute_summary_stats

# Sidebar - Country selection
st.sidebar.header("Select Country")
country = st.sidebar.selectbox("Country", ["Benin", "Sierra Leone", "Togo"])

# Load data dynamically
df = load_clean_data(country)

# Display Summary Statistics
st.header(f"Summary Statistics - {country}")
st.dataframe(compute_summary_stats(df))

# Boxplot for GHI
st.header(f"GHI Distribution - {country}")
fig, ax = plt.subplots()
ax.boxplot(df['GHI'])
ax.set_ylabel("GHI")
st.pyplot(fig)

# Optional: Top regions by solar potential
if 'Region' in df.columns:
    st.header("Top Regions by Solar Potential")
    top_regions = df.groupby('Region')['GHI'].mean().sort_values(ascending=False).head(10)
    st.dataframe(top_regions)
