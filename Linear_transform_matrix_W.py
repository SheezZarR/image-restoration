import numpy as np


def W_matrix(g_len: int, f_len: int) -> np.matrix:
    """
    W matrix linear transformation
    :param g_len: Length of array g(restoration img)
    :param f_len: Length of array f(restored img)
    :return: Linear transform matrix (numpy.matrix)
    """
    m, n = g_len, f_len
    N = 1  # num samples

    rng = np.random.RandomState(42)

    W = rng.randn(m, n)
    X = rng.randn(n, N)
    Z_clean = W.dot(X)

    W_est = np.linalg.pinv(X.T).dot(Z_clean.T).T
    return W_est