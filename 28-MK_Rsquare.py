# Theory about this code:

# This code demonstrates Linear Regression with MSE and R² Score evaluation
# using Scikit-learn. The LinearRegression class is used to create the regression model,
# while mean_squared_error and r2_score are used to evaluate its performance.
# The X dataset represents the number of hours studied, and y represents the
# corresponding marks. The model is created using LinearRegression() and trained
# with model.fit(X, y), allowing it to learn the relationship between study hours
# and marks. After training, model.predict(X) generates predictions for the training data.
# The Mean Squared Error (MSE) is calculated using mean_squared_error(y, y_pred)
# and measures the average squared difference between the actual and predicted values.
# In this example, the data follows a perfect linear relationship, so the MSE is 0.0.
# The R² Score is calculated using r2_score(y, y_pred) and indicates how well the model
# explains the variation in the target values. Here, the R² Score is 1.0, meaning the
# model perfectly fits the given data. Finally, model.predict([[3.5]]) predicts the marks
# for a student who studied for 3.5 hours, resulting in 65 marks. Overall, this code
# demonstrates the complete process of training a Linear Regression model, evaluating
# it using MSE and R² Score, and making predictions on new data.







from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error 
from sklearn.metrics import r2_score
import time

# Sample dataset
X = [[1], [2], [3], [4], [5]]   # Input (Hours Studied)
y = [40, 50, 60, 70, 80]         # Output (Marks)

# Create linear regression model
model = LinearRegression()

# Train model
model.fit(X, y)

print("################ model is in training phase #############")
time.sleep(3)


# Predict on training data
y_pred = model.predict(X)

# Calculate MSE
mse = mean_squared_error(y, y_pred)
print("Mean Squared Error (MSE):", mse)

# Calculate R² Score
r2 = r2_score(y, y_pred)
print("R² Score:", r2)

print("###################### predicting phase #################")
time.sleep(3)

# Predict for new data
prediction = model.predict([[3.5]])

print("Predicted Marks:", prediction[0])