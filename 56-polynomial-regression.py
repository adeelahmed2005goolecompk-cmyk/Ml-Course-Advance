# Theory about this code:


# This code demonstrates a complete Data Preprocessing and Polynomial Regression workflow.
# It creates a student dataset, handles missing values, and converts categorical data into numerical form.
# The data is split into training and testing sets and standardized using StandardScaler.
# Polynomial features of different degrees are created and used to train regression models.
# The models are evaluated using MAE, MSE, RMSE, and R² Score.
# Finally, the code compares Linear and Polynomial Regression and visualizes their performance.



# ============================================================================
# DATA PREPROCESSING & POLYNOMIAL REGRESSION ASSIGNMENT
# ============================================================================

# Import all necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression  # <-- This was missing
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import warnings

warnings.filterwarnings('ignore')

# Set style for better visualizations
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

print("=" * 70)
print("DATA PREPROCESSING & POLYNOMIAL REGRESSION ASSIGNMENT")
print("=" * 70)

# ============================================================================
# PART 1: DATA PREPROCESSING
# ============================================================================

# 1.1 Load the dataset
print("\n" + "=" * 50)
print("1. LOADING DATASET")
print("=" * 50)

# Create synthetic dataset (similar to Student Scores Dataset)
np.random.seed(42)
n_samples = 100

# Create base data
data = {
    'Hours_Studied': np.random.uniform(1, 10, n_samples),
    'Previous_Score': np.random.uniform(40, 95, n_samples),
    'Attendance': np.random.uniform(60, 100, n_samples),
    'Gender': np.random.choice(['Male', 'Female'], n_samples),
    'Subject': np.random.choice(['Math', 'Science', 'English', 'History'], n_samples),
}

df = pd.DataFrame(data)

# Make Exam_Score dependent on other variables
df['Exam_Score'] = (df['Hours_Studied'] * 3.5 +
                    df['Previous_Score'] * 0.4 +
                    df['Attendance'] * 0.2 +
                    np.random.normal(0, 5, n_samples))

# Clip exam scores to 0-100 range
df['Exam_Score'] = df['Exam_Score'].clip(0, 100)

# Introduce some missing values
df.loc[np.random.choice(n_samples, 5, replace=False), 'Attendance'] = np.nan
df.loc[np.random.choice(n_samples, 3, replace=False), 'Previous_Score'] = np.nan

print(f"Dataset created successfully!")
print(f"Shape: {df.shape}")
print(f"Columns: {list(df.columns)}")

# 1.2 Display first 5 rows
print("\n" + "=" * 50)
print("2. FIRST 5 ROWS")
print("=" * 50)
print(df.head())

# 1.3 Dataset information
print("\n" + "=" * 50)
print("3. DATASET INFORMATION")
print("=" * 50)
print(df.info())

# 1.4 Summary statistics
print("\n" + "=" * 50)
print("4. SUMMARY STATISTICS")
print("=" * 50)
print(df.describe())

# 1.5 Check for missing values
print("\n" + "=" * 50)
print("5. MISSING VALUES ANALYSIS")
print("=" * 50)
missing_values = df.isnull().sum()
missing_percentages = (df.isnull().sum() / len(df)) * 100
missing_df = pd.DataFrame({
    'Missing Values': missing_values,
    'Percentage': missing_percentages
})
print(missing_df[missing_df['Missing Values'] > 0])

# 1.6 Handle missing values
print("\n" + "=" * 50)
print("6. HANDLING MISSING VALUES")
print("=" * 50)

df_processed = df.copy()

# Handle missing values
for column in df_processed.columns:
    if df_processed[column].dtype in ['float64', 'int64']:
        df_processed[column].fillna(df_processed[column].mean(), inplace=True)
    elif df_processed[column].dtype == 'object':
        df_processed[column].fillna(df_processed[column].mode()[0], inplace=True)

print(f"Missing values handled!")
print(f"Remaining missing values: {df_processed.isnull().sum().sum()}")

# 1.7 Convert categorical columns into numerical values
print("\n" + "=" * 50)
print("7. ENCODING CATEGORICAL VARIABLES")
print("=" * 50)

categorical_cols = df_processed.select_dtypes(include=['object']).columns
print(f"Categorical columns: {list(categorical_cols)}")

# Label Encoding
label_encoder = LabelEncoder()
df_encoded = df_processed.copy()

for col in categorical_cols:
    df_encoded[col] = label_encoder.fit_transform(df_encoded[col])
    print(f"Encoded '{col}': {dict(zip(label_encoder.classes_, label_encoder.transform(label_encoder.classes_)))}")

print("\nDataset after encoding:")
print(df_encoded.head())

# 1.8 Separate Features (X) and Target (y)
print("\n" + "=" * 50)
print("8. SEPARATING FEATURES AND TARGET")
print("=" * 50)

y = df_encoded['Exam_Score']
X = df_encoded.drop('Exam_Score', axis=1)

print(f"Features shape: {X.shape}")
print(f"Target shape: {y.shape}")
print(f"Features: {list(X.columns)}")
print(f"Target: Exam_Score")

# 1.9 Split dataset into 80% training and 20% testing
print("\n" + "=" * 50)
print("9. SPLITTING DATASET (80% Train, 20% Test)")
print("=" * 50)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"Training set: {X_train.shape[0]} samples")
print(f"Testing set: {X_test.shape[0]} samples")

# 1.10 Scale the input features using StandardScaler
print("\n" + "=" * 50)
print("10. FEATURE SCALING (StandardScaler)")
print("=" * 50)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("Feature scaling completed!")
print(f"Scaled training data shape: {X_train_scaled.shape}")
print(f"Scaled testing data shape: {X_test_scaled.shape}")

# ============================================================================
# PART 2: POLYNOMIAL REGRESSION
# ============================================================================

print("\n" + "=" * 50)
print("PART 2: POLYNOMIAL REGRESSION")
print("=" * 50)

# 2.1 Import PolynomialFeatures (already imported)
print("\n" + "=" * 50)
print("11. CREATING POLYNOMIAL FEATURES (Degree = 2)")
print("=" * 50)

poly = PolynomialFeatures(degree=2, include_bias=False)
X_train_poly = poly.fit_transform(X_train_scaled)
X_test_poly = poly.transform(X_test_scaled)

print(f"Original features: {X_train_scaled.shape[1]}")
print(f"Polynomial features: {X_train_poly.shape[1]}")
print(f"Polynomial feature names: {poly.get_feature_names_out(X_train.columns)}")

# 2.2 Train Linear Regression model using transformed data
print("\n" + "=" * 50)
print("12. TRAINING POLYNOMIAL REGRESSION MODEL")
print("=" * 50)

poly_model = LinearRegression()
poly_model.fit(X_train_poly, y_train)

print("Model trained successfully!")
print(f"Coefficients shape: {poly_model.coef_.shape}")
print(f"Intercept: {poly_model.intercept_:.4f}")

# 2.3 Predict on testing data
print("\n" + "=" * 50)
print("13. MAKING PREDICTIONS")
print("=" * 50)

y_train_pred = poly_model.predict(X_train_poly)
y_test_pred = poly_model.predict(X_test_poly)

print("Predictions completed!")
print("\nFirst 10 predictions (Test set):")
comparison_df = pd.DataFrame({
    'Actual': y_test[:10].values,
    'Predicted': y_test_pred[:10]
})
print(comparison_df)

# 2.4 Calculate evaluation metrics
print("\n" + "=" * 50)
print("14. MODEL EVALUATION METRICS")
print("=" * 50)

# Calculate metrics for training set
train_mae = mean_absolute_error(y_train, y_train_pred)
train_mse = mean_squared_error(y_train, y_train_pred)
train_rmse = np.sqrt(train_mse)
train_r2 = r2_score(y_train, y_train_pred)

# Calculate metrics for testing set
test_mae = mean_absolute_error(y_test, y_test_pred)
test_mse = mean_squared_error(y_test, y_test_pred)
test_rmse = np.sqrt(test_mse)
test_r2 = r2_score(y_test, y_test_pred)

# Create metrics DataFrame
metrics_df = pd.DataFrame({
    'Metric': ['MAE', 'MSE', 'RMSE', 'R² Score'],
    'Training Set': [train_mae, train_mse, train_rmse, train_r2],
    'Test Set': [test_mae, test_mse, test_rmse, test_r2]
})
print(metrics_df)

print("\n" + "-" * 40)
print(f"Test Set Performance:")
print(f"  MAE : {test_mae:.4f}")
print(f"  MSE : {test_mse:.4f}")
print(f"  RMSE: {test_rmse:.4f}")
print(f"  R²  : {test_r2:.4f}")
print("-" * 40)

# 2.5 Plot original data points and Polynomial Regression Curve
print("\n" + "=" * 50)
print("15. VISUALIZING RESULTS")
print("=" * 50)

# Create visualization
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# Plot 1: Actual vs Predicted (Test Set)
axes[0, 0].scatter(y_test, y_test_pred, alpha=0.6, color='blue')
axes[0, 0].plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
axes[0, 0].set_xlabel('Actual Values')
axes[0, 0].set_ylabel('Predicted Values')
axes[0, 0].set_title(f'Polynomial Regression: Actual vs Predicted (R² = {test_r2:.4f})')
axes[0, 0].grid(True, alpha=0.3)

# Plot 2: Residual Plot
residuals = y_test - y_test_pred
axes[0, 1].scatter(y_test_pred, residuals, alpha=0.6, color='green')
axes[0, 1].axhline(y=0, color='red', linestyle='--', lw=2)
axes[0, 1].set_xlabel('Predicted Values')
axes[0, 1].set_ylabel('Residuals')
axes[0, 1].set_title('Residual Plot')
axes[0, 1].grid(True, alpha=0.3)

# Plot 3: Data Distribution
if X_train_scaled.shape[1] >= 1:
    axes[1, 0].scatter(X_train_scaled[:, 0], y_train, alpha=0.6, color='blue', label='Training Data')
    axes[1, 0].scatter(X_test_scaled[:, 0], y_test, alpha=0.6, color='orange', label='Test Data')
    axes[1, 0].set_xlabel(f'{X_train.columns[0]} (Scaled)')
    axes[1, 0].set_ylabel('Exam Score')
    axes[1, 0].set_title('Data Distribution by First Feature')
    axes[1, 0].legend()
    axes[1, 0].grid(True, alpha=0.3)

# Plot 4: Learning Curve
sample_sizes = np.arange(10, len(X_train_scaled), 10)
train_errors = []
test_errors = []

for size in sample_sizes:
    X_sub = X_train_scaled[:size]
    y_sub = y_train[:size]
    X_sub_poly = poly.fit_transform(X_sub)
    model_sub = LinearRegression()
    model_sub.fit(X_sub_poly, y_sub)
    y_sub_pred = model_sub.predict(X_sub_poly)
    y_test_pred_sub = model_sub.predict(X_test_poly)
    train_errors.append(mean_squared_error(y_sub, y_sub_pred))
    test_errors.append(mean_squared_error(y_test, y_test_pred_sub))

axes[1, 1].plot(sample_sizes, train_errors, 'o-', label='Training Error', color='blue')
axes[1, 1].plot(sample_sizes, test_errors, 's-', label='Test Error', color='red')
axes[1, 1].set_xlabel('Training Set Size')
axes[1, 1].set_ylabel('MSE')
axes[1, 1].set_title('Learning Curve')
axes[1, 1].legend()
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('polynomial_regression_results.png', dpi=300, bbox_inches='tight')
plt.show()

# 2.6 Compare with Simple Linear Regression
print("\n" + "=" * 50)
print("16. COMPARISON: LINEAR vs POLYNOMIAL REGRESSION")
print("=" * 50)

# Train simple linear regression
simple_model = LinearRegression()  # Now this works!
simple_model.fit(X_train_scaled, y_train)
y_test_pred_simple = simple_model.predict(X_test_scaled)

# Calculate metrics for simple linear regression
simple_mae = mean_absolute_error(y_test, y_test_pred_simple)
simple_mse = mean_squared_error(y_test, y_test_pred_simple)
simple_rmse = np.sqrt(simple_mse)
simple_r2 = r2_score(y_test, y_test_pred_simple)

# Comparison DataFrame
comparison_df = pd.DataFrame({
    'Metric': ['MAE', 'MSE', 'RMSE', 'R² Score'],
    'Linear Regression': [simple_mae, simple_mse, simple_rmse, simple_r2],
    'Polynomial Regression': [test_mae, test_mse, test_rmse, test_r2],
    'Improvement': [
        f"{(simple_mae - test_mae) / simple_mae * 100:.2f}%",
        f"{(simple_mse - test_mse) / simple_mse * 100:.2f}%",
        f"{(simple_rmse - test_rmse) / simple_rmse * 100:.2f}%",
        f"{(test_r2 - simple_r2) / abs(simple_r2) * 100:.2f}%"
    ]
})
print(comparison_df)

# Visual comparison
fig, ax = plt.subplots(figsize=(10, 6))
x_range = np.linspace(y_test.min(), y_test.max(), 100)

ax.scatter(y_test, y_test_pred_simple, alpha=0.6, label='Linear Regression', color='blue')
ax.scatter(y_test, y_test_pred, alpha=0.6, label='Polynomial Regression', color='green')
ax.plot(x_range, x_range, 'r--', label='Perfect Prediction', lw=2)

ax.set_xlabel('Actual Values')
ax.set_ylabel('Predicted Values')
ax.set_title('Linear vs Polynomial Regression Comparison')
ax.legend()
ax.grid(True, alpha=0.3)
plt.savefig('model_comparison.png', dpi=300, bbox_inches='tight')
plt.show()

# ============================================================================
# BONUS: Try Polynomial Degrees 2, 3, and 4
# ============================================================================

print("\n" + "=" * 50)
print("BONUS: COMPARING DIFFERENT POLYNOMIAL DEGREES")
print("=" * 50)

degrees = [2, 3, 4]
results = []

for degree in degrees:
    poly = PolynomialFeatures(degree=degree, include_bias=False)
    X_train_poly = poly.fit_transform(X_train_scaled)
    X_test_poly = poly.transform(X_test_scaled)

    model = LinearRegression()
    model.fit(X_train_poly, y_train)

    y_pred = model.predict(X_test_poly)

    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)

    results.append({
        'Degree': degree,
        'R² Score': r2,
        'MAE': mae,
        'MSE': mse,
        'RMSE': rmse,
        'Feature Count': X_train_poly.shape[1]
    })

# Create comparison DataFrame
comparison_df = pd.DataFrame(results)
print(comparison_df)

# Visualize R² scores for different degrees
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(comparison_df['Degree'], comparison_df['R² Score'],
        'o-', linewidth=2, markersize=10, color='blue')
ax.set_xlabel('Polynomial Degree')
ax.set_ylabel('R² Score')
ax.set_title('Model Performance by Polynomial Degree')
ax.grid(True, alpha=0.3)

for idx, row in comparison_df.iterrows():
    ax.annotate(f'{row["R² Score"]:.4f}',
                (row['Degree'], row['R² Score']),
                textcoords="offset points",
                xytext=(0, 10),
                ha='center')

plt.savefig('degree_comparison.png', dpi=300, bbox_inches='tight')
plt.show()

# Determine best degree
best_degree = comparison_df.loc[comparison_df['R² Score'].idxmax(), 'Degree']
print(f"\nBEST MODEL: Polynomial Degree {best_degree}")
print(f"Best R² Score: {comparison_df['R² Score'].max():.4f}")

print("\n" + "=" * 50)
print("EXPLANATION")
print("=" * 50)
print(f"Degree {best_degree} gives the best performance because it provides the")
print("optimal balance between bias and variance. Lower degrees may underfit")
print("the data, while higher degrees may overfit.")
print("The model with degree 2 captures the underlying pattern without")
print("overfitting to noise in the data.")

# ============================================================================
# FINAL SUMMARY
# ============================================================================

print("\n" + "=" * 70)
print("ASSIGNMENT COMPLETED SUCCESSFULLY")
print("=" * 70)

print("\nFINAL SUMMARY:")
print("-" * 70)
print(f"Dataset Shape: {df.shape}")
print(f"Training Samples: {X_train.shape[0]}")
print(f"Testing Samples: {X_test.shape[0]}")
print(f"Number of Features: {X.shape[1]}")
print(f"\nBEST MODEL: Polynomial Regression (Degree = {best_degree})")
print(f"Performance on Test Set:")
print(f"  - MAE : {test_mae:.4f}")
print(f"  - MSE : {test_mse:.4f}")
print(f"  - RMSE: {test_rmse:.4f}")
print(f"  - R²  : {test_r2:.4f}")
print("-" * 70)
print("\nAll plots have been saved as PNG files:")
print("  - polynomial_regression_results.png")
print("  - model_comparison.png")
print("  - degree_comparison.png")
print("\n" + "=" * 70)