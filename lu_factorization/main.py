import numpy as np

def lu_factorization(A):
    """
    Performs in-place LU factorization without pivoting.

    Params: A - n x n coefficient matrix.

    Returns: None - A is not n x n
                    Zero pivot is encountered
    """

    if A.shape[0] != A.shape[1]:
        return None

    eps = 1e-5
    n = A.shape[0]

    for j in range(n-1):
        if np.abs(A[j, j]) < eps:
            return None

        for i in range(j+1, n):
            mp = A[i, j] / A[j, j]
            A[i, j] = mp

            for k in range(j+1, n):
                A[i, k] = A[i, k] - (mp * A[j, k])

def forward_sub(A, b):
    """
    Performs in-place forward substitution.

    Params: A - n x n LU factorized matrix.
            b - n length rhs of equation.

    Returns: None - A is not n x n 
                    b is not n length
    """

    if A.shape[0] != A.shape[1] or A.shape[0] != b.size:
        return None

    n = A.shape[0]

    for i in range(0, n):
        b[i+1:] = b[i+1:] - (b[i] * A[i+1:, i])


def back_sub(A, b):
    """
    Performs in-place backwards substitution.

    Params: A - n x n coefficient matrix.
            b - n length rhs of equation.

    Returns: None - A is not n x n 
                    b is not n length
    """
    if A.shape[0] != A.shape[1] or A.shape[0] != b.size:
        return None

    n = A.shape[0]

    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            b[i] = b[i] - (A[i, j] * b[j])
        
        b[i] = b[i] / A[i, i]

# Solve for:
# 4x1 + 2x2 + 0x3 = 2
# 4x1 + 4x2 + 2x3 = 4
# 2x1 + 2x2 + 3x3 = 6

A = np.array([[4., 2., 0.], 
              [4., 4., 2.],
              [2., 2., 3.]])
b = np.array([2., 
              4., 
              6.])

lu_factorization(A)
forward_sub(A, b)
back_sub(A, b)

print('x1 = {0:.2f}\nx2 = {1:.2f}\nx3 = {2:.2f}'.format(b[0], b[1], b[2]))
