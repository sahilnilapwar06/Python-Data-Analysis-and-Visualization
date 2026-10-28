import pandas as pd
import numpy as np

# Create a DataFrame with missing values
data = {
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Rohan", "Neha"],
    "Department": ["IT", "CS", "IT", "CS", "IT", "CS"],
    "Marks": [85, np.nan, 78, 92, np.nan, 88],
    "Age": [20, 21, 19, 22, 20, 21]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Detect missing values
print("\nMissing Values:")
print(df.isnull())

print("\nMissing Value Count:")
print(df.isnull().sum())

# Fill missing values in Marks with the mean
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
print("\nAfter Filling Missing Values:")
print(df)

# Demonstrate dropna on a separate copy
df_with_missing = pd.DataFrame(data)
df_dropped = df_with_missing.dropna()
print("\nRows After dropna():")
print(df_dropped)

# Filter rows
print("\nStudents with Marks Above 85:")
print(df[df["Marks"] > 85])

# Select columns
print("\nSelected Columns:")
print(df[["Name", "Marks"]])

# Sort values
print("\nSorted by Marks:")
print(df.sort_values(by="Marks", ascending=False))

# Group by department
print("\nDepartment-wise Average Marks:")
print(df.groupby("Department")["Marks"].mean())

print("\nDepartment-wise Student Count:")
print(df.groupby("Department")["Name"].count())
