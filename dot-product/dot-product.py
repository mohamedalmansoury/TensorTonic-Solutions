import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    x = np.asarray(x , dtype = np.float64)
    y = np.asarray(y , dtype = np.float64)
    dot = np.dot(x, y)

    return dot
