import pandas as pd
data = pd.read_csv("students.csv")
result = data.loc[0:4, ["Name", "Marks", "City"]]
print(result)