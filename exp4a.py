import numpy as np

# Define the probability distribution of a random variable
prob_dist = np.array([0.18, 0.34, 0.35, 0.11, 0.02])

# Define the values of the random variable
x_values = np.array([0, 1, 2, 3, 4])

# Calculate the expected value of the random variable
expected_value = np.sum(x_values * prob_dist)

# Print the result
print("Expected value of the random variable:", expected_value)