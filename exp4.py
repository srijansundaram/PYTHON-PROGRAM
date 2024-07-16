import numpy as np
from scipy.stats.contingency import margins

# Joint probability table
join_probability_X_Y = np.array([
                [4/36, 3/36, 2/36, 1/36],
                [1/36, 3/36, 3/36, 2/36],
                [5/36, 1/36, 1/36, 1/36],
                [1/36, 2/36, 1/36, 5/36]
            ])

x, y = margins(join_probability_X_Y)

print("Marginal distribution of X:")
print(x)

print("Marginal distribution of Y:")
print(y)