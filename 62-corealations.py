# Theory about this code:

# This code performs correlation analysis on the Titanic dataset to study the relationship between different variables and the Result.
# It preprocesses the data and converts categorical values such as Gender, Ticket, and Cabin into numerical values.
# Pearson correlation and Cramer's V are used to measure relationships between variables.
# The code creates scatter plots, box plots, a correlation bar chart, and a heatmap for better visualization.
# It also calculates p-values and identifies whether correlations are strong, moderate, weak, or very weak.
# Finally, the correlation results and visualizations are saved into CSV and image files.




# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# from scipy.stats import chi2_contingency
# from sklearn.preprocessing import LabelEncoder
# import warnings
#
# warnings.filterwarnings('ignore')
#
# # ============================================
# # STEP 1: LOAD THE DATA
# # ============================================
# print("=" * 80)
# print("STEP 1: LOADING THE DATA")
# print("=" * 80)
#
# df = pd.read_csv('titanic_dataset.csv')
# print(f"Dataset loaded successfully with {len(df)} rows and {len(df.columns)} columns")
# print("\nFirst 5 rows:")
# print(df.head())
#
# # ============================================
# # STEP 2: DATA PREPROCESSING
# # ============================================
# print("\n" + "=" * 80)
# print("STEP 2: DATA PREPROCESSING")
# print("=" * 80)
#
# # Check for missing values
# print("\nMissing Values:")
# print(df.isnull().sum())
#
# # Fill missing values
# df['Age'] = df['Age'].fillna(df['Age'].median())
# df['Fare'] = df['Fare'].fillna(df['Fare'].median())
# df['Cabin'] = df['Cabin'].fillna('Unknown')
# df['Name'] = df['Name'].fillna('Unknown')
#
# print("\nMissing values after cleaning:")
# print(df.isnull().sum())
#
# # ============================================
# # STEP 3: ENCODE CATEGORICAL VARIABLES
# # ============================================
# print("\n" + "=" * 80)
# print("STEP 3: ENCODING CATEGORICAL VARIABLES")
# print("=" * 80)
#
# # Create a copy for encoding
# df_encoded = df.copy()
#
# # Encode Gender (male=1, female=0)
# df_encoded['Gender_encoded'] = (df_encoded['Gender'] == 'male').astype(int)
#
# # Encode Result (Embarkation - S, C, Q)
# le = LabelEncoder()
# df_encoded['Result_encoded'] = le.fit_transform(df_encoded['Result'].astype(str))
#
#
# # Encode Name (extract title and encode)
# def extract_title(name):
#     try:
#         if isinstance(name, str) and ',' in name:
#             title = name.split(',')[1].split('.')[0].strip()
#             return title
#         else:
#             return 'Unknown'
#     except:
#         return 'Unknown'
#
#
# df_encoded['Title'] = df_encoded['Name'].apply(extract_title)
# le_name = LabelEncoder()
# df_encoded['Name_encoded'] = le_name.fit_transform(df_encoded['Title'])
#
# # Encode Ticket
# le_ticket = LabelEncoder()
# df_encoded['Ticket_encoded'] = le_ticket.fit_transform(df_encoded['Ticket'].astype(str))
#
# # Encode Cabin
# le_cabin = LabelEncoder()
# df_encoded['Cabin_encoded'] = le_cabin.fit_transform(df_encoded['Cabin'].astype(str))
#
# print("\nEncoded columns created:")
# print(f"  - Gender_encoded: 0=Female, 1=Male")
# print(f"  - Result_encoded: {dict(enumerate(le.classes_))}")
# print(f"  - Name_encoded: Encoded titles")
# print(f"  - Ticket_encoded: Encoded tickets")
# print(f"  - Cabin_encoded: Encoded cabins")
#
# # ============================================
# # STEP 4: CALCULATE ALL REQUESTED CORRELATIONS
# # ============================================
# print("\n" + "=" * 80)
# print("STEP 4: CALCULATING CORRELATIONS WITH RESULT")
# print("=" * 80)
#
#
# # Function to calculate Cramer's V for categorical variables
# def cramers_v(confusion_matrix):
#     """Calculate Cramer's V statistic for categorical variables"""
#     try:
#         chi2 = chi2_contingency(confusion_matrix)[0]
#         n = confusion_matrix.sum().sum()
#         phi2 = chi2 / n
#         r, k = confusion_matrix.shape
#         phi2corr = max(0, phi2 - ((k - 1) * (r - 1)) / (n - 1))
#         rcorr = r - ((r - 1) ** 2) / (n - 1)
#         kcorr = k - ((k - 1) ** 2) / (n - 1)
#         return np.sqrt(phi2corr / min((kcorr - 1), (rcorr - 1)))
#     except:
#         return np.nan
#
#
# # Create a dictionary to store all correlations
# correlations = {}
#
# # 1. PassengerId & Result
# print("\n1. Correlation between PassengerId and Result:")
# corr_val = df_encoded['PassengerId'].corr(df_encoded['Result_encoded'])
# print(f"   Pearson Correlation: {corr_val:.6f}")
# correlations['PassengerId vs Result'] = corr_val
#
# # 2. Survived & Result
# print("\n2. Correlation between Survived and Result:")
# corr_val = df_encoded['Survived'].corr(df_encoded['Result_encoded'])
# print(f"   Pearson Correlation: {corr_val:.6f}")
# correlations['Survived vs Result'] = corr_val
#
# # 3. Pclass & Result
# print("\n3. Correlation between Pclass and Result:")
# corr_val = df_encoded['Pclass'].corr(df_encoded['Result_encoded'])
# print(f"   Pearson Correlation: {corr_val:.6f}")
# correlations['Pclass vs Result'] = corr_val
#
# # 4. Name & Result
# print("\n4. Correlation between Name and Result:")
# corr_val = df_encoded['Name_encoded'].corr(df_encoded['Result_encoded'])
# print(f"   Pearson Correlation: {corr_val:.6f}")
# correlations['Name vs Result'] = corr_val
#
# # 5. Gender & Result (using Cramer's V since both are categorical)
# print("\n5. Correlation between Gender and Result:")
# contingency_table = pd.crosstab(df['Gender'], df['Result'])
# cramers_v_val = cramers_v(contingency_table)
# print(f"   Cramer's V: {cramers_v_val:.6f}")
# print(f"   Chi-square p-value: {chi2_contingency(contingency_table)[1]:.6f}")
# correlations['Gender vs Result'] = cramers_v_val
#
# # 6. Age & Result
# print("\n6. Correlation between Age and Result:")
# corr_val = df_encoded['Age'].corr(df_encoded['Result_encoded'])
# print(f"   Pearson Correlation: {corr_val:.6f}")
# correlations['Age vs Result'] = corr_val
#
# # 7. SibSp & Result
# print("\n7. Correlation between SibSp and Result:")
# corr_val = df_encoded['SibSp'].corr(df_encoded['Result_encoded'])
# print(f"   Pearson Correlation: {corr_val:.6f}")
# correlations['SibSp vs Result'] = corr_val
#
# # 8. Parch & Result
# print("\n8. Correlation between Parch and Result:")
# corr_val = df_encoded['Parch'].corr(df_encoded['Result_encoded'])
# print(f"   Pearson Correlation: {corr_val:.6f}")
# correlations['Parch vs Result'] = corr_val
#
# # 9. Ticket & Result
# print("\n9. Correlation between Ticket and Result:")
# corr_val = df_encoded['Ticket_encoded'].corr(df_encoded['Result_encoded'])
# print(f"   Pearson Correlation: {corr_val:.6f}")
# correlations['Ticket vs Result'] = corr_val
#
# # 10. Fare & Result
# print("\n10. Correlation between Fare and Result:")
# corr_val = df_encoded['Fare'].corr(df_encoded['Result_encoded'])
# print(f"   Pearson Correlation: {corr_val:.6f}")
# correlations['Fare vs Result'] = corr_val
#
# # 11. Cabin & Result
# print("\n11. Correlation between Cabin and Result:")
# corr_val = df_encoded['Cabin_encoded'].corr(df_encoded['Result_encoded'])
# print(f"   Pearson Correlation: {corr_val:.6f}")
# correlations['Cabin vs Result'] = corr_val
#
# # 12. Result & Result (Self-correlation)
# print("\n12. Correlation between Result and Result:")
# print(f"   Pearson Correlation: 1.000000")
# correlations['Result vs Result'] = 1.0
#
# # ============================================
# # STEP 5: CREATE SUMMARY TABLE
# # ============================================
# print("\n" + "=" * 80)
# print("STEP 5: SUMMARY TABLE OF ALL CORRELATIONS")
# print("=" * 80)
#
# # Create a summary DataFrame
# summary_data = []
# for pair, value in correlations.items():
#     # Determine strength
#     if abs(value) > 0.5:
#         strength = 'Strong'
#     elif abs(value) > 0.3:
#         strength = 'Moderate'
#     elif abs(value) > 0.1:
#         strength = 'Weak'
#     else:
#         strength = 'Very Weak'
#
#     # Determine direction
#     direction = 'Positive' if value > 0 else 'Negative' if value < 0 else 'Zero'
#
#     summary_data.append({
#         'Variables': pair,
#         'Correlation': value,
#         'Direction': direction,
#         'Strength': strength
#     })
#
# summary_df = pd.DataFrame(summary_data)
# print("\n" + summary_df.to_string(index=False))
#
# # ============================================
# # STEP 6: VISUALIZE CORRELATIONS
# # ============================================
# print("\n" + "=" * 80)
# print("STEP 6: VISUALIZING CORRELATIONS")
# print("=" * 80)
#
# # Create a bar plot of all correlations
# plt.figure(figsize=(12, 8))
# variables = list(correlations.keys())
# values = list(correlations.values())
#
# # Create color map: red for negative, green for positive
# colors = ['red' if v < 0 else 'green' if v > 0 else 'gray' for v in values]
#
# # Sort by correlation value
# sorted_data = sorted(zip(variables, values, colors), key=lambda x: x[1])
# variables_sorted = [x[0] for x in sorted_data]
# values_sorted = [x[1] for x in sorted_data]
# colors_sorted = [x[2] for x in sorted_data]
#
# bars = plt.barh(variables_sorted, values_sorted, color=colors_sorted)
# plt.xlabel('Correlation Coefficient')
# plt.title('Correlations with Result (Embarkation - S, C, Q)')
# plt.axvline(x=0, color='black', linestyle='-', linewidth=0.5)
# plt.axvline(x=0.3, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
# plt.axvline(x=-0.3, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
# plt.grid(axis='x', alpha=0.3)
# plt.tight_layout()
# plt.savefig('all_correlations_with_result.png', dpi=300, bbox_inches='tight')
# plt.show()
#
# # ============================================
# # STEP 7: CREATE CORRELATION HEATMAP
# # ============================================
# print("\n" + "=" * 80)
# print("STEP 7: CREATING CORRELATION HEATMAP")
# print("=" * 80)
#
# # Select columns for heatmap
# heatmap_cols = ['PassengerId', 'Survived', 'Pclass', 'Name_encoded', 'Gender_encoded',
#                 'Age', 'SibSp', 'Parch', 'Ticket_encoded', 'Fare', 'Cabin_encoded', 'Result_encoded']
#
# # Calculate correlation matrix
# corr_matrix = df_encoded[heatmap_cols].corr()
#
# # Rename columns for better display
# rename_dict = {
#     'PassengerId': 'Passenger ID',
#     'Survived': 'Survived',
#     'Pclass': 'Pclass',
#     'Name_encoded': 'Name',
#     'Gender_encoded': 'Gender',
#     'Age': 'Age',
#     'SibSp': 'SibSp',
#     'Parch': 'Parch',
#     'Ticket_encoded': 'Ticket',
#     'Fare': 'Fare',
#     'Cabin_encoded': 'Cabin',
#     'Result_encoded': 'Result'
# }
# corr_matrix = corr_matrix.rename(columns=rename_dict, index=rename_dict)
#
# # Create heatmap
# plt.figure(figsize=(12, 10))
# sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0,
#             fmt='.3f', square=True, linewidths=0.5,
#             cbar_kws={"shrink": 0.8})
# plt.title('Correlation Matrix of Titanic Dataset', fontsize=16)
# plt.tight_layout()
# plt.savefig('correlation_heatmap.png', dpi=300, bbox_inches='tight')
# plt.show()
#
# # ============================================
# # STEP 8: KEY INSIGHTS
# # ============================================
# print("\n" + "=" * 80)
# print("STEP 8: KEY INSIGHTS")
# print("=" * 80)
#
# # Find strongest correlations
# correlations_no_self = {k: v for k, v in correlations.items() if k != 'Result vs Result'}
# strongest_corr = max(correlations_no_self.items(), key=lambda x: abs(x[1]))
# weakest_corr = min(correlations_no_self.items(), key=lambda x: abs(x[1]))
#
# print(f"\nStrongest correlation with Result:")
# print(f"  - {strongest_corr[0]}: {strongest_corr[1]:.6f}")
#
# print(f"\nWeakest correlation with Result:")
# print(f"  - {weakest_corr[0]}: {weakest_corr[1]:.6f}")
#
# # Sort correlations by absolute value
# sorted_corrs = sorted(correlations_no_self.items(), key=lambda x: abs(x[1]), reverse=True)
# print("\nAll correlations sorted by strength:")
# for i, (pair, value) in enumerate(sorted_corrs, 1):
#     print(f"  {i}. {pair}: {value:.6f}")
#
# # ============================================
# # STEP 9: SAVE RESULTS TO CSV
# # ============================================
# print("\n" + "=" * 80)
# print("STEP 9: SAVING RESULTS")
# print("=" * 80)
#
# # Save summary table to CSV
# summary_df.to_csv('correlation_summary.csv', index=False)
# print("Summary table saved to 'correlation_summary.csv'")
#
# # Save correlation matrix to CSV
# corr_matrix.to_csv('correlation_matrix.csv')
# print("Correlation matrix saved to 'correlation_matrix.csv'")
#
# print("\n" + "=" * 80)
# print("ANALYSIS COMPLETE!")
# print("=" * 80)






























import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency, pearsonr
from sklearn.preprocessing import LabelEncoder
import warnings

warnings.filterwarnings('ignore')

# ============================================
# LOAD AND ENCODE DATA
# ============================================
df = pd.read_csv('titanic_dataset.csv')

# Encode categorical variables
df_encoded = df.copy()
df_encoded['Gender_encoded'] = (df_encoded['Gender'] == 'male').astype(int)

le = LabelEncoder()
df_encoded['Result_encoded'] = le.fit_transform(df_encoded['Result'].astype(str))


def extract_title(name):
    try:
        if isinstance(name, str) and ',' in name:
            return name.split(',')[1].split('.')[0].strip()
        return 'Unknown'
    except:
        return 'Unknown'


df_encoded['Title'] = df_encoded['Name'].apply(extract_title)
df_encoded['Name_encoded'] = LabelEncoder().fit_transform(df_encoded['Title'])
df_encoded['Ticket_encoded'] = LabelEncoder().fit_transform(df_encoded['Ticket'].astype(str))
df_encoded['Cabin_encoded'] = LabelEncoder().fit_transform(df_encoded['Cabin'].astype(str))


# Function for Cramer's V
def cramers_v(confusion_matrix):
    try:
        chi2 = chi2_contingency(confusion_matrix)[0]
        n = confusion_matrix.sum().sum()
        phi2 = chi2 / n
        r, k = confusion_matrix.shape
        phi2corr = max(0, phi2 - ((k - 1) * (r - 1)) / (n - 1))
        rcorr = r - ((r - 1) ** 2) / (n - 1)
        kcorr = k - ((k - 1) ** 2) / (n - 1)
        return np.sqrt(phi2corr / min((kcorr - 1), (rcorr - 1)))
    except:
        return np.nan


# ============================================
# CALCULATE CORRELATIONS
# ============================================
print("\n" + "=" * 80)
print("CORRELATION ANALYSIS: Titanic Dataset")
print("=" * 80)

correlations = {}
p_values = {}

# Define pairs to analyze
pairs = [
    ('PassengerId', 'PassengerId'),
    ('Survived', 'Survived'),
    ('Pclass', 'Pclass'),
    ('Name', 'Name_encoded'),
    ('Gender', 'Gender'),  # Will use Cramer's V
    ('Age', 'Age'),
    ('SibSp', 'SibSp'),
    ('Parch', 'Parch'),
    ('Ticket', 'Ticket_encoded'),
    ('Fare', 'Fare'),
    ('Cabin', 'Cabin_encoded'),
    ('Result', 'Result')  # Self-correlation
]

print("\n{:<20} {:>15} {:>12} {:>12}".format('Variable', 'Correlation', 'P-value', 'Strength'))
print("-" * 65)

for display_name, col_name in pairs:
    if display_name == 'Result' and col_name == 'Result':
        corr = 1.0
        p = 0.0
    elif display_name == 'Gender':
        contingency_table = pd.crosstab(df['Gender'], df['Result'])
        corr = cramers_v(contingency_table)
        chi2, p, dof, expected = chi2_contingency(contingency_table)
    else:
        corr, p = pearsonr(df_encoded[col_name], df_encoded['Result_encoded'])

    # Determine strength
    if abs(corr) > 0.5:
        strength = 'Strong'
    elif abs(corr) > 0.3:
        strength = 'Moderate'
    elif abs(corr) > 0.1:
        strength = 'Weak'
    else:
        strength = 'Very Weak'

    correlations[display_name] = corr
    p_values[display_name] = p

    # Print neatly formatted
    print("{:<20} {:>15.6f} {:>12.6f} {:>12}".format(
        display_name, corr, p, strength))

print("=" * 80)

# ============================================
# SCATTER PLOTS FOR NUMERICAL VARIABLES
# ============================================
print("\nGenerating scatter plots...")

# Numerical variables for scatter plots
scatter_vars = ['PassengerId', 'Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare']

fig, axes = plt.subplots(2, 4, figsize=(16, 8))
axes = axes.flatten()

for idx, var in enumerate(scatter_vars):
    if idx < len(axes):
        ax = axes[idx]
        ax.scatter(df_encoded[var], df_encoded['Result_encoded'], alpha=0.5, s=20, c='steelblue')
        ax.set_xlabel(var, fontsize=10)
        ax.set_ylabel('Result (Encoded)', fontsize=10)
        corr = correlations.get(var, 0)
        ax.set_title(f'{var} vs Result\nr = {corr:.4f}', fontsize=10)
        ax.grid(True, alpha=0.3)

# Hide empty subplot
axes[-1].set_visible(False)

plt.suptitle('Scatter Plots: Numerical Variables vs Result', fontsize=14, y=1.02)
plt.tight_layout()
plt.savefig('scatter_plots.png', dpi=300, bbox_inches='tight')
plt.show()

# ============================================
# BOX PLOTS FOR CATEGORICAL VARIABLES
# ============================================
print("\nGenerating box plots for categorical variables...")

categorical_vars = ['Gender', 'Title', 'Ticket', 'Cabin']

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
axes = axes.flatten()

for idx, var in enumerate(categorical_vars):
    if idx < len(axes):
        ax = axes[idx]

        # Prepare data
        if var == 'Title':
            data_to_plot = df_encoded['Title']
        else:
            data_to_plot = df_encoded[var]

        # Create box plot
        plot_data = []
        labels = []
        for category in data_to_plot.unique():
            if pd.notna(category):
                values = df_encoded[df_encoded[var if var != 'Title' else 'Title'] == category]['Result_encoded']
                if len(values) > 5:  # Only show categories with enough data
                    plot_data.append(values)
                    labels.append(str(category)[:15])  # Truncate long labels

        if plot_data:
            bp = ax.boxplot(plot_data, labels=labels, patch_artist=True)
            ax.set_title(f'{var} vs Result', fontsize=12)
            ax.set_xlabel(var, fontsize=10)
            ax.set_ylabel('Result (Encoded)', fontsize=10)
            ax.tick_params(axis='x', rotation=45, labelsize=8)
            ax.grid(True, alpha=0.3)

plt.suptitle('Box Plots: Categorical Variables vs Result', fontsize=14, y=1.02)
plt.tight_layout()
plt.savefig('box_plots.png', dpi=300, bbox_inches='tight')
plt.show()

# ============================================
# CORRELATION BAR CHART
# ============================================
print("\nGenerating correlation bar chart...")

# Remove self-correlation for better visualization
plot_data = {k: v for k, v in correlations.items() if k != 'Result'}

plt.figure(figsize=(12, 7))
variables = list(plot_data.keys())
values = list(plot_data.values())

# Colors: red for negative, green for positive
colors = ['red' if v < 0 else 'green' if v > 0 else 'gray' for v in values]

# Sort by correlation value
sorted_data = sorted(zip(variables, values, colors), key=lambda x: x[1])
vars_sorted = [x[0] for x in sorted_data]
vals_sorted = [x[1] for x in sorted_data]
cols_sorted = [x[2] for x in sorted_data]

bars = plt.barh(vars_sorted, vals_sorted, color=cols_sorted, height=0.6)
plt.xlabel('Correlation Coefficient', fontsize=12)
plt.title('Correlations with Result (Embarkation - S, C, Q)', fontsize=14)
plt.axvline(x=0, color='black', linestyle='-', linewidth=0.5)
plt.axvline(x=0.3, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
plt.axvline(x=-0.3, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
plt.grid(axis='x', alpha=0.3)

# Add correlation values on bars
for i, (var, val) in enumerate(zip(vars_sorted, vals_sorted)):
    plt.text(val + 0.01 if val >= 0 else val - 0.01, i,
             f'{val:.4f}', va='center', fontsize=9)

plt.tight_layout()
plt.savefig('correlation_bar_chart.png', dpi=300, bbox_inches='tight')
plt.show()

# ============================================
# HEATMAP
# ============================================
print("\nGenerating correlation heatmap...")

# Select columns for heatmap
heatmap_cols = ['PassengerId', 'Survived', 'Pclass', 'Name_encoded', 'Gender_encoded',
                'Age', 'SibSp', 'Parch', 'Ticket_encoded', 'Fare', 'Cabin_encoded', 'Result_encoded']

# Calculate correlation matrix
corr_matrix = df_encoded[heatmap_cols].corr()

# Rename for better display
rename_dict = {
    'PassengerId': 'PassID',
    'Survived': 'Surv',
    'Pclass': 'Pclass',
    'Name_encoded': 'Name',
    'Gender_encoded': 'Gender',
    'Age': 'Age',
    'SibSp': 'SibSp',
    'Parch': 'Parch',
    'Ticket_encoded': 'Ticket',
    'Fare': 'Fare',
    'Cabin_encoded': 'Cabin',
    'Result_encoded': 'Result'
}
corr_matrix = corr_matrix.rename(columns=rename_dict, index=rename_dict)

plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0,
            fmt='.3f', square=True, linewidths=0.5,
            cbar_kws={"shrink": 0.8})
plt.title('Correlation Matrix', fontsize=14)
plt.tight_layout()
plt.savefig('correlation_heatmap.png', dpi=300, bbox_inches='tight')
plt.show()

# ============================================
# SAVE RESULTS
# ============================================
# Create summary DataFrame
summary_data = []
for var, corr in correlations.items():
    if abs(corr) > 0.5:
        strength = 'Strong'
    elif abs(corr) > 0.3:
        strength = 'Moderate'
    elif abs(corr) > 0.1:
        strength = 'Weak'
    else:
        strength = 'Very Weak'

    summary_data.append({
        'Variable': var,
        'Correlation': round(corr, 6),
        'P-value': round(p_values.get(var, 0), 6),
        'Strength': strength
    })

summary_df = pd.DataFrame(summary_data)
summary_df.to_csv('correlation_results.csv', index=False)

print("\n" + "=" * 80)
print("RESULTS SAVED")
print("=" * 80)
print("✓ correlation_results.csv - Full correlation table")
print("✓ scatter_plots.png - Scatter plots for numerical variables")
print("✓ box_plots.png - Box plots for categorical variables")
print("✓ correlation_bar_chart.png - Correlation bar chart")
print("✓ correlation_heatmap.png - Correlation heatmap")

# Final summary
print("\n" + "=" * 80)
print("FINAL SUMMARY")
print("=" * 80)
print("\n{:<20} {:>15} {:>12}".format('Variable', 'Correlation', 'Strength'))
print("-" * 50)

# Show only top variables (exclude Result self-correlation)
for var, corr in correlations.items():
    if var != 'Result':
        strength = 'Strong' if abs(corr) > 0.5 else 'Moderate' if abs(corr) > 0.3 else 'Weak' if abs(
            corr) > 0.1 else 'Very Weak'
        print("{:<20} {:>15.6f} {:>12}".format(var, corr, strength))

print("=" * 80)
print("Analysis Complete!")



