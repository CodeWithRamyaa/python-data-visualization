import pandas as pd
import matplotlib.pyplot as plt

# Sample student performance data
data = {
    "Subject": ["Maths", "Science", "English", "Python", "Statistics"],
    "Marks": [85, 90, 78, 95, 88]
}

df = pd.DataFrame(data)

# Display the graph
plt.figure(figsize=(8, 5))
plt.bar(df["Subject"], df["Marks"])

plt.title("Student Performance Analysis")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.ylim(0, 100)

plt.tight_layout()
plt.savefig("student_performance_graph.png")
plt.show()
