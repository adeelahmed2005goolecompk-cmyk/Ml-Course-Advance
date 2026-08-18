# Theory about this code:

# This code demonstrates Polynomial Regression using Python and Scikit-learn.
# It loads salary data and uses YearsExperience to predict Salary.
# PolynomialFeatures(degree=3) converts the input into polynomial features up to degree 3.
# The data is divided into training and testing sets to evaluate the model properly.
# The model is evaluated using MSE, RMSE, MAE, and R² Score.
# It also predicts the salary for a new experience value of 13 years.
# Finally, Matplotlib displays the actual data and the Polynomial Regression
# curve, while NumPy is used for an additional polynomial fitting example.







import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import numpy
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import time


# 1. Read CSV
df = pd.read_csv("salary_data.csv")

# 2. Prepare data
X = df[["YearsExperience"]]
y = df["Salary"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)



# 3. Create polynomial features (degree 3)
poly = PolynomialFeatures(degree=3)
X_poly_train = poly.fit_transform(X_train)
X_poly_test = poly.transform(X_test)

print(X_poly_train)

print("\n---------------------------\n")
print(X_poly_test)


print("\n\n--------------- training started -------------------\n\n")
# 4. Train polynomial regression
model = LinearRegression()
model.fit(X_poly_train, y_train)
time.sleep(3)

# 5. Make predictions
y_pred = model.predict(X_poly_test)



# 6. Evaluation Matric
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)


print("Value of MSE", mse)
print("Value of RMSE", rmse)
print("Value of MAE", mae)
print("value of r square", r2)


print("\n\n----------------- predicted values -------------------------\n\n")
# pridicting on new value
new_exp = [[13]]
new_exp_poly = poly.transform(new_exp)
pred = model.predict(new_exp_poly)
print(pred[0])




# 7. Scatter Plot with Polynomial Regression Curve

plt.figure(figsize=(8, 6))

# Scatter plot of original data
plt.scatter(X, y, color="blue", label="Actual Data")

# Create smooth X values for curve
X_range = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
X_range_poly = poly.transform(X_range)

# Predict using polynomial model
y_range_pred = model.predict(X_range_poly)

# Plot regression curve
plt.plot(X_range, y_range_pred, color="red", linewidth=2, label="Polynomial Regression")

plt.title("Polynomial Regression")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.legend()
plt.grid(True)
plt.show()
print("\n\n----------------- predicted values -------------------------\n\n")
x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

print(r2_score(y, mymodel(x)))



