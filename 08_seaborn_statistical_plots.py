import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a sample DataFrame
df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [120, 150, 100, 180, 220, 200],
    "Profit": [20, 30, 15, 40, 50, 45],
    "Advertising": [10, 15, 8, 20, 25, 22]
})

sns.set_theme(style="whitegrid")

# Line plot
sns.lineplot(data=df, x="Month", y="Sales", marker="o")
plt.title("Monthly Sales - Seaborn Line Plot")
plt.show()

# Bar plot
sns.barplot(data=df, x="Month", y="Sales")
plt.title("Monthly Sales - Seaborn Bar Plot")
plt.show()

# Histogram
sns.histplot(data=df, x="Sales", bins=5, kde=True)
plt.title("Sales Distribution - Histogram")
plt.show()

# Box plot
sns.boxplot(data=df, y="Sales")
plt.title("Sales Distribution - Box Plot")
plt.show()

# Scatter plot
sns.scatterplot(
    data=df,
    x="Advertising",
    y="Sales",
    hue="Profit",
    s=100
)
plt.title("Advertising vs Sales")
plt.show()
