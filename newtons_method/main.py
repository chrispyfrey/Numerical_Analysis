import numpy as np

def f(x):
    return np.e**x + x -7

def fp(x):
    return np.e**x + 1

x0 = 1
k_max = 1000
vals = np.zeros(k_max+1)
vals[0] = x0
tol = 10**-8
j = 0

for i in range(k_max):
    vals[i+1] = vals[i] - (f(vals[i]) / fp(vals[i]))

    if np.abs(vals[i] - vals[i+1]) < tol:
        j = i + 1
        break

print('{:.9f}'.format(vals[j]))
