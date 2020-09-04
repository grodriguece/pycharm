import matplotlib.pyplot as plt
import numpy as np
from piscale import *


# Plot a sine and cosine curve
fig, ax = plt.subplots()
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y = np.tan(x)
y[np.abs(np.cos(x)) <= np.abs(np.sin(x[1]-x[0]))] = np.nan
# This operation inserts a NaN where sin(x) is reaching 0
# NaN means "Not a Number" and NaNs are not plotted or connected
ax.plot(x, y, lw=2, color="blue", label='tangent')
#
# Set up grid, legend, and limits
ax.grid(True)
ax.legend(frameon=False)
# ax.axis('equal')
ax.set_xlim(-2 * np.pi, 2 * np.pi)
ax.xaxis.set_major_locator(plt.MultipleLocator(np.pi / 2))
ax.xaxis.set_minor_locator(plt.MultipleLocator(np.pi / 4))
ax.xaxis.set_major_formatter(plt.FuncFormatter(format_func2))
fig
plt.show()