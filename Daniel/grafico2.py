import numpy as np
import matplotlib.pyplot as plt
plt.figure()    # Create a new figure window
xlist = np.linspace(-2.0, 1.0, 100)     # Create 1-D arrays for x,y dimensions
ylist = np.linspace(-1.0, 2.0, 100)
X, Y = np.meshgrid(xlist, ylist)     # Create 2-D grid xlist,ylist values
Z = np.sqrt(X**2 + Y**2)    # Compute function values on the grid
plt.contour(X, Y, Z, [0.5, 1.0, 1.2, 1.5], colors='k', linestyles='solid')
# plt.axes().set_aspect('equal')  # Scale the plot size to get same aspect ratio
# plt.axis([-1.0, 1.0, -0.5, 0.5])    # Set axis limits
plt.show()

