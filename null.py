import pandas as pd
d= pd.read_csv("students.csv")
print("missing value:",d.isnull())