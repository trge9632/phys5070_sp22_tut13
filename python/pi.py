"""
Numerical approximation of pi using an integral.
"""

import numpy as np

num_points = 100

x = np.linspace(-1,1,num_points)
my_pi = 2*np.trapz(np.sqrt(1-x**2), x=x)

print("Pi = (approximately)", my_pi)
