import math
import numpy as np
from matplotlib import pyplot as plt
import pyswarms as ps
from pyswarms.utils.plotters import plot_cost_history

def endurance(arr):
    x, y, z, u, v, w = arr
    return -math.exp(-2*(y-math.sin(x))**2)+math.sin(z*u)+math.cos(v*w)

def f(x):
    n_particles = x.shape[0]
    j = [endurance(x[i]) for i in range(n_particles)]
    return np.array(j)

# Set-up hyperparameters
options = {'c1': 0.5, 'c2': 0.3, 'w':0.9}

x_max = [1, 1, 1, 1, 1, 1]
x_min = [0, 0, 0, 0, 0, 0]
my_bounds = [x_min, x_max]

# Call instance of PSO
optimizer = ps.single.GlobalBestPSO(n_particles=10, dimensions=6, options=options, bounds=my_bounds)

# Perform optimization
cost, pos = optimizer.optimize(f, iters=200)

# Obtain cost history from optimizer instance
cost_history = optimizer.cost_history

# Plot!
plot_cost_history(cost_history)
plt.show()