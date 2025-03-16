import pandas as pd  # Import Pandas

# Load CSV file (Make sure the file path is correct!)
df = pd.read_csv("/Users/yelinlee/Downloads/data.csv", encoding="ISO-8859-1")

# Display the first 5 rows
print(df.head())

# Show column information
print(df.info())

# Check for missing values
print(df.isnull().sum())

import matplotlib.pyplot as plt

# Convert InvoiceDate to datetime format
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Extract year and month
df["YearMonth"] = df["InvoiceDate"].dt.to_period("M")

# Calculate total sales per month
df["TotalSales"] = df["Quantity"] * df["UnitPrice"]
monthly_sales = df.groupby("YearMonth")["TotalSales"].sum()

# Plot sales trend
plt.figure(figsize=(12, 6))
monthly_sales.plot(marker="o", linestyle="-", color="b")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.title("Monthly Sales Trend")
plt.grid(True)
plt.show()

# Filter only returned products (Quantity < 0)
returned_products = df[df["Quantity"] < 0]

# Group by product (StockCode) and sum absolute quantity to find total returns per product
returned_products_summary = returned_products.groupby("StockCode")["Quantity"].sum().abs()

# Sort by highest number of returns
top_returned_products = returned_products_summary.sort_values(ascending=False).head(5)
 
# Plot top 5 returned products
plt.figure(figsize=(10, 6))
top_returned_products.plot(kind="bar", color="salmon")
plt.xlabel("Product (StockCode)")
plt.ylabel("Total Quantity Returned")
plt.title("Top 5 Most Returned Products")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()


sales_by_country = df.groupby("Country")["TotalSales"].sum().sort_values(ascending=False)
plt.figure(figsize=(12, 6))
sales_by_country.plot(kind="bar", color="skyblue")
plt.title("Total Sales by Country")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

df["TotalSales"] = df["Quantity"] * df["UnitPrice"]
order_values = df.groupby("InvoiceNo")["TotalSales"].sum()
AOV = order_values.mean()
print(f"Average Order Value: {AOV:.2f}")
print(order_values.head())  
print(AOV)  