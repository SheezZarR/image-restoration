import Work_with_matrix as my


# Просто формула W+ = Wt(WWt)^-1
def WWplus(W) -> list:
    Wt = my.transposion(W)
    # m > n
    if len(W[0]) < len(W):
        Wplus = my.matrix_multiply(Wt, W)
        Wplus = my.opposite(Wplus)
        Wplus = my.matrix_multiply(Wplus, Wt)
    else: # n > m
        Wplus = my.matrix_multiply(W, Wt)
        Wplus = my.opposite(Wplus)
        Wplus = my.matrix_multiply(Wt, Wplus)
    return Wplus

A = [[2, 1, 1, 3], [1, 0, 1, -1]]
#B = my.opposite(A)
#print(B)
print(WWplus(A))
#print(my.matrix_multiply(A, B))