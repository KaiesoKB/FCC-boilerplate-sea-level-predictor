import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    # print(df.head(20))

    # Create scatter plot
    x_data = df['Year']
    y_data = df['CSIRO Adjusted Sea Level']
    plt.figure(figsize=(10, 6))
    plt.scatter(x_data, y_data, color='blue', marker='o', alpha=0.7)

    # Create first line of best fit
    result = linregress(x_data, y_data)
    print(f"Slope: {result.slope}")
    print(f"Intercept: {result.intercept}")

    x_fit = np.arange(x_data.min(), 2051)
    y_fit = (result.slope * x_fit) + result.intercept
    plt.plot(x_fit, y_fit, color='red', label="Line of best fit (to 2050)")

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    x_data_recent = df_recent['Year']
    y_data_recent = df_recent['CSIRO Adjusted Sea Level']
    result_2000s = linregress(x_data_recent, y_data_recent)
    x_fit_part_two = np.arange(x_data_recent.min(), 2051)
    y_fit_part_two = (result_2000s.slope * x_fit_part_two) + result_2000s.intercept
    plt.plot(x_fit_part_two, y_fit_part_two, color='green', label="Line of best fit (From 2000 to 2050)")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()
        
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
