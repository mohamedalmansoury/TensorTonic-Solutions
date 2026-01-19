import numpy as np
import math

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    x = np.asarray(x)
    y = np.asarray(y)

    x = x.ravel()
    y = y.ravel()

    if x.size != y.size:
        raise ValueError("Vectors must have the same length")

    sum_sq = 0.0
    for i in range(x.size):
        diff = float(x[i]) - float(y[i])
        sum_sq += diff * diff

    return float(math.sqrt(sum_sq))
