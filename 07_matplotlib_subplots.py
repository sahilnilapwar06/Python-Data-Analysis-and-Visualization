import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 4, 9, 16, 25]

# Create a figure with four subplots
plt.figure(figsize=(12, 8))

# Subplot 1: Line plot
plt.subplot(2, 2, 1)
plt.plot(x, y1, marker="o", label="Linear")
plt.title("Line Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)

# Subplot 2: Bar plot
plt.subplot(2, 2, 2)
plt.bar(x, y2, label="Square Values")
plt.title("Bar Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(axis="y")

# Subplot 3: Scatter plot
plt.subplot(2, 2, 3)
plt.scatter(x, y2, label="Data Points")
plt.title("Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)

# Subplot 4: Histogram
plt.subplot(2, 2, 4)
plt.hist(y2, bins=5, edgecolor="black", label="Values")
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.legend()
plt.grid(axis="y")

plt.suptitle("Multiple Matplotlib Plots")
plt.tight_layout()
plt.show()
