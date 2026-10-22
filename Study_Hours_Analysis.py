```python
import pandas as pd
import matplotlib.pyplot as plt

# Sample student study data
data = {
    "Student": ["A", "B", "C", "D", "E", "F"],
    "Study_Hours": [1, 2, 3, 4, 5, 6],
    "Marks": [45, 52, 65, 72, 85, 92]
}

df = pd.DataFrame(data)

# Display the data
print("STUDY HOURS ANALYSIS")
print("--------------------")
print(df.to_string(index=False))

# Calculate average study hours and marks
print("\nAverage Study Hours:", df["Study_Hours"].mean())
print("Average Marks:", df["Marks"].mean())

# Create a scatter plot
plt.figure(figsize=(8, 5))

plt.scatter(
    df["Study_Hours"],
    df["Marks"],
    s=100
)

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.grid(True)
plt.tight_layout()

# Save and display the graph
plt.savefig("study_hours_analysis.png")
plt.show()
```
