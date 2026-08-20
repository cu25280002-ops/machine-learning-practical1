import pandas as pd
data = pd.read_csv("students.csv")
high_marks = data[data["Marks"] >= 80]
print(high_marks)