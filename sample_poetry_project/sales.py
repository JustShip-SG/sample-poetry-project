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


# 3. Product with the best sales
# your code here to find the product with the best sales and print it


# 4. Product with the most steady sales (lowest standard deviation)
# your code here to find the product with the most steady sales and print it
product_std = df.groupby("Product")["Total Sales"].std()
product_best_sales = product_std.idxmin()

print(product_best_sales)