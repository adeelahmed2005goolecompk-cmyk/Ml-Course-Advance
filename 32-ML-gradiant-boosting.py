# Theory about this code:


# This code demonstrates LightGBM Regression for predicting passenger fares using Titanic dataset features.
# It loads the dataset, handles missing values, and converts categorical data into numerical values.
# The data is divided into training and testing sets, and a LGBMRegressor model is trained.
# The model predicts fares and is evaluated using MSE, RMSE, MAE, and R² Score.
# It also predicts the fare for a new passenger using the trained model.
# Finally, a scatter plot compares the actual fares with predicted fares.





import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from lightgbm import LGBMRegressor
import time
import subprocess

try:
    result = subprocess.check_output(['ver'], shell=True, stderr=subprocess.STDOUT)
    print(result.decode())
except Exception as e:
    print(f"Error: {e}")

# 1. Read CSV File
df = pd.read_csv("titanic_dataset.csv")

# Print column names
print(df.columns.tolist())

# 2. Handle Missing Values
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Fare"] = df["Fare"].fillna(df["Fare"].median())
df["Cabin"] = df["Cabin"].fillna("Unknown")
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# 3. Convert Categorical Columns to Numeric
df["Name"] = df["Name"].astype("category").cat.codes
df["Sex"] = df["Sex"].astype("category").cat.codes
df["Ticket"] = df["Ticket"].astype("category").cat.codes
df["Cabin"] = df["Cabin"].astype("category").cat.codes
df["Embarked"] = df["Embarked"].astype("category").cat.codes

# 4. Features (X)
X = df[[
    "PassengerId",
    "Survived",
    "Pclass",
    "Name",
    "Sex",
    "Age",
    "SibSp",
    "Parch",
    "Ticket",
    "Cabin",
    "Embarked"
]]

# 5. Target (y)
y = df["Fare"]

# 6. Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# 7. Create LightGBM Regression Model
model = LGBMRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=3,
    random_state=42
)

# 8. Train Model
model.fit(X_train, y_train)
time.sleep(1)

# 9. Make Predictions
y_pred = model.predict(X_test)

# 10. Evaluation Metrics
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Value of MSE :", mse)
print("Value of RMSE:", rmse)
print("Value of MAE :", mae)
print("Value of R2 Score:", r2)

# 11. Predict for a New Passenger
new_passenger = pd.DataFrame(
    [[892, 0, 3, 100, 1, 25, 0, 0, 200, 50, 2]],
    columns=[
        "PassengerId",
        "Survived",
        "Pclass",
        "Name",
        "Sex",
        "Age",
        "SibSp",
        "Parch",
        "Ticket",
        "Cabin",
        "Embarked"
    ]
)

pred = model.predict(new_passenger)

print("\nPredicted Fare:", round(pred[0], 2))

# 12. Plot Actual vs Predicted
plt.figure(figsize=(6, 6))
plt.scatter(y_test, y_pred, color="blue")
plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    color="red"
)
plt.xlabel("Actual Fare")
plt.ylabel("Predicted Fare")
plt.title("LightGBM Regression: Actual vs Predicted")
plt.grid(True)
plt.show()







