# Theory about this code:

# This program uses the Fish Market dataset to predict fish width using Linear and
# Polynomial Regression. The data is divided into training and testing sets, and
# features are standardized using StandardScaler. A Linear Regression model and
# Polynomial Regression models of different degrees are trained and evaluated. MSE and
# R² scores are used to compare model performance. Graphs visualize actual versus
# predicted values and training/testing errors. Finally, different polynomial degrees
# are tested to find the model with better performance.




import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import warnings

warnings.filterwarnings('ignore')

# Load the Fish Market dataset from a reliable source
# Using the Plotly dataset which is stable and doesn't require authentication
url = "https://raw.githubusercontent.com/vincentarelbundock/Rdatasets/master/csv/MASS/fish.csv"
fish_df = pd.read_csv(url)

print("First 5 rows of the dataset:")
print(fish_df.head())
print("\nDataset Info:")
print(fish_df.info())
print("\nDataset Description:")
print(fish_df.describe())

# Define features and target
# Features: Weight, Length1, Length2, Length3, Height
# Target: Width
X = fish_df[['Weight', 'Length1', 'Length2', 'Length3', 'Height']]
y = fish_df['Width']

print(f"\nFeature matrix shape: {X.shape}")
print(f"Target vector shape: {y.shape}")

# Split the data (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"\nTraining set size: {X_train.shape[0]} samples")
print(f"Testing set size: {X_test.shape[0]} samples")

# Preprocessing - Standardization
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("\nFeature scaling complete.")

# 1. Linear Regression Model
lin_reg = LinearRegression()
lin_reg.fit(X_train_scaled, y_train)
y_pred_lin = lin_reg.predict(X_test_scaled)

# Evaluate Linear Regression
mse_lin = mean_squared_error(y_test, y_pred_lin)
r2_lin = r2_score(y_test, y_pred_lin)

print("\n" + "=" * 50)
print("LINEAR REGRESSION RESULTS")
print("=" * 50)
print(f"Mean Squared Error (MSE): {mse_lin:.4f}")
print(f"R-squared (R²) Score: {r2_lin:.4f}")
print(f"Model Intercept: {lin_reg.intercept_:.4f}")
print("Model Coefficients:")
for feature, coef in zip(X.columns, lin_reg.coef_):
    print(f"  {feature}: {coef:.4f}")

# 2. Polynomial Regression Model (Degree 2)
poly = PolynomialFeatures(degree=2, include_bias=False)
X_train_poly = poly.fit_transform(X_train_scaled)
X_test_poly = poly.transform(X_test_scaled)

print(f"\nOriginal feature count: {X_train_scaled.shape[1]}")
print(f"Polynomial feature count (degree 2): {X_train_poly.shape[1]}")

poly_reg = LinearRegression()
poly_reg.fit(X_train_poly, y_train)
y_pred_poly = poly_reg.predict(X_test_poly)

# Evaluate Polynomial Regression
mse_poly = mean_squared_error(y_test, y_pred_poly)
r2_poly = r2_score(y_test, y_pred_poly)

print("\n" + "=" * 50)
print("POLYNOMIAL REGRESSION (Degree 2) RESULTS")
print("=" * 50)
print(f"Mean Squared Error (MSE): {mse_poly:.4f}")
print(f"R-squared (R²) Score: {r2_poly:.4f}")

# 3. Model Comparison
print("\n" + "=" * 50)
print("MODEL COMPARISON")
print("=" * 50)
comparison_df = pd.DataFrame({
    'Model': ['Linear Regression', 'Polynomial Regression (deg 2)'],
    'MSE': [mse_lin, mse_poly],
    'R² Score': [r2_lin, r2_poly]
})
print(comparison_df.to_string(index=False))

# 4. Visualization of Predictions
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Linear Regression predictions
ax1.scatter(y_test, y_pred_lin, alpha=0.7, color='blue')
ax1.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', lw=2)
ax1.set_xlabel('Actual Width')
ax1.set_ylabel('Predicted Width')
ax1.set_title('Linear Regression\nPredictions vs. Actual')
ax1.grid(True, linestyle='--', alpha=0.6)

# Polynomial Regression predictions
ax2.scatter(y_test, y_pred_poly, alpha=0.7, color='green')
ax2.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', lw=2)
ax2.set_xlabel('Actual Width')
ax2.set_ylabel('Predicted Width')
ax2.set_title('Polynomial Regression (deg 2)\nPredictions vs. Actual')
ax2.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()

# 5. Experiment with different polynomial degrees
print("\n" + "=" * 50)
print("EXPERIMENTING WITH DIFFERENT POLYNOMIAL DEGREES")
print("=" * 50)

degrees_to_try = [1, 2, 3, 4]
train_errors = []
test_errors = []

for d in degrees_to_try:
    poly = PolynomialFeatures(degree=d, include_bias=False)
    X_train_poly = poly.fit_transform(X_train_scaled)
    X_test_poly = poly.transform(X_test_scaled)

    model = LinearRegression()
    model.fit(X_train_poly, y_train)

    y_train_pred = model.predict(X_train_poly)
    y_test_pred = model.predict(X_test_poly)

    train_mse = mean_squared_error(y_train, y_train_pred)
    test_mse = mean_squared_error(y_test, y_test_pred)
    train_errors.append(train_mse)
    test_errors.append(test_mse)

    print(f"Degree {d}: Training MSE = {train_mse:.4f}, Test MSE = {test_mse:.4f}")

# Plot the errors for different degrees
plt.figure(figsize=(8, 5))
plt.plot(degrees_to_try, train_errors, label='Training Error (MSE)', marker='o', linewidth=2)
plt.plot(degrees_to_try, test_errors, label='Test Error (MSE)', marker='s', linewidth=2)
plt.xlabel('Polynomial Degree')
plt.ylabel('Mean Squared Error')
plt.title('Training vs. Test Error for Different Polynomial Degrees')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()