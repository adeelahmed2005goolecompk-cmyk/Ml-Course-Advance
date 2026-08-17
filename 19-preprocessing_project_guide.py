# Theory of this code:

# This code demonstrates the basic process of loading, inspecting,
# and cleaning data using Pandas. First, the pandas library is
# imported as pd, which provides useful tools for working with tabular data.
# The pd.read_csv("data.csv") function loads the CSV file into a DataFrame named df.
# The df.head(1) function displays the first row of the dataset,
# while df.tail(10) displays the last 10 rows. The df.shape function
# shows the number of rows and columns in the dataset. The df.columns
# function displays all column names, and df.dtypes shows the data type of
# each column. The df.describe() function generates statistical information
# such as count, mean, standard deviation, minimum, maximum, and quartile values
# for numerical columns. The df.duplicated() function checks whether any rows
# are duplicated, while df.duplicated().sum() calculates the total number of
# duplicate rows. The pd.to_datetime() function can be used to convert a date
# column into the proper datetime format. The df["Name"].str.strip() function
# removes unnecessary spaces from the beginning and end of text values. Finally,
# df["Name"].str.upper() converts all values in the Name column to uppercase.
# Overall, this code provides a basic introduction to data loading, dataset
# inspection, statistical analysis, duplicate checking, and text data cleaning
# with Pandas.








import pandas as pd

# Load the CSV file
df = pd.read_csv("data.csv")

# Display the first 10 rows
print(df.head(1))

print("###############################  Display last 10 rows ################")
# Display last 10 rows
print(df.tail(10))



print("###############################  shape of data (culums, row) ################")
# Display the shape of the dataset
print(df.shape)


print("###############################  show all columnes ################")
# Display all column names
print(df.columns)

print("###############################  show all columnes datatypes ################")
# Display data types of all columns
data_type_of_all_columns = df.dtypes
print(data_type_of_all_columns)

print("###############################  statistics of dataset ################")

# Generate descriptive statistics
print(df.describe())

print("###############################  check duplicate values  ################")
# Check for duplicate rows
print(df.duplicated())


# Count the total number of duplicate rows
print("Number of duplicate rows:", df.duplicated().sum())

print("###############################  connver column into dateformat  ################")

# Convert the Date column to datetime format
#df["Date"] = pd.to_datetime(df["Date"])


print("###############################  remove extra spaceing from start and end (only valid for string datatype) ################")

# Remove leading and trailing spaces
df["Name"] = df["Name"].str.strip()



print("###############################  connver column into upper case  (only valid for string datatype )################")

# Convert product names to uppercase
df["Name"] = df["Name"].str.upper()













