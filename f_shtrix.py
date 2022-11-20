import numpy as np
def f_shtrix(W, g):
    f_sh = W.dot(g)
    return f_sh
"""W = np.matrix([ [2, 1], [2, 2], [4, 3] ])
g = np.matrix([ [1], [3] ])
print(f_shtrix(W,g))"""
