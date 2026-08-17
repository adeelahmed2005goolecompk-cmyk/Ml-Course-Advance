# Theory About This Code:

# This Python program demonstrates splitting a dataset into training
# and testing sets using Scikit-learn. First, the Pandas library and
# train_test_split function are imported, and the CSV file is loaded
# into a DataFrame. The features are stored in X, which contains student
# information such as StudentID, Name, Age, Gender, Math, Physics, Chemistry,
# English, and Attendance. The target labels are stored in Y, which contains
# the Result column. The train_test_split() function divides the features and
# labels into training and testing data, with 80% used for training and 20% used
# for testing. The random_state=42 ensures that the same split can be reproduced
# each time.Finally, the training features, testing features, training labels, and
# testing labels are displayed separately.







import pandas as pd
from sklearn.model_selection import train_test_split

# Read CSV file
df = pd.read_csv("data.csv")
print(df)



print("############################################################")

# X are features
# Y are labels

X = df[["StudentID", "Name" , "Age" , "Gender" , "Math" ,  "Physics", "Chemistry", "English", "Attendance"]]
Y = df["Result"]

print(X)
print(Y)


print("################################# spliting data into 4 chunks ############################")

X_train, X_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

print("Triaining data features")
print(X_train)

print("Testing Data Features")
print(X_test)

print("labels of train dataset")
print(y_train)

print("labels of test dataset")
print(y_test )