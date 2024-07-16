import numpy as np

# Define the probability distribution of a random variable
chance = np.array([0.20, 0.50, 0.30])

# Define the values of the random variable
amount = np.array([200, 100, 50])

# Calculate the expected value of the random variable
expected_value = np.sum(amount * chance)

# Print the result
print("Expected return value in the investment:", expected_value)