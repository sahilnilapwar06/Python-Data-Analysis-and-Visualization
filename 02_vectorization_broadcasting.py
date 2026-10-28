import numpy as np

# Vectorized operations
a = np.array([1, 4, 9, 16, 25])
b = np.array([10, 20, 30, 40, 50])

print("Array A:", a)
print("Array B:", b)

print("Addition:", np.add(a, b))
print("Square Root:", np.sqrt(a))
print("Exponential:", np.exp(a))

# Broadcasting: add a scalar to every element
print("Scalar Broadcasting:", a + 5)

# Broadcasting between a 2D array and a 1D array
matrix = np.array([[1, 2, 3], [4, 5, 6]])
vector = np.array([10, 20, 30])

print("Matrix:\n", matrix)
print("Vector:", vector)
print("Broadcasting Result:\n", matrix + vector)

# Broadcasting with column and row vectors
column = np.array([[1], [2], [3]])
row = np.array([10, 20, 30])

print("Column + Row:\n", column + row)
