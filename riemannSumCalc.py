# McKenna Branting 
# Outputs code for Riemann Sum
import numpy as np
import matplotlib.pyplot as plt


# Function used to find the exact value of riemann sum value
def riemann_sum(f, a, b, N, method='midpoint'):
    dx = (b - a) / N
    x = np.linspace(a, b, N + 1)

    # Calculates value if finding left riemann sum value
    if method == 'left':
        x_left = x[:-1]
        print(np.sum(f(x_left) * dx))
        return np.sum(f(x_left) * dx)
    # Calculates value if finding right riemann sum value
    elif method == 'right':
        x_right = x[1:]
        print(np.sum(f(x_right) * dx))
        return np.sum(f(x_right) * dx)
    # Calculates value if finding midpoint riemann sum value (default value)
    elif method == 'midpoint':
        x_mid = (x[:-1] + x[1:]) / 2
        print(np.sum(f(x_mid) * dx))
        return np.sum(f(x_mid) * dx)
    else:
        raise ValueError("Method must be 'left', 'right' or 'midpoint'.")


# Finds value for Part 1 Section C Subsection 1
riemann_sum(np.log, 1, np.e, 100)
