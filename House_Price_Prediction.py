```python
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

# Sample housing dataset
data = {
    "Area_sqft": [800, 1000, 1200, 1500, 1800, 2000, 2200, 2500],
    "Bedrooms": [2, 2, 3, 3, 3, 4, 4, 4],
    "Price_lakhs": [35, 42, 50, 62, 75, 85, 95, 110]
}

df = pd.DataFrame(data)

# Select features and target
X = df[["Area_sqft", "Bedrooms"]]
y = df["Price_lakhs"]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate predictions
predictions = model.predict(X_test)

print("HOUSE PRICE PREDICTION")
print("----------------------")
print("Mean Absolute Error:",
      round(mean_absolute_error(y_test, predictions), 2), "lakhs")
print("R-squared Score:",
      round(r2_score(y_test, predictions), 2))

# Predict the price of a sample house
new_house = pd.DataFrame({
    "Area_sqft": [1600],
    "Bedrooms": [3]
})

predicted_price = model.predict(new_house)[0]

print("\nHouse Area: 1600 sqft")
print("Bedrooms: 3")
print("Predicted Price:", round(predicted_price, 2), "lakhs")
```
