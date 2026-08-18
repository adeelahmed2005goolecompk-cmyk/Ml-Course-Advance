# Theory about this code:

# This code demonstrates how to build a Multiple Linear Regression model using a CSV
# dataset and Scikit-learn. First, LinearRegression is imported to create the
# regression model, while mean_squared_error and r2_score are used to evaluate its
# performance. Pandas is used to read and process the CSV dataset, and the time module
# adds a delay during the training and prediction phases. The pd.read_csv() function loads
# the data.csv file into a DataFrame named df. The input features are Physics, English,
# Chemistry, and Math, which are stored in X, while the Result column is selected as the
# target variable y. A LinearRegression() model is created and trained using model.fit(X, y),
# allowing the model to learn how the four subject scores are related to the student('s result.'
# After training, model.predict(X) generates predictions for the existing dataset.
# The Mean Squared Error (MSE) measures the average squared difference between the actual
# and predicted results, while the R² Score measures how well the model explains the variation
# in the target values. Finally, a new student's subject scores are stored in a Pandas
# DataFrame, and model.predict(new_student) predicts the student('s result based on those
# scores. The predicted value is then displayed using print(). Overall, this code
# demonstrates the complete process of loading data, selecting multiple features,
# training a Multiple Linear Regression model, evaluating its performance, and predicting the
# result for a new student.)











from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import time

# Read dataset
df = pd.read_csv("C:/Users/PC/Desktop/data.csv")

print(df)

# Input and Output
X = df[["Physics", "English", "Chemistry","Math"]]
y = df["Result"]

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

print("################ model is in training phase #############")
time.sleep(3)

# Predict on training data
y_pred = model.predict(X)

# Evaluation
mse = mean_squared_error(y, y_pred)
print("Mean Squared Error (MSE):", mse)

r2 = r2_score(y, y_pred)
print("R² Score:", r2)



print("###################### predicting on new data #################")
time.sleep(3)

# New student's data
new_student = pd.DataFrame({
    "Physics": [85],
    "English": [90],
    "Chemistry": [88],
    "Math": [87]
})

# Predict
prediction = model.predict(new_student)

print("Predicted Result (Raw):", prediction[0])
