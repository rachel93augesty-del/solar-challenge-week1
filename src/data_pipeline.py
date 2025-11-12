# src/data_pipeline.py
import pandas as pd

def load_csv(path):
    """
    Load a CSV file into a pandas DataFrame.
    Args:
        path (str): Path to the CSV file
    Returns:
        pd.DataFrame
    """
    return pd.read_csv(path)

def clean_ghi(df):
    """
    Clean GHI column by removing negative values
    Args:
        df (pd.DataFrame)
    Returns:
        pd.DataFrame
    """
    df = df[df['GHI'] >= 0]
    return df

def summary_statistics(df):
    """
    Return summary statistics and missing value report
    Args:
        df (pd.DataFrame)
    Returns:
        pd.DataFrame, pd.Series
    """
    stats = df.describe()
    missing = df.isna().sum()
    return stats, missing

def drop_outliers(df, column_list):
