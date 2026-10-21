import pandas as pd
import matplotlib.pyplot as plt

# Subject marks data
data = {
    "Subject": ["Maths", "Science", "English", "Python", "Statistics"],
    "Marks": [85, 90, 78, 95, 88]
}

df = pd.DataFrame(data)

# Calculate statistics
average_marks = df["Marks"].mean()
highest_marks = df["Marks"].max()
lowest_marks = df["Marks"].min()

print("SUBJECT MARKS ANALYSIS")
print("----------------------")
print(df.to_string(index=False))
print(f"\nAverage Marks: {average_marks:.2f}")
print(f"Highest Marks: {highest_marks}")
print(f"Lowest Marks: {lowest_marks}")

# Generate a bar graph
plt.figure(figsize=(8, 5))
plt.bar(df["Subject"], df["Marks"])

plt.title("Subject Marks Analysis")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.ylim(0, 100)

plt.tight_layout()
plt.savefig("subject_marks_analysis.png")
plt.show()

