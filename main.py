import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv("cpi_all_data.csv")
print()
print(data.dtypes, end='\n\n')

data['Real GDP %'].fillna(method='ffill', inplace=True)
data['CPI ^ %'].fillna('0%', inplace=True)

# Display the first few rows of the dataset to understand its structure
print(data.head(), end='\n\n')

# Summary statistics
print(data.describe(), end='\n\n')


def plot_line(data):
# Line plot of CPI over time
    plt.figure(figsize=(12, 6))
    plt.plot(data['DATE'], data['CPI ^ %'], label='CPI')
    plt.xlabel('Date')
    plt.ylabel('CPI')
    plt.title('Consumer Price Index (CPI) Over Time')
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.legend()
    plt.show()

plot_line(data)

if __name__ == '__main__':
    plot_line()