import numpy as np
import matplotlib.pyplot as plt     # The code below assumes this convenient renaming
xvals = np.arange(-7, 7, 0.01)  # Grid of 0.01 spacing from -2 to 10
yvals = np.cos(xvals)   # Evaluate function on xvals
plt.plot(xvals, yvals)  # Create line plot with yvals against xvals
# plt.show()  # Show the figure, remove to the end to show both figs
newyvals = 1 - 0.5 * xvals**2 # Evaluate quadratic approximation on xvals
plt.plot(xvals, newyvals, 'r--')    # Create line plot with red dashed line
plt.title('Example plots')
plt.xlabel('Input')
plt.ylabel('Function values')
plt.show()  # Show the figure (remove the previous instance)
