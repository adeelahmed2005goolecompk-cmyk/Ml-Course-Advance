# Theory about this code:

# This code demonstrates a complete Simple Linear Regression model with evaluation,
# prediction, regression equation, and visualization using Scikit-learn, NumPy,
# and Matplotlib. First, LinearRegression is imported to create the regression model,
# while mean_squared_error and r2_score are used to evaluate its performance.
# NumPy is used to store the input and output data as numerical arrays,
# and Matplotlib is used to visualize the results. The dataset contains hours studied
# as the input X and marks as the output y. A Linear Regression model is created and
# trained using model.fit(X, y), allowing the model to learn the relationship between
# study hours and marks. The model then predicts values for the original
# data using model.predict(X). The MSE measures the average squared difference between
# actual and predicted marks, while the R² Score measures how well the regression model
# explains the variation in the data. Because this dataset has a perfect linear
# relationship, the MSE is 0.0 and the R² Score is 1.0. The model then predicts the
# marks for a new input of 3.5 hours, giving a prediction of 65 marks.
# The coef_ and intercept_ values are used to create the regression equation,
# which is Marks = 10.00 × Hours + 30.00. The Matplotlib section creates a graph
# containing the original data points, the regression line, and the predicted point
# for 3.5 hours. Dashed helper lines show the predicted hours and marks on the graph.
# The equation, MSE, and R² Score are also displayed inside the graph using plt.text().
# Overall, this code demonstrates the complete workflow of building, training, evaluating,
# predicting, explaining, and visually presenting a Simple Linear Regression model.








from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import numpy as np
import time

# ============================
# Sample Dataset
# ============================
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([40, 50, 60, 70, 80])

# ============================
# Create Model
# ============================
model = LinearRegression()

print("################ Training Model ################")
time.sleep(2)

# Train
model.fit(X, y)

# ============================
# Predictions
# ============================
y_pred = model.predict(X)

# Metrics
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

print("Mean Squared Error (MSE):", mse)
print("R² Score:", r2)

print("\n################ Prediction ################")
time.sleep(2)

new_x = np.array([[3.5]])
prediction = model.predict(new_x)

print("Hours Studied :", new_x[0][0])
print("Predicted Marks :", prediction[0])

# ============================
# Regression Equation
# ============================
slope = model.coef_[0]
intercept = model.intercept_

print("\nRegression Equation")
print(f"Marks = {slope:.2f} × Hours + {intercept:.2f}")

# ============================
# Plot
# ============================
plt.figure(figsize=(8,6))

# Original data
plt.scatter(
    X,
    y,
    color='blue',
    s=100,
    label='Actual Data'
)

# Regression line
plt.plot(
    X,
    y_pred,
    color='red',
    linewidth=3,
    label='Regression Line'
)

# Predicted point
plt.scatter(
    new_x,
    prediction,
    color='green',
    s=150,
    marker='*',
    label='Prediction (3.5 hrs)'
)

# Dashed helper lines
plt.plot(
    [3.5, 3.5],
    [0, prediction[0]],
    linestyle='--',
    color='green'
)

plt.plot(
    [0, 3.5],
    [prediction[0], prediction[0]],
    linestyle='--',
    color='green'
)

# Labels
plt.title("Simple Linear Regression", fontsize=16)
plt.xlabel("Hours Studied", fontsize=12)
plt.ylabel("Marks", fontsize=12)

# Equation + Metrics
text = (
    f"Equation: y = {slope:.2f}x + {intercept:.2f}\n"
    f"MSE = {mse:.2f}\n"
    f"R² = {r2:.2f}"
)

plt.text(
    1.1,
    73,
    text,
    fontsize=10,
    bbox=dict(facecolor='white', alpha=0.8)
)

plt.grid(True)
plt.legend()

plt.show()