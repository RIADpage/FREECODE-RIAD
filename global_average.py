import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data
    df = pd.read_csv("epa-sea-level.csv")
    
    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], label="Data", alpha=0.6)
    
    # First line of best fit (1880-2050)
    slope, intercept, _, _, _ = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years_extended = pd.Series(range(1880, 2051))
    plt.plot(years_extended, slope * years_extended + intercept, 'r', label="Best Fit: 1880-2050")
    
    # Second line of best fit (2000-2050)
    df_2000 = df[df["Year"] >= 2000]
    slope_2000, intercept_2000, _, _, _ = linregress(df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"])
    years_future = pd.Series(range(2000, 2051))
    plt.plot(years_future, slope_2000 * years_future + intercept_2000, 'g', label="Best Fit: 2000-2050")
    
    # Labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()
    plt.grid(True)
    
    # Save and return plot
    plt.savefig("sea_level_plot.png")
    return plt
