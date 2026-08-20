import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("students.csv")
plt.hist(data["Marks"], bins=5)
plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.show()