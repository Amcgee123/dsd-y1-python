import pandas as pd
df = pd.read_csv('students (1).csv')
rows = len(df)
print(df.to_string()) 
print("Number of students:", rows)