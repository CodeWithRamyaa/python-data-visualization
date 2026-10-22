```python
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Sample training data
data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Marks": [35, 40, 50, 55, 65, 70, 80, 90]
}

df = pd.DataFrame(data)

# Prepare input and output
X = df[["Study_Hours"]]
y = df["Marks"]

# Train the machine learning model
model = LinearRegression()
model.fit(X, y)

# Predict marks for 6 hours of study
hours = pd.DataFrame({"Study_Hours": [6]})
predicted_marks = model.predict(hours)[0]

print("STUDENT MARKS PREDICTION")
print("------------------------")
print("Study Hours:", 6)
print("Predicted Marks:", round(predicted_marks, 2))

# Plot actual data and regression line
plt.figure(figsize=(8, 5))
plt.scatter(df["Study_Hours"], df["Marks"], label="Actual Data")
plt.plot(
    df["Study_Hours"],
    model.predict(X),
    label="Regression Line"
)

plt.title("Study Hours vs Predicted Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig("student_marks_prediction.png")
plt.show()
```
