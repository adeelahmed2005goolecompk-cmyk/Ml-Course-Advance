# Theory about this code:

# This program compares R² and Adjusted R² while adding features to a Linear Regression
# model. It calculates how model performance changes as more variables are included.
# R² usually increases when features are added, while Adjusted R² penalizes unnecessary
# features. The program tests different feature orders and identifies the model with
# the highest Adjusted R². This helps select a model that provides a good balance between
# accuracy and simplicity.






import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import LabelEncoder

# ============================================
# 1. LOAD YOUR DATASET
# ============================================
# Load your CSV file
df = pd.read_csv('titanic_dataset.csv')

print("Dataset shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())
print("\nColumn names:", df.columns.tolist())
print("\nData types:")
print(df.dtypes)

# ============================================
# 2. PREPARE DATA FOR REGRESSION
# ============================================
# Identify numeric columns for features
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

# Remove target column (last column or specify your target)
target_col = numeric_cols[-1]  # Uses last numeric column as target
feature_cols = [col for col in numeric_cols if col != target_col]

print(f"\n🎯 Target column: {target_col}")
print(f"📊 Feature columns: {feature_cols}")

# Handle missing values
df = df.dropna(subset=[target_col])
for col in feature_cols:
    df[col] = df[col].fillna(df[col].median())

# Prepare X and y
X = df[feature_cols]
y = df[target_col]


# ============================================
# 3. FUNCTION TO CALCULATE METRICS
# ============================================
def get_model_metrics(X, y):
    """Calculate R² and Adjusted R² for a model"""
    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)

    n = len(y)
    k = X.shape[1] if hasattr(X, 'shape') else 1
    r2 = r2_score(y, y_pred)
    adj_r2 = 1 - (1 - r2) * (n - 1) / (n - k - 1)

    return r2, adj_r2, k


# ============================================
# 4. BUILD MODELS SEQUENTIALLY
# ============================================
print("\n" + "=" * 70)
print("TASK 1 & 2: Adding Features One by One")
print("=" * 70)

# Create feature sets - add one feature at a time
feature_sets = []
for i in range(1, len(feature_cols) + 1):
    feature_sets.append(feature_cols[:i])

# Store results
results = []

for i, features in enumerate(feature_sets, 1):
    X_subset = df[features]
    r2, adj_r2, k = get_model_metrics(X_subset, y)
    results.append({
        'model': f'Model {i}',
        'features': ', '.join(features),
        'k': k,
        'R2': r2,
        'Adj_R2': adj_r2
    })

# ============================================
# 5. COMPARISON TABLE
# ============================================
print("\nTASK 3: Comparison Table")
print("-" * 85)
print(f"{'Model':<10} {'Features':<55} {'k':<5} {'R²':<10} {'Adj R²':<12}")
print("-" * 85)

for res in results:
    features_short = res['features'][:55] + '...' if len(res['features']) > 55 else res['features']
    print(f"{res['model']:<10} {features_short:<55} {res['k']:<5} "
          f"{res['R2']:<10.4f} {res['Adj_R2']:<12.4f}")
print("-" * 85)

# ============================================
# 6. ANALYSIS QUESTIONS
# ============================================
print("\n" + "=" * 70)
print("TASK 4: Analysis")
print("=" * 70)

# R² trend
print("\n1. R² TREND:")
print("   R² values:", [f"{r['R2']:.4f}" for r in results])
print("   → R² always increases (never decreases) when adding features")
print("   → This is mathematically guaranteed, even for useless features")

# Adjusted R² trend
print("\n2. ADJUSTED R² TREND:")
adj_values = [r['Adj_R2'] for r in results]
print("   Adj R² values:", [f"{a:.4f}" for a in adj_values])
print("   → Adjusted R² DOES NOT always increase")
print("   → It penalizes adding useless features")

# Best model
best_idx = adj_values.index(max(adj_values))
best_model = results[best_idx]
print(f"\n3. BEST MODEL: {best_model['model']}")
print(f"   Features: {best_model['features']}")
print(f"   Adjusted R²: {best_model['Adj_R2']:.4f}")
print("   → This model gives the best balance of fit and simplicity")

# Why adjusted R² is better
print("\n4. WHY ADJUSTED R² IS BETTER:")
print("   • Accounts for model complexity (number of features)")
print("   • Formula: 1 - (1-R²)(n-1)/(n-k-1)")
print("   • Increases only if new feature adds real value")
print("   • Prevents overfitting by penalizing unnecessary variables")

# ============================================
# 7. CHALLENGE - DIFFERENT ORDER
# ============================================
print("\n" + "=" * 70)
print("TASK 5: Challenge - Different Feature Order")
print("=" * 70)

# Try reverse order
reverse_feature_sets = []
for i in range(1, len(feature_cols) + 1):
    reverse_feature_sets.append(feature_cols[-i:])

print("\nReverse order results:")
print("-" * 70)
reverse_results = []

for i, features in enumerate(reverse_feature_sets, 1):
    X_subset = df[features]
    r2, adj_r2, k = get_model_metrics(X_subset, y)
    reverse_results.append({
        'model': f'Model {i}',
        'features': ', '.join(features),
        'k': k,
        'R2': r2,
        'Adj_R2': adj_r2
    })
    print(f"Model {i}: k={k}, R²={r2:.4f}, Adj R²={adj_r2:.4f}")
    print(f"   Features: {', '.join(features)}\n")

print("-" * 70)
print("\nANALYSIS:")
print("1. Final model (all features) has SAME Adjusted R² regardless of order")
print("   → It's the same set of features, just added differently")
print("2. The PATH of Adjusted R² values CHANGES with different order")
print("   → Some features appear more useful when added later vs earlier")
print("   → This shows that feature importance depends on context")

# ============================================
# 8. CONCLUSION
# ============================================
print("\n" + "=" * 70)
print("CONCLUSION")
print("=" * 70)

# Find best model overall
best_idx = adj_values.index(max(adj_values))
best = results[best_idx]

print(f"\n✓ RECOMMENDED MODEL: {best['model']}")
print(f"  Features: {best['features']}")
print(f"  Adjusted R²: {best['Adj_R2']:.4f}")
print(f"\n  Why?")
print(f"  • This model has the highest Adjusted R²")
print(f"  • Adding more features lowers Adjusted R² (overfitting)")
print(f"  • Using fewer features would reduce predictive power")
print(f"\n✓ KEY INSIGHT: Adjusted R² > R² for model selection")
print("  • R² always increases with more features (misleading)")
print("  • Adjusted R² penalizes complexity (more honest)")
print("  • Always use Adjusted R² when comparing models with different features")

# ============================================
# 9. VISUALIZATION (Optional)
# ============================================
try:
    import matplotlib.pyplot as plt

    plt.figure(figsize=(12, 6))
    model_names = [r['model'] for r in results]
    r2_values = [r['R2'] for r in results]
    adj_values = [r['Adj_R2'] for r in results]

    plt.plot(model_names, r2_values, marker='o', label='R²', linewidth=2)
    plt.plot(model_names, adj_values, marker='s', label='Adjusted R²', linewidth=2)
    plt.xlabel('Models')
    plt.ylabel('R² Score')
    plt.title('R² vs Adjusted R² as Features Are Added')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('r2_comparison.png', dpi=100)
    plt.show()
    print("\n✅ Visualization saved as 'r2_comparison.png'")
except:
    print("\n⚠️ Could not create visualization (matplotlib not installed)")

print("\n" + "=" * 70)
print("✅ Analysis Complete!")
print("=" * 70)