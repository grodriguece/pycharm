import matplotlib.pyplot as plt
import numpy as np
from matplot_fmt_pi import MultiplePi

fig, ax = plt.subplots()        # creates a figure and one subplot
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y = np.tan(x)
y[np.abs(np.cos(x)) <= np.abs(np.sin(x[1]-x[0]))] = np.nan
# This operation inserts a NaN where cos(x) is reaching 0
# NaN means "Not a Number" and NaNs are not plotted or connected
ax.plot(x, y, lw=2, color="blue", label='Tangent')
# Set up grid, legend, and limits
ax.grid(True)
ax.axhline(0, color='black', lw=.75)
ax.axvline(0, color='black', lw=.75)
ax.set_title("Trigonometric Functions")
ax.legend(frameon=False)    # remove frame legend frame
# axis formatting
ax.set_xlim(-2 * np.pi, 2 * np.pi)
pi_manager = MultiplePi(8)          # number= ticks between 0 - pi
ax.xaxis.set_major_locator(pi_manager.locator())
ax.xaxis.set_major_formatter(pi_manager.formatter())
plt.ylim(top=10)  # y axis limit values
plt.ylim(bottom=-10)
y_ticks = np.arange(-10, 10, 1)
plt.yticks(y_ticks)
fig
plt.tight_layout()
plt.savefig("./tangent_graph.png", dpi=120)
plt.show()
