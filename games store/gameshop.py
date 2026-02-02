import pandas as pd

gameshop = pd.read_csv("pixelvault game sales.csv")
numberofrows = len(gameshop)
numberofcolumns = len(gameshop.columns)
print(gameshop.head())
print(gameshop.tail())
columnames = gameshop.columns 
print (numberofrows)
print (numberofcolumns)
print (columnames)