import pandas as pd
data = pd.read_csv("students.csv")
sorted_data = data.sort_values(by="Marks", ascending=False)
print(sorted_data)