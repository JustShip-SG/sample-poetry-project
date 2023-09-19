import pandas as pd

import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("sales_data.csv")

# Compute total sales per day: sales = units sold * price per unit
df["Total Sales"] = df["Units Sold"] * df["Price per Unit"]
print (df)

# 1. Sales trend across the dates
# your code here to plot the sales trend across the dates
x = df["Date"]
y = df["Total Sales"]

plt.plot(x, y)
plt.title("Sales trend across the dates")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.show()

# 2. Total sales and Average sales per day
# your code here to print the total sales and average sales per day

# Convert the 'Date' column to datetime type
df['Date'] = pd.to_datetime(df['Date'])

# Calculate 'Total Sales' by multiplying 'Units Sold' by 'Price per unit'
df['Total Sales'] = df['Units Sold'] * df['Price per Unit']

# Group the DataFrame by 'Date' and calculate the daily total sales and average sales
daily_sales = df.groupby('Date')['Total Sales'].agg(['sum', 'mean'])

# Print the results
print("Total Sales:")
print(daily_sales['sum'])
print("\nAverage Sales per Day:")
print(daily_sales['mean'])

# 3. Product with the best sales
# your code here to find the product with the best sales and print it

best_product = df[df['Total Sales'] == df['Total Sales'].max()]['Product'].values[0]

# Print the result
print(f"The product with the best sales is: {best_product}")

# 4. Product with the most steady sales (lowest standard deviation)
# your code here to find the product with the most steady sales and print it
product_std = df.groupby("Product")["Total Sales"].std()
PBS = product_std.idxmin()

print(PBS)