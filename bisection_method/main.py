import numpy as np

def f(x):
    return np.cos(x)**2 - x + 6

tol = 10**-7
a, b = 6.0, 7.0
f_a, f_b = f(a), f(b)

while (b - a) / 2 > tol:
    c = (a + b) / 2
    f_c = f(c)

    if f_c == 0:
        break
    
    if np.sign(f_c) * np.sign(f_a) < 0:
        b = c
        f_b = f_c
    else:
        a = c
        f_a = f_c

# Truncates root value from 7 decimal places to 6 without rounding
rt_str = '{:.7f}'.format((a + b) / 2)[:-1]
print(rt_str)