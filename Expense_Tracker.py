```python
import pandas as pd
import matplotlib.pyplot as plt

# Sample expense data
data = {
    "Category": [
        "Food", "Travel", "Shopping",
        "Food", "Bills", "Travel", "Shopping"
    ],
    "Amount": [250, 100, 500, 300, 800, 150, 400]
}

df = pd.DataFrame(data)

# Display expenses
print("EXPENSE TRACKER")
print("----------------")
print(df.to_string(index=False))

# Calculate total expenses by category
category_expenses = df.groupby("Category")["Amount"].sum()

print("\nExpenses by Category:")
print(category_expenses)

print("\nTotal Expenses: ₹", df["Amount"].sum())
print("Average Expense: ₹", round(df["Amount"].mean(), 2))

# Create a bar chart
plt.figure(figsize=(8, 5))
category_expenses.plot(kind="bar")

plt.title("Expenses by Category")
plt.xlabel("Category")
plt.ylabel("Amount (₹)")
plt.xticks(rotation=0)
plt.tight_layout()

# Save and display the graph
plt.savefig("expense_chart.png")
plt.show()
```
