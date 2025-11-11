import pandas as pd

def load_clean_data(country):
    """Load the cleaned CSV for a given country."""
    file_map = {
        "Benin": "data/benin_clean.csv",
        "Sierra Leone": "data/sierraleone_clean.csv",
        "Togo": "data/togo_clean.csv"
    }
    return pd.read_csv(file_map[country])

def compute_summary_stats(df):
    """Return basic summary statistics."""
    return df.describe()