# Theory of this code:


# This code demonstrates Linear Regression with model coefficients, intercept,
# and prediction using Scikit-learn. The LinearRegression class is imported to
# create a linear regression model, while the time module is used to add delays
# during the training and prediction phases. The X dataset represents the number
# of hours studied, and y represents the corresponding marks.
# The LinearRegression() object creates the model, and model.fit(X, y)
# trains it by learning the relationship between study hours and marks.
# After training, model.intercept_ gives the intercept (β₀) of the regression equation,
# which represents the predicted value when the input is zero.
# model.coef_[0] gives the coefficient (β₁), which represents how much the predicted
# marks change when study hours increase by one unit. In this example, the relationship
# can be represented as y = 30 + 10x. Therefore, when 3.5 hours are entered into
# model.predict([[3.5]]), the model predicts 65 marks. The time.sleep(3) statements simply
# create a three-second delay to simulate the training and prediction phases.
# However, the line mse = mean_squared_error(y_test, y_pred_test) will produce
# an error because mean_squared_error, y_test, and y_pred_test have not been defined or
# imported in this code. Overall, the code demonstrates the main concepts of training a
# Linear Regression model, understanding its intercept and coefficient,
# and making predictions.







from sklearn.linear_model import LinearRegression
import time

# Sample dataset
X = [[1], [2], [3], [4], [5]]   # Input (Hours Studied)
y = [40, 50, 60, 70, 80]


# create linear regression model

model = LinearRegression()


#train model
model.fit(X, y)

print("################ model is in training phase #############")
time.sleep(3)



print("Intercept (β₀):", model.intercept_)
print("Coefficient (β₁):", model.coef_[0])


mse = mean_squared_error(y_test, y_pred_test)


print("###################### predicting phase #################") 
# predict model
prediction = model.predict([[3.5]])
time.sleep(3)

print("Predicted Marks:", prediction[0])


