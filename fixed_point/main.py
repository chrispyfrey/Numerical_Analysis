import numpy as np

def g(x):
    return np.log(7-x)

tol = 10**-8
max_iter = 1000
x0, j = 0, 0

vals = np.zeros(max_iter + 1)
vals[0] = x0

for i in range(max_iter):
    j = i+1
    vals[j] = g(vals[i])

    if np.abs(vals[j] - vals[i]) < tol:
        break

# Truncates root value from 9 decimal places to 8 without rounding
rt_str = '{:.9f}'.format(vals[j])[:-1]
print(rt_str)