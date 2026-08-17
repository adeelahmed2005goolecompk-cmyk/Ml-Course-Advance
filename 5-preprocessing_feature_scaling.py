# Theory About This Code:

# This Python program demonstrates data normalization using
# MinMaxScaler from Scikit-learn. First, the Pandas library
# and MinMaxScaler are imported. The CSV file is loaded into a DataFrame.
# A scaler is created with a feature range from -100 to 100,
# which transforms numerical values into this specified range.
# The Age column is first scaled separately using fit_transform().
# After that, both the Age and Math columns are scaled together using the same scaler.
# Finally, the scaled values of these columns are displayed.
# This process is useful for bringing numerical features to a
# similar scale before applying machine learning algorithms.







import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Read CSV file
df = pd.read_csv("data.csv")
print(df)

# Create scaler
scaler = MinMaxScaler(feature_range=(-100, 100))

# Scale the Age column
df["Age"] = scaler.fit_transform(df[["Age"]])

print(df["Age"])


# Scale the Age column
df[["Age", "Math"]] = scaler.fit_transform(df[["Age", "Math"]])

print(df[["Age", "Math"]])

