# Theory of this code:

# This code demonstrates Linear Regression with Mean Squared Error (MSE)
# evaluation using Scikit-learn. The LinearRegression class is imported
# to create the regression model, while mean_squared_error is imported to
# measure the prediction error. The time module is used to add delays during
# the training and prediction phases. The X dataset represents the number of
# hours studied, and y represents the corresponding marks. A LinearRegression()
# model is created and trained using model.fit(X, y), where the model learns the
# relationship between study hours and marks. After training, model.predict(X)
# generates predictions for the same training data. The mean_squared_error(y, y_pred)
# function calculates the average squared difference between the actual marks and
# predicted marks. In this example, the relationship is perfectly linear, so the MSE
# is 0.0, meaning the model's predictions exactly match the given training values.
# Finally, model.predict([[3.5]]) predicts the marks for a student who studied
# for 3.5 hours. Based on the learned relationship, the predicted marks are 65.
# Overall, this code demonstrates the complete basic process of training a Linear
# Regression model, evaluating its error using MSE, and making predictions on new data.)







from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
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

print("###################### predicting phase #################")
time.sleep(3)

# Predict for new data
prediction = model.predict([[3.5]])

print("Predicted Marks:", prediction[0])