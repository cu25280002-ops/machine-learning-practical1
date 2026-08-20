import pandas as pd
data = pd.read_csv("students.csv")
data = data.rename(columns={
    "Marks": "Score",
    "City": "Location"
})
print(data.head())