import pandas as pd
data1= pd.read_csv("students.csv")
row,column= data1.shape
print("Row:",row)
print("Column:",column)