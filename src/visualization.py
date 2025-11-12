# src/visualization.py
import matplotlib.pyplot as plt
import seaborn as sns

def plot_ghi_histogram(df):
    sns.histplot(df['GHI'])
    plt.show()