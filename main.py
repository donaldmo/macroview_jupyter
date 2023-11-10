
import pandas as panda
import matplotlib.pyplot as plotlib
import seaborn as seab

# 3. Exploratory Data Analysis (EDA):
''' Start by plotting the data. Time series plots, line plots, 
    or scatter plots can help you visualize how the data changes over time.
    Calculate basic statistics like mean, median, and standard deviation to 
    get an initial sense of the data distribution.
'''

# Load the data
data = panda.read_csv('cpi_all_data.csv')

# Display the first few rows of the dataset to understand its structure
print(data.head())

# Line plot of Real GDP over time
def plot_line_graph(data):
    plotlib.figure(figsize=(12, 6))