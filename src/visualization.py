# src/visualization.py
import matplotlib.pyplot as plt
import seaborn as sns

def plot_line(df, x_col, y_col, title="", xlabel="", ylabel=""):
    """
    Plot a simple line chart
    """
    plt.figure(figsize=(10, 5))
    plt.plot(df[x_col], df[y_col])
    plt.title(title)
    plt.xlabel(xlabel or x_col)
    plt.ylabel(ylabel or y_col)
    plt.grid(True)
    plt.show()

def plot_box(df, x_col, y_col, title="", xlabel="", ylabel=""):
    """
    Plot a boxplot
    """
    plt.figure(figsize=(8, 5))
    sns.boxplot(x=x_col, y=y_col, data=df)
    plt.title(title)
    plt.xlabel(xlabel or x_col)
    plt.ylabel(ylabel or y_col)
    plt.show()

def plot_heatmap(df, title="Correlation Heatmap"):
    """
    Plot correlation heatmap of numeric columns
    """
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=True, fmt=".2f", cmap="coolwarm")
    plt.title(title)
    plt.show()
