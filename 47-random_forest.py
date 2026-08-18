# Theory about this code:

# This code demonstrates Gradient Boosting Classification for predicting whether a student will pass or fail.
# The dataset is loaded using Pandas, and features such as Age, Gender, Math, Physics, Chemistry, English, and Attendance are used for prediction.
# Missing values are handled, and categorical values like Gender and Result are converted into numerical form.
# The data is split into training and testing sets, and a GradientBoostingClassifier is trained on the training data.
# The model predicts the test results and is evaluated using Accuracy and a Classification Report.
# Overall, the code shows how Gradient Boosting can be used for student result classification.



import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.ensemble import GradientBoostingClassifier

from sklearn.metrics import accuracy_score, classification_report




# Load dataset
df = pd.read_csv("data.csv")

# Features and labels
# Remove StudentID, Name, and duplicate Result from features
X = df[['Age', 'Gender', 'Math', 'Physics', 'Chemistry', 'English', 'Attendance']]
y = df['Result']  # Target is 'Result'

# Handle missing values in Age column
X['Age'] = X['Age'].fillna(X['Age'].mean())

# Convert Gender to numeric (Male=0, Female=1)
X['Gender'] = X['Gender'].map({'Male': 0, 'Female': 1})

# Convert Result target to binary (Pass=1, Fail=0)
y = y.map({'Pass': 1, 'Fail': 0})

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


model = GradientBoostingClassifier(
    random_state=42
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))

print("Accuracy:", accuracy_score(y_test, y_pred))

# Evaluate model performance
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))