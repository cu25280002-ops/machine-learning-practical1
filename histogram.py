import seaborn as sns
import matplotlib.pyplot as plt
marks = [45, 52, 60, 65, 70, 75, 80, 85, 90]
sns.histplot(marks, kde=True)
plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.show()