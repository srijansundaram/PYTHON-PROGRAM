import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# Setting the values of n and p
n = 6
p = 0.6

# Defining the list of r values
r_values = np.arange(n + 1)

# Obtaining the mean and variance
mean, var = binom.stats(n, p)

# List of PMF values
dist = [binom.pmf(r, n, p) for r in r_values]

# Printing the table
print("r\tp(r)")
for i in range(n + 1):
    print(f"{r_values[i]}\t{dist[i]:.4f}")

# Plotting the histogram
plt.bar(r_values, dist, align='center')
plt.xlabel('r')
plt.ylabel('p(r)')
plt.title(f'Binomial Distribution for n={n}, p={p}')
plt.show()