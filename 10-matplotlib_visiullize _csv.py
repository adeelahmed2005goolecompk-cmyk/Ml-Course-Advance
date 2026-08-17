# Theory About This Code:

# This Python program demonstrates visualizing categorical gender data
# using Matplotlib. First, Pandas and Matplotlib are imported, and the data.csv file
# is loaded into a DataFrame. The value_counts() function is used to count
# the number of occurrences of each gender and store the results in gender_counts.
# A figure size of 6×6 is created for the graph.
# The plt.plot() function then plots the values from the Gender column as individual
# points using the 'o' marker. A title, "Gender Distribution", is added to the graph,
# and plt.show() displays the visualization.







import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

gender_counts = df["Gender"].value_counts()

plt.figure(figsize=(6,6))
plt.plot(df["Gender"], 'o')

plt.title("Gender Distribution")
plt.show()