import numpy as np

def f(x):
    return np.e**x + np.sin(x) - 4

x0, x1 = 0, 1
k_max = 1000
vals = np.zeros(k_max+2)
vals[0], vals[1] = x0, x1
tol = 10**-8
j = 0

for i in range(1, k_max+1):
    x, x_prv = vals[i], vals[i-1]
    f_x = f(x)
    vals[i+1] = x - ((f_x * (x - x_prv)) / (f_x - f(x_prv)))

    if np.abs(vals[i+1] - x) < tol:
        j = i + 1
        break

print('{:.9f}'.format(vals[j]))
