import matplotlib.pyplot as plt

# Sample data
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [120, 150, 100, 180, 220]

# Line plot
plt.figure(figsize=(7, 4))
plt.plot(months, sales, marker="o", label="Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales - Line Plot")
plt.legend()
plt.grid(True)
plt.show()

# Bar plot
plt.figure(figsize=(7, 4))
plt.bar(months, sales, label="Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales - Bar Plot")
plt.legend()
plt.show()

# Scatter plot
advertising = [10, 20, 30, 40, 50]
revenue = [25, 40, 45, 60, 75]

plt.figure(figsize=(7, 4))
plt.scatter(advertising, revenue, label="Data Points")
plt.xlabel("Advertising Cost")
plt.ylabel("Revenue")
plt.title("Advertising vs Revenue - Scatter Plot")
plt.legend()
plt.grid(True)
plt.show()

# Histogram
marks = [45, 55, 60, 65, 70, 72, 75, 80, 85, 90, 92, 95]

plt.figure(figsize=(7, 4))
plt.hist(marks, bins=5, edgecolor="black", label="Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Marks Distribution - Histogram")
plt.legend()
plt.show()
