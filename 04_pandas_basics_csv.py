import pandas as pd

# Create a Series
marks = pd.Series([85, 90, 78, 92, 88])
print("Pandas Series:")
print(marks)

# Create a DataFrame
data = {
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Rohan"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [85, 90, 78, 92, 88]
}

df = pd.DataFrame(data)

print("\nDataFrame:")
print(df)

# Display first and last rows
print("\nFirst Five Rows:")
print(df.head())

print("\nLast Three Rows:")
print(df.tail(3))

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Basic operations
print("\nColumn Names:", df.columns.tolist())
print("\nNames Column:")
print(df["Name"])

print("\nStudents with Marks Above 85:")
print(df[df["Marks"] > 85])

# Export DataFrame to CSV
df.to_csv("students.csv", index=False)
print("\nData exported to students.csv")

# Import CSV file
df_imported = pd.read_csv("students.csv")
print("\nImported CSV Data:")
print(df_imported)
