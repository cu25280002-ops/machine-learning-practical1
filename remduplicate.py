import pandas as pd
data = pd.read_csv("students.csv")
print("Before removing duplicates:", len(data))
data = data.drop_duplicates()
print("After removing duplicates:", len(data))
print(data)