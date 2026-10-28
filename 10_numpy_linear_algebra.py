import numpy as np

# Define a coefficient matrix
A = np.array([
    [2, 1],
    [1, 3]
])

# Define constants for the equations:
# 2x + y = 8
# x + 3y = 13
B = np.array([8, 13])

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

# Solve the matrix equation AX = B
solution = np.linalg.solve(A, B)

print("\nSolution [x, y]:")
print(solution)

# Find the inverse
inverse = np.linalg.inv(A)

print("\nInverse of A:")
print(inverse)

# Find the transpose
transpose = A.T

print("\nTranspose of A:")
print(transpose)

# Find eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print("\nEigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)

# Verify the inverse
print("\nA multiplied by its inverse:")
print(A @ inverse)
