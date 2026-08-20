import pandas as pd
data= pd.read_csv("students.csv")
misvalue= data.isnull().sum()
print( misvalue)