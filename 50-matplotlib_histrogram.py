# Theory about this code:

# This code demonstrates Logistic Regression Classification using a dataset with numerical and categorical features.
# It loads the data, handles missing values, and converts categorical values into numerical form using LabelEncoder.
# The dataset is divided into training and testing sets, and features are standardized using StandardScaler.
# A LogisticRegression model is trained to classify the target variable.
# The model is evaluated using a Confusion Matrix and Accuracy Score.
# Finally, a histogram is used to visualize the distribution of the first standardized feature.



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score

# Load dataset
dataset = pd.read_csv('Data.csv')

# Display column names to understand the structure
print("Column names:", dataset.columns.tolist())
print("\nFirst 5 rows:")
print(dataset.head())
print("\nData types:")
print(dataset.dtypes)

# Split features and target (assuming last column is target)
X = dataset.iloc[:, :-1].copy()
y = dataset.iloc[:, -1].copy()

# Identify numeric and categorical columns
numeric_cols = X.select_dtypes(include=[np.number]).columns.tolist()
categorical_cols = X.select_dtypes(include=['object']).columns.tolist()

print(f"\nNumeric columns: {numeric_cols}")
print(f"Categorical columns: {categorical_cols}")

# Handle missing values for numeric columns only
for col in numeric_cols:
    if X[col].isnull().any():
        X[col] = X[col].fillna(X[col].mean())

# Encode categorical columns
for col in categorical_cols:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col].astype(str))

# Encode target variable
le = LabelEncoder()
y = le.fit_transform(y)

# Convert to numpy array
X = X.values

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Train the model
classifier = LogisticRegression(random_state=0)
classifier.fit(X_train, y_train)

# Predict
y_pred = classifier.predict(X_test)

# Confusion matrix and accuracy
cm = confusion_matrix(y_test, y_pred)
print(f'\nConfusion Matrix:\n{cm}')
print(f'Accuracy: {accuracy_score(y_test, y_pred)}')

# Create histogram for the first numeric column
plt.figure(figsize=(10, 6))
plt.hist(X_train[:, 0], bins=10, color='blue', alpha=0.7, edgecolor='black')
plt.title('Distribution of First Feature in Training Set')
plt.xlabel('Feature Value (Standardized)')
plt.ylabel('Frequency')
plt.grid(True, alpha=0.3)
plt.show()