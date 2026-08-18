# Theory about this code:

# This code performs residual analysis using Linear Regression on a salary dataset.
# It automatically selects numeric columns, uses the last numeric column as the target,
# and divides the data into training and testing sets. The Linear Regression model
# predicts the target values, and residuals are calculated as the difference between
# actual and predicted values. Finally, a residual plot is created to check how well the
# model fits the data. A good model usually has residuals randomly distributed around zero.







import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# 1. Load Dataset
df = pd.read_csv("salary_data.csv")

print("=" * 70)
print("DATASET")
print("=" * 70)

print(df.head(20))

print("\nDataset Shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())



# 2. Automatically Find Numeric Columns
numeric_columns = df.select_dtypes(include="number").columns.tolist()

print("\nNumeric Columns:")
print(numeric_columns)



# 3. Check Numeric Columns
if len(numeric_columns) < 2:
    raise ValueError(
        "Dataset must contain at least 2 numeric columns "
        "for residual analysis."
    )



# 4. Automatically Select Target
# Use the last numeric column as target
target_column = numeric_columns[-1]

# All other numeric columns become features
feature_columns = numeric_columns[:-1]

print("\n" + "=" * 70)
print("AUTOMATIC SELECTION")
print("=" * 70)

print("Features:", feature_columns)
print("Target:", target_column)



# 5. Create X and y
X = df[feature_columns].copy()
y = df[target_column].copy()



# 6. Handle Missing Values
X = X.fillna(X.median())
y = y.fillna(y.median())



# 7. Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# 8. Create Linear Regression Model
model = LinearRegression()

model.fit(X_train, y_train)



# 9. Make Predictions
y_pred = model.predict(X_test)



# 10. Calculate Residuals
residuals = y_test - y_pred



# 11. Print Results
print("\n" + "=" * 70)
print("RESIDUAL RESULTS")
print("=" * 70)

for actual, predicted, residual in zip(
    y_test,
    y_pred,
    residuals
):
    print(
        f"Actual: {actual:.2f} | "
        f"Predicted: {predicted:.2f} | "
        f"Residual: {residual:.2f}"
    )



# 12. Residual Plot...
plt.figure(figsize=(8, 6))


plt.scatter(
    y_pred,
    residuals
)

plt.axhline(
    y=0,
    linestyle="--"
)

plt.xlabel("Predicted Values")
plt.ylabel("Residuals")

plt.title(
    f"Residual Plot - Target: {target_column}"
)

plt.grid(True)

plt.show()