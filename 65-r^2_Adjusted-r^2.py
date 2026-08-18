# Theory about this code:

# This code creates a house price dataset with features such as size, bedrooms,
# bathrooms, age, lot size, and garage. It uses Linear Regression to predict house
# prices and calculates both R² and Adjusted R². Different models are created by adding
# features one by one to compare their performance. The code also tests the same features
# in a different order to show that the final R² and Adjusted R² remain the same.
# Finally, it selects the best model based on the highest Adjusted R².






import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# ============================================================
# 1. Generate Dataset
# ============================================================

np.random.seed(42)

n = 50

size = np.random.randint(800, 3000, n)
bedrooms = np.random.randint(2, 6, n)
bathrooms = np.random.randint(1, 4, n)
age = np.random.randint(0, 30, n)
lot_size = np.random.randint(2000, 8000, n)
garage = np.random.randint(0, 3, n)

# Price formula
noise = np.random.normal(0, 20, n)

price = (
    50
    + 0.12 * size
    + 8 * bedrooms
    + 15 * bathrooms
    - 2 * age
    + 0.02 * lot_size
    + 10 * garage
    + noise
).astype(int)

df = pd.DataFrame({
    'Size': size,
    'Bedrooms': bedrooms,
    'Bathrooms': bathrooms,
    'Age': age,
    'LotSize': lot_size,
    'Garage': garage,
    'Price': price
})

print("=" * 70)
print("DATASET")
print("=" * 70)
print(df.head())
print("\nShape:", df.shape)


# ============================================================
# 2. Define Target
# ============================================================

y = df['Price']


# ============================================================
# 3. Function to Calculate R² and Adjusted R²
# ============================================================

def compute_metrics(X, y):
    model = LinearRegression()
    model.fit(X, y)

    y_pred = model.predict(X)

    r2 = r2_score(y, y_pred)

    n = len(y)
    k = X.shape[1]

    adjusted_r2 = 1 - ((1 - r2) * (n - 1) / (n - k - 1))

    return r2, adjusted_r2, k


# ============================================================
# 4. Build Models Sequentially
# ============================================================

feature_sets = [
    ['Size'],
    ['Size', 'Bedrooms'],
    ['Size', 'Bedrooms', 'Bathrooms'],
    ['Size', 'Bedrooms', 'Bathrooms', 'Age'],
    ['Size', 'Bedrooms', 'Bathrooms', 'Age', 'LotSize'],
    ['Size', 'Bedrooms', 'Bathrooms', 'Age', 'LotSize', 'Garage']
]

results = []

for i, features in enumerate(feature_sets, start=1):

    X = df[features]

    r2, adj_r2, k = compute_metrics(X, y)

    results.append({
        'Model': f'Model {i}',
        'Features Used': ', '.join(features),
        'k (features)': k,
        'R²': r2,
        'Adjusted R²': adj_r2
    })


# ============================================================
# 5. Comparison Table
# ============================================================

results_df = pd.DataFrame(results)

print("\n" + "=" * 70)
print("COMPARISON TABLE")
print("=" * 70)

print(results_df.to_string(
    index=False,
    formatters={
        'R²': '{:.4f}'.format,
        'Adjusted R²': '{:.4f}'.format
    }
))


# ============================================================
# 6. Print Individual Model Results
# ============================================================

print("\n" + "=" * 70)
print("INDIVIDUAL MODEL RESULTS")
print("=" * 70)

for result in results:
    print(
        f"{result['Model']}: "
        f"R²={result['R²']:.4f}, "
        f"Adjusted R²={result['Adjusted R²']:.4f}, "
        f"k={result['k (features)']}"
    )


# ============================================================
# 7. Find Best Model According to Adjusted R²
# ============================================================

best_model = results_df.loc[
    results_df['Adjusted R²'].idxmax()
]

print("\n" + "=" * 70)
print("BEST MODEL")
print("=" * 70)

print("Model:", best_model['Model'])
print("Features:", best_model['Features Used'])
print("R²:", f"{best_model['R²']:.4f}")
print("Adjusted R²:", f"{best_model['Adjusted R²']:.4f}")


# ============================================================
# 8. Challenge Task - Different Feature Order
# ============================================================

different_order = [
    ['Garage'],
    ['Garage', 'LotSize'],
    ['Garage', 'LotSize', 'Age'],
    ['Garage', 'LotSize', 'Age', 'Bathrooms'],
    ['Garage', 'LotSize', 'Age', 'Bathrooms', 'Bedrooms'],
    ['Garage', 'LotSize', 'Age', 'Bathrooms', 'Bedrooms', 'Size']
]

challenge_results = []

for i, features in enumerate(different_order, start=1):

    X = df[features]

    r2, adj_r2, k = compute_metrics(X, y)

    challenge_results.append({
        'Model': f'Challenge Model {i}',
        'Features Used': ', '.join(features),
        'k (features)': k,
        'R²': r2,
        'Adjusted R²': adj_r2
    })


# ============================================================
# 9. Challenge Comparison Table
# ============================================================

challenge_df = pd.DataFrame(challenge_results)

print("\n" + "=" * 70)
print("CHALLENGE - DIFFERENT FEATURE ORDER")
print("=" * 70)

print(challenge_df.to_string(
    index=False,
    formatters={
        'R²': '{:.4f}'.format,
        'Adjusted R²': '{:.4f}'.format
    }
))


# ============================================================
# 10. Verify Final Model
# ============================================================

full_model_original = df[
    ['Size', 'Bedrooms', 'Bathrooms', 'Age', 'LotSize', 'Garage']
]

full_r2_1, full_adj_1, _ = compute_metrics(
    full_model_original,
    y
)

full_model_different = df[
    ['Garage', 'LotSize', 'Age', 'Bathrooms', 'Bedrooms', 'Size']
]

full_r2_2, full_adj_2, _ = compute_metrics(
    full_model_different,
    y
)

print("\n" + "=" * 70)
print("FINAL FULL MODEL COMPARISON")
print("=" * 70)

print(f"Original Order:")
print(f"R² = {full_r2_1:.4f}")
print(f"Adjusted R² = {full_adj_1:.4f}")

print(f"\nDifferent Order:")
print(f"R² = {full_r2_2:.4f}")
print(f"Adjusted R² = {full_adj_2:.4f}")

print("\nFinal Adjusted R² is the same because the final model")
print("contains exactly the same features, regardless of their order.")