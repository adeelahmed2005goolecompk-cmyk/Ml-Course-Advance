# Ml-Course-Advance...


## codes of python here

# No1 - preprocessing

**Theory :**

This Python program demonstrates how to read and access data from a CSV file using the Pandas library. First, the pandas library is imported with the alias pd, which provides 

useful tools for working with tabular data. The pd.read_csv("data.csv") function is used to load the CSV file into a Pandas DataFrame, which is stored in the variable df. The 

DataFrame is then printed to display all the available data. After that, the "Result" column is selected from the DataFrame and stored in the variable basket. This allows the 

program to work specifically with the values contained in the Result column. The selected column is printed to the screen. The program then prints a separator line to make 

the output easier to understand. Finally, the "Result" column is selected again and stored in basket2, and its values are printed. Overall, this file demonstrates CSV file 

reading, DataFrame creation, column selection, and data display using Pandas.






python code:

```
import pandas as pd
# to read our csv file
df = pd.read_csv("data.csv")
print(df)

basket = df["Result"]
print(basket)

print("\n-------------------------------------------------------\n")

basket2 = df["Result"]
print(basket2)
```
