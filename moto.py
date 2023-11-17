import pandas as pd
import matplotlib.pyplot as plt

# Sample data (replace this with your own DataFrame)
data = {
    'Date': pd.date_range('2023-01-01', '2023-01-10'),
    'Value': [10, 15, 8, 12, 20, 18, 25, 30, 22, 28]
}

df = pd.DataFrame(data)

# Line plot
df.plot(x='Date', y='Value', kind='line', title='Line Plot')
plt.show()

# Bar plot
df.plot(x='Date', y='Value', kind='bar', title='Bar Plot')
plt.show()

# Histogram
df['Value'].plot(kind='hist', title='Histogram')
plt.show()

# Scatter plot
df.plot(x='Date', y='Value', kind='scatter', title='Scatter Plot')
plt.show()
