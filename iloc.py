import pandas as pd
data = pd.read_csv("students.csv")
result = data.iloc[0:5, 0:4]
print(result)