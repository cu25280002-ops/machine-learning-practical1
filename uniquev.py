import pandas as pd
data = pd.read_csv("students.csv")
print("Cities in the dataset:")
print(data["City"].unique())