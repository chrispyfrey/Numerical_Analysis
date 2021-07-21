import numpy as np

def guassian_elim(A, b):
    """
    Performs in-place Guassian elemination without pivoting.

    Params: A - n x n coefficient matrix.
            b - n length rhs of equation.

    Returns: None - A is not n x n 
                    b is not n length
                    Zero pivot is encountered
    """

    if A.shape[0] != A.shape[1] or A.shape[0] != b.size:
        return None

    eps = 1e-5
    n = A.shape[0]

    for j in range(n-1):
        if np.abs(A[j, j]) < eps:
            return None

        for i in range(j+1, n):
            mp = A[i, j] / A[j, j]

            for k in range(j+1, n):
                A[i, k] = A[i, k] - (mp * A[j, k])

            b[i] = b[i] - (mp * b[j])

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
#  2x + 1y - 4z = -7
#  1x - 1y + 1z = -2
# -1x + 3y - 2z =  6

A = np.array([[ 2.,  1., -4.], 
              [ 1., -1.,  1.], 
              [-1.,  3., -2.]])

b = np.array([-7., 
              -2., 
               6.])

guassian_elim(A, b)
back_sub(A, b)

print('x = {0:.2f}\ny = {1:.2f}\nz = {2:.2f}'.format(b[0], b[1], b[2]))
