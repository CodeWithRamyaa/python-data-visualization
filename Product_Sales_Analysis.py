import pandas as pd
import matplotlib.pyplot as plt

# Product sales data
data = {
    "Product": ["Laptop", "Phone", "Tablet", "Headphones", "Keyboard"],
    "Units_Sold": [10, 25, 15, 30, 20],
    "Price": [50000, 20000, 15000, 2000, 1500]
}

df = pd.DataFrame(data)

# Calculate revenue for each product
df["Revenue"] = df["Units_Sold"] * df["Price"]

# Display the report
print("PRODUCT SALES ANALYSIS")
print("----------------------")
print(df.to_string(index=False))

# Calculate total revenue
print("\nTotal Revenue:", df["Revenue"].sum())

# Find the best-selling product by units
best_selling = df.loc[df["Units_Sold"].idxmax(), "Product"]
print("Best-Selling Product:", best_selling)

# Plot product revenue
plt.figure(figsize=(9, 5))
plt.bar(df["Product"], df["Revenue"])

plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=20)
plt.tight_layout()

# Save and display the graph
plt.savefig("product_sales_graph.png")
plt.show()

