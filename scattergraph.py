import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("students.csv")
plt.scatter(data["Age"], data["Marks"])
plt.title("Age vs Marks")
plt.xlabel("Age")
plt.ylabel("Marks")
plt.show()