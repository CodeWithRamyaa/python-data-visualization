```python
import pandas as pd
import matplotlib.pyplot as plt

# Create a sample dataset
data = {
    "Product": ["Laptop", "Phone", "Tablet", "Headphones", "Keyboard"],
    "Units_Sold": [10, 25, 15, 30, 20],
    "Price": [50000, 20000, 15000, 2000, 1500]
}

df = pd.DataFrame(data)

# Calculate revenue
df["Revenue"] = df["Units_Sold"] * df["Price"]

# Save the dataset as a CSV file
df.to_csv("sales_data.csv", index=False)

# Display dataset
print("SALES DATASET")
print(df.to_string(index=False))

# Summary statistics
print("\nTOTAL REVENUE:", df["Revenue"].sum())
print("AVERAGE REVENUE:", round(df["Revenue"].mean(), 2))
print("TOTAL UNITS SOLD:", df["Units_Sold"].sum())

# Find product with the highest revenue
best_product = df.loc[df["Revenue"].idxmax(), "Product"]
print("HIGHEST REVENUE PRODUCT:", best_product)

# Create a revenue chart
plt.figure(figsize=(8, 5))
plt.bar(df["Product"], df["Revenue"])

plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue (₹)")
plt.xticks(rotation=20)
plt.tight_layout()

plt.savefig("sales_revenue_chart.png")
plt.show()
```
