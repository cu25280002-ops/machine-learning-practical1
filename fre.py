import pandas as pd
data= pd.read_csv("students.csv")
frequency= data["City"].value_counts()
print(frequency)