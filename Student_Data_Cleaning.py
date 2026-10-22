```python
import pandas as pd

# Sample student data with missing values
data = {
    "Student": ["A", "B", "C", "D", "E", "F"],
    "Maths": [85, 90, None, 76, 88, 92],
    "Science": [78, None, 85, 80, 91, 87],
    "English": [90, 82, 88, None, 85, 94]
}

df = pd.DataFrame(data)

print("ORIGINAL STUDENT DATA")
print(df)

# Count missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Replace missing marks with the column average
subjects = ["Maths", "Science", "English"]

for subject in subjects:
    df[subject] = df[subject].fillna(df[subject].mean())

# Round marks to two decimal places
df[subjects] = df[subjects].round(2)

print("\nCLEANED STUDENT DATA")
print(df)

# Calculate each student's average marks
df["Average"] = df[subjects].mean(axis=1).round(2)

print("\nSTUDENT AVERAGES")
print(df[["Student", "Average"]])

# Save the cleaned data
df.to_csv("cleaned_student_data.csv", index=False)

print("\nCleaned data saved to cleaned_student_data.csv")
```
