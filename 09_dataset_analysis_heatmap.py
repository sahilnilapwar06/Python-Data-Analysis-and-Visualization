import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load a real-world dataset
df = sns.load_dataset("iris")

# Display the dataset
print("First Five Rows:")
print(df.head())

print("\nLast Five Rows:")
print(df.tail())

# Dataset information
print("\nDataset Information:")
df.info()

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing numeric values if any exist
numeric_columns = df.select_dtypes(include="number").columns
df[numeric_columns] = df[numeric_columns].fillna(
    df[numeric_columns].mean()
)

# Correlation matrix
correlation = df[numeric_columns].corr()

print("\nCorrelation Matrix:")
print(correlation)

# Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
plt.title("Iris Dataset - Correlation Heatmap")
plt.tight_layout()
plt.show()

# Pairwise visual analysis
sns.pairplot(df, hue="species")
plt.show()

# Average measurements by species
print("\nAverage Measurements by Species:")
print(df.groupby("species")[numeric_columns].mean())
