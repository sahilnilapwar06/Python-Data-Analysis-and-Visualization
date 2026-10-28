import numpy as np

# Create a 1D array
arr1 = np.array([10, 20, 30, 40, 50])
print("1D Array:", arr1)

# Create arrays using arange and linspace
arr2 = np.arange(1, 11)
arr3 = np.linspace(0, 10, 5)

print("Arange Array:", arr2)
print("Linspace Array:", arr3)

# Indexing
print("First Element:", arr1[0])
print("Last Element:", arr1[-1])

# Slicing
print("First Three Elements:", arr1[:3])
print("Every Second Element:", arr1[::2])

# Create a 2D array
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("2D Array:\n", arr2d)

# 2D indexing and slicing
print("Element at Row 1, Column 2:", arr2d[0, 1])
print("First Row:", arr2d[0, :])
print("Second Column:", arr2d[:, 1])

# Reshaping
arr = np.arange(1, 13)
reshaped = np.reshape(arr, (3, 4))
print("Reshaped Array:\n", reshaped)

# Mathematical operations
print("Sum:", np.sum(arr1))
print("Mean:", np.mean(arr1))
print("Addition:", arr1 + 5)
print("Multiplication:", arr1 * 2)
