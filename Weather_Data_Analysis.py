```python
import pandas as pd
import matplotlib.pyplot as plt

# Sample weather data
data = {
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday", "Sunday"],
    "Temperature": [28, 30, 29, 32, 31, 27, 33]
}

df = pd.DataFrame(data)

# Display weather information
print("WEEKLY WEATHER ANALYSIS")
print("-----------------------")
print(df.to_string(index=False))

# Calculate statistics
print("\nAverage Temperature:", df["Temperature"].mean())
print("Highest Temperature:", df["Temperature"].max())
print("Lowest Temperature:", df["Temperature"].min())

# Plot temperature changes
plt.figure(figsize=(9, 5))
plt.plot(
    df["Day"],
    df["Temperature"],
    marker="o"
)

plt.title("Weekly Temperature Analysis")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.xticks(rotation=30)
plt.tight_layout()

# Save and display the graph
plt.savefig("weather_analysis.png")
plt.show()
```
