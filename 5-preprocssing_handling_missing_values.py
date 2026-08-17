# Theory about this code:

# This Python program demonstrates **handling missing values
# in a CSV dataset using Pandas**.
# First, the Pandas library is imported and the `data.csv` file is loaded into a DataFrame using `pd.read_csv()`
# The complete dataset is displayed using `print(df)`.
# The program then demonstrates three different methods for replacing missing values in the `Age` column:
# **mean, mode, and median**. The mean method replaces missing values with the average age,
# while the mode method uses the most frequently occurring age.
# The median method replaces missing values with the middle value of the sorted age data.
# In this program, the **median method is currently active**, while the mean and mode methods are commented out.
# Finally, the updated DataFrame is printed, followed by printing only the `Age` column.
# Overall, the program demonstrates **missing-value handling and basic data preprocessing using Pandas**.










import pandas as pd

# Read CSV file
df = pd.read_csv("data.csv")
print(df)

print("\n-------------------------------------------------------\n")

#
# # Replace missing values in Age with mean Age
# df["Age"] = df["Age"].fillna(df["Age"].mean())
#
# print(df)

print("\n-------------------------------------------------------\n")


# Replace missing values with mode
# df["Age"] = df["Age"].fillna(df["Age"].mode()[0])
#
# print(df)

print("\n-------------------------------------------------------\n")


# Replace missing values with median
df["Age"] = df["Age"].fillna(df["Age"].median())

print(df)

# print the age column only
print(df["Age"])
