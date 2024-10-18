#  data
x = [16, 27, 11, 20, 30, 25, 5, 24, 21, 10]
y = [46, 80, 36, 52, 98, 75, 10, 70, 64, 30]

n = len(x)

# Mean
mean_x = sum(x) / n
mean_y = sum(y) / n

# Variance
variance_x = sum((xi - mean_x) ** 2 for xi in x) / (n - 1)
variance_y = sum((yi - mean_y) ** 2 for yi in y) / (n - 1)

# Covariance
covariance_xy = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n)) / (n - 1)

# Correlation
correlation_xy = covariance_xy / (variance_x ** 0.5 * variance_y ** 0.5)

# Print results
print(f"Mean of x: {mean_x}")
print(f"Mean of y: {mean_y}")
print(f"Variance of x: {variance_x}")
print(f"Variance of y: {variance_y}")
print(f"Covariance between x and y: {covariance_xy}")
print(f"Correlation between x and y: {correlation_xy}")
