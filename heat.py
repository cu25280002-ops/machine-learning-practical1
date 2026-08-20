import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv("students.csv")
correlation = data[["Age", "Marks"]].corr()
print("Correlation Matrix:")
print(correlation)
sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()