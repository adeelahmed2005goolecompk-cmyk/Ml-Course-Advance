# Theory about this code:

# This code is used for Decision Tree Classification using a dataset such as Titanic.
# It loads and preprocesses the dataset, handles missing values, and converts categorical data into numbers.
# Different Decision Tree depths are tested to find the model with the best accuracy.
# The model is evaluated using accuracy, classification report, and confusion matrix.
# Feature importance is also calculated to identify which features contribute most to predictions.
# Finally, different visualizations are created to understand the model's performance.



import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ============================================
# 1. FIND AND LOAD DATASET
# ============================================
# Try different common dataset names
dataset_names = ['titanic_dataset.csv']
df = None

for filename in dataset_names:
    if os.path.exists(filename):
        df = pd.read_csv(filename)
        print(f"✅ Loaded: {filename}")
        break

if df is None:
    # If no file found, use a sample dataset
    print("⚠️ No CSV file found. Creating sample dataset...")
    np.random.seed(42)
    n = 100
    df = pd.DataFrame({
        'Age': np.random.randint(18, 65, n),
        'Income': np.random.randint(20000, 100000, n),
        'Score': np.random.randint(50, 100, n),
        'Gender': np.random.choice(['Male', 'Female'], n),
        'City': np.random.choice(['New York', 'LA', 'Chicago'], n),
        'Target': np.random.choice(['Yes', 'No'], n)
    })
    print("✅ Created sample dataset")

# ============================================
# 2. DATA EXPLORATION
# ============================================
print("\n" + "=" * 70)
print("DATA EXPLORATION")
print("=" * 70)
print(f"Dataset shape: {df.shape}")
print(f"\nColumns: {df.columns.tolist()}")
print(f"\nFirst 3 rows:\n{df.head(3)}")

# Check for missing values
print(f"\nMissing values:\n{df.isnull().sum()}")

# ============================================
# 3. AUTO-DETECT TARGET COLUMN
# ============================================
# Try to find the target column (classification target)
target_col = None
potential_targets = ['Result', 'Target', 'Survived', 'Grade', 'Status', 'Class', 'Category']

for col in potential_targets:
    if col in df.columns:
        target_col = col
        break

# If no standard target found, use the last column or a column with few unique values
if target_col is None:
    # Find columns with few unique values (likely categorical/target)
    for col in df.columns:
        if df[col].nunique() <= 5 and df[col].dtype == 'object':
            target_col = col
            break
    # If still none, use last column
    if target_col is None:
        target_col = df.columns[-1]

print(f"\n🎯 Target Column: '{target_col}'")

# ============================================
# 4. AUTO-DETECT FEATURES
# ============================================
# Identify numeric columns for features
feature_cols = []
for col in df.columns:
    if col != target_col:
        if df[col].dtype in ['int64', 'float64']:
            feature_cols.append(col)
        elif df[col].nunique() > 2:  # categorical with many unique values (like names)
            continue
        else:
            feature_cols.append(col)

print(f"📊 Features: {feature_cols[:10]}{'...' if len(feature_cols) > 10 else ''}")

# ============================================
# 5. DATA PREPROCESSING
# ============================================
print("\n" + "=" * 70)
print("DATA PREPROCESSING")
print("=" * 70)

# Remove rows with missing target values
df = df.dropna(subset=[target_col])

# Handle missing values in features
for col in feature_cols:
    if df[col].dtype in ['int64', 'float64']:
        df[col] = df[col].fillna(df[col].median())
    else:
        df[col] = df[col].fillna(df[col].mode()[0])

# Encode categorical features
le_features = {}
for col in feature_cols:
    if df[col].dtype == 'object':
        le = LabelEncoder()
        df[col + '_encoded'] = le.fit_transform(df[col].astype(str))
        feature_cols[feature_cols.index(col)] = col + '_encoded'
        le_features[col] = le

# Encode target variable
le_target = LabelEncoder()
df[target_col + '_encoded'] = le_target.fit_transform(df[target_col].astype(str))

# Prepare X and y
X = df[[col for col in feature_cols if col.endswith('_encoded') or df[col].dtype in ['int64', 'float64']]]
y = df[target_col + '_encoded']

# Ensure all columns are numeric
for col in X.columns:
    if X[col].dtype == 'object':
        X[col] = LabelEncoder().fit_transform(X[col].astype(str))

print(f"✅ Feature shape: {X.shape}")
print(f"✅ Target shape: {y.shape}")
print(f"✅ Target classes: {le_target.classes_}")

# ============================================
# 6. TRAIN DECISION TREE MODELS
# ============================================
print("\n" + "=" * 70)
print("DECISION TREE CLASSIFICATION")
print("=" * 70)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Try different depths
depths = [3, 5, 7, 10, None]  # None means unlimited
results = []

for depth in depths:
    dt = DecisionTreeClassifier(max_depth=depth, random_state=42)
    dt.fit(X_train, y_train)

    train_acc = dt.score(X_train, y_train)
    test_acc = dt.score(X_test, y_test)

    depth_str = 'Unlimited' if depth is None else depth
    results.append((depth_str, train_acc, test_acc, dt))
    print(f"Depth={depth_str:>9}: Train={train_acc:.4f}, Test={test_acc:.4f}")

# Select best model (based on test accuracy)
best_idx = max(range(len(results)), key=lambda i: results[i][2])
best_depth, best_train, best_test, best_model = results[best_idx]

print(f"\n🏆 Best Model: Depth={best_depth}, Test Accuracy={best_test:.4f}")

# ============================================
# 7. EVALUATION
# ============================================
print("\n" + "=" * 70)
print("MODEL EVALUATION")
print("=" * 70)

y_pred = best_model.predict(X_test)

print(f"\nAccuracy: {accuracy_score(y_test, y_pred):.4f}")
print(f"\nClassification Report:\n{classification_report(y_test, y_pred, target_names=le_target.classes_)}")
print(f"\nConfusion Matrix:\n{confusion_matrix(y_test, y_pred)}")

# Feature importance
feature_importance = pd.DataFrame({
    'feature': X.columns,
    'importance': best_model.feature_importances_
}).sort_values('importance', ascending=False)

print(f"\n📊 Top Features:\n{feature_importance.head(10)}")

# ============================================
# 8. VISUALIZATIONS
# ============================================
print("\n" + "=" * 70)
print("CREATING VISUALIZATIONS")
print("=" * 70)

# Plot 1: Decision Tree
plt.figure(figsize=(20, 10))
plot_tree(best_model,
          feature_names=X.columns,
          class_names=le_target.classes_,
          filled=True,
          rounded=True,
          max_depth=3,
          fontsize=10)
plt.title(f'Decision Tree (Depth={best_depth})')
plt.tight_layout()
plt.savefig('decision_tree.png', dpi=100)
print("✅ Saved: decision_tree.png")

# Plot 2: Feature Importance
plt.figure(figsize=(12, 6))
top_n = min(10, len(feature_importance))
plt.barh(feature_importance['feature'][:top_n], feature_importance['importance'][:top_n])
plt.xlabel('Feature Importance')
plt.title('Top Features for Classification')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('feature_importance.png', dpi=100)
print("✅ Saved: feature_importance.png")

# Plot 3: Model Performance
plt.figure(figsize=(10, 6))
depth_values = [str(r[0]) for r in results]
train_accs = [r[1] for r in results]
test_accs = [r[2] for r in results]
plt.plot(depth_values, train_accs, marker='o', label='Training Accuracy')
plt.plot(depth_values, test_accs, marker='s', label='Testing Accuracy')
plt.xlabel('Max Depth')
plt.ylabel('Accuracy')
plt.title('Decision Tree Performance vs Max Depth')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('model_performance.png', dpi=100)
print("✅ Saved: model_performance.png")

# Plot 4: Confusion Matrix
plt.figure(figsize=(8, 6))
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=le_target.classes_,
            yticklabels=le_target.classes_)
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.tight_layout()
plt.savefig('confusion_matrix.png', dpi=100)
print("✅ Saved: confusion_matrix.png")

# ============================================
# 9. MAKE PREDICTIONS
# ============================================
print("\n" + "=" * 70)
print("MAKE PREDICTIONS")
print("=" * 70)

# Use test set for sample predictions
sample_indices = np.random.choice(len(X_test), min(5, len(X_test)), replace=False)
sample_data = X_test.iloc[sample_indices]
sample_predictions = best_model.predict(sample_data)

print("\nSample Predictions:")
for i, (idx, pred) in enumerate(zip(sample_indices, sample_predictions)):
    actual = y_test.iloc[i]
    pred_label = le_target.classes_[pred]
    actual_label = le_target.classes_[actual]
    status = "✅ Correct" if pred == actual else "❌ Wrong"
    print(f"Sample {i + 1}: Predicted={pred_label}, Actual={actual_label} {status}")

# ============================================
# 10. SUMMARY
# ============================================
print("\n" + "=" * 70)
print("FINAL SUMMARY")
print("=" * 70)

print(f"""
✅ Decision Tree Classification Completed Successfully!

📊 Dataset: {df.shape[0]} rows, {df.shape[1]} columns
🎯 Target: {target_col}
📈 Best Model Accuracy: {best_test:.4f}
🔍 Top 3 Features:
  1. {feature_importance.iloc[0]['feature']}: {feature_importance.iloc[0]['importance']:.4f}
  2. {feature_importance.iloc[1]['feature']}: {feature_importance.iloc[1]['importance']:.4f}
  3. {feature_importance.iloc[2]['feature']}: {feature_importance.iloc[2]['importance']:.4f}

📁 Files Saved:
  - decision_tree.png
  - feature_importance.png
  - model_performance.png
  - confusion_matrix.png

💡 Tip: This code works with ANY dataset automatically!
""")

plt.show()
print("\n🎉 Done!")