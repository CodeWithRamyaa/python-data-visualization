import pandas as pd
import matplotlib.pyplot as plt

# Monthly sales data
data = {
    "Month": [
        "January", "February", "March", "April",
        "May", "June"
    ],
    "Sales": [12000, 15000, 18000, 14000, 22000, 25000]
}

df = pd.DataFrame(data)

# Display sales information
print("MONTHLY SALES REPORT")
print("--------------------")
print(df.to_string(index=False))

# Calculate total and average sales
total_sales = df["Sales"].sum()
average_sales = df["Sales"].mean()

print("\nTotal Sales:", total_sales)
print("Average Monthly Sales:", round(average_sales, 2))

# Create a line graph
plt.figure(figsize=(9, 5))
plt.plot(df["Month"], df["Sales"], marker="o")

plt.title("Monthly Sales Analysis")
plt.xlabel("Month")
plt.ylabel("Sales Amount")
plt.xticks(rotation=30)
plt.grid(True)
plt.tight_layout()

# Save and display the graph
plt.savefig("monthly_sales_graph.png")
plt.show()
