"""Some handy math tools"""

import numpy as np
from scipy import derivative

def diff(f, x, i, n=1, eps=0.01, n_points=3):
    """Takes the i-th derivative of a multi-dimmensional function
    """
    def func_for_diff(x_i):
        return f(np.concatenate((x[:i],[x_i],x[i+1:])))

    x = np.atleast_1d(x)

    return derivative(func=func_for_diff, x0=x[i], dx=eps, n=n, order=n_points)

def diff2(f, x, i, j, eps=0.01, n_points=5):
    """Takes the second derivative with respect to function parameters
    i and j of a multi-dimensional function"""
    x = np.atleast_1d(x)

    if i == j:
        return diff(f, x, i, 2, eps, n_points)
    else:
        return diff(lambda z: diff(f, z, i, 1, eps, n_points),\
                    x, j, 1, eps, n_points)

def grad(f, x, eps=0.01, n_points=3):
    x = np.atleast_1d(x)
    g = np.zeros_like(x)
    for i in range(len(x)):
        g[i] = diff(f, x, i, 1, eps, n_points)
    return g

def hess(f, x, eps=0.01, n_points=5):
    x = np.atleast_1d(x)
    d = len(x)
    h = np.zeros((d,d))
    for i in range(d):
        h[i,i] = diff2(f, x, i, i, eps, n_points)
        for j in range(i):
            h[i,j] = diff2(f, x, i, j, eps, n_points)
            h[j,i] = h[i,j]
    return h

def shrink_matrix(matrix, factor=0.2):
    """
    Shrinks a matrix towards the identity matrix while maintaining the
    frobenious matrix norm.
    """
    if matrix.ndim != 2:
        raise ValueError("shrink_matrix requires a 2d-numpy array!")
    n = matrix.shape[0]
    if n != matrix.shape[1]:
        raise ValueError("shrink_matrix requires a square matrix!")

    l = 1.0-factor
    return l*matrix\
        + np.sqrt((1.0-l**2)/n)*np.linalg.norm(matrix)*np.eye(n)

