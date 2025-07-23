import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv('sales_data.csv')

# Preview the dataset
print("First 5 rows:")
print(df.head())

# Show summary info
print("\nInfo:")
print(df.info())

# Total sales by product
sales_by_product = df.groupby('Product')['Sales'].sum().sort_values(ascending=False)
print("\nTotal Sales by Product:")
print(sales_by_product)

# Plot sales by product
plt.figure(figsize=(8,5))
sales_by_product.plot(kind='bar', color='orange')
plt.title('Total Sales by Product')
plt.xlabel('Product')
plt.ylabel('Sales')
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot sales over time
df['Date'] = pd.to_datetime(df['Date'])
daily_sales = df.groupby('Date')['Sales'].sum()

plt.figure(figsize=(8,5))
daily_sales.plot(marker='o')
plt.title('Daily Sales Trend')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.grid(True)
plt.tight_layout()
plt.show()
