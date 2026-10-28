import numpy as np

# Set seed for reproducible results
np.random.seed(42)

# Generate random numbers between 0 and 1
random_values = np.random.rand(5)
print("Random Values:", random_values)

# Generate normally distributed standard random numbers
normal_values = np.random.randn(5)
print("Standard Normal Values:", normal_values)

# Generate random integers
integers = np.random.randint(1, 101, size=10)
print("Random Integers:", integers)

# Generate values from a normal distribution
normal_distribution = np.random.normal(
    loc=50, scale=10, size=1000
)
print("First 10 Normal Values:", normal_distribution[:10])

# Calculate statistics
print("Mean:", np.mean(normal_distribution))
print("Median:", np.median(normal_distribution))
print("Standard Deviation:", np.std(normal_distribution))
print("Minimum:", np.min(normal_distribution))
print("Maximum:", np.max(normal_distribution))
print("Variance:", np.var(normal_distribution))
