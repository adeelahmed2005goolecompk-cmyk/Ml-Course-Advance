# Thoery about this code:
# This Python program demonstrates Label Encoding of categorical data
# using Pandas and Scikit-learn.
# First, the Pandas library and LabelEncoder are imported.
# The data.csv file is then loaded into a DataFrame and displayed.
# A LabelEncoder object is created to convert categorical text values into numerical
# values. The Gender column is encoded using fit_transform(),
# which assigns a unique number to each category.
# The same process is then applied to the Result column.
# Finally, the updated DataFrame is printed,
# showing how categorical values have been converted
# into numerical form for use in machine learning models.





import pandas as pd
from sklearn.preprocessing import LabelEncoder


# Read CSV file
df = pd.read_csv("data.csv")
print(df)

print("###################################")

le = LabelEncoder()

df["Gender"] = le.fit_transform(df["Gender"])

print(df)

df["Result"] = le.fit_transform(df["Result"])
print(df)