import matplotlib.pyplot as plt
import numpy as np


def format_func2(value, tick_number):
    # find number of multiples of pi/2
    N = int(np.round(2 * value / np.pi))
    if N == 0:
        return "0"
    elif N == 1:
        return r"$\pi/2$"
    elif N == -1:
        return r"$-\pi/2$"
    elif N == 2:
        return r"$\pi$"
    elif N == -2:
        return r"$-\pi$"
    elif N % 2 > 0:
        return r"${0}\pi/2$".format(N)
    else:
        return r"${0}\pi$".format(N // 2)


fig, ax = plt.subplots()
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y = 1/np.tan(x)
y[np.abs(np.sin(x)) <= np.abs(np.sin(x[1]-x[0]))] = np.nan
# This operation inserts a NaN where cos(x) is reaching 0
# NaN means "Not a Number" and NaNs are not plotted or connected
ax.plot(x, y, lw=2, color="blue", label='Tangent')
# Set up grid, legend, and limits
ax.grid(True)
ax.legend(frameon=False)
ax.set_xlim(-2 * np.pi, 2 * np.pi)
ax.xaxis.set_major_locator(plt.MultipleLocator(np.pi / 2))
ax.xaxis.set_minor_locator(plt.MultipleLocator(np.pi / 4))
ax.xaxis.set_major_formatter(plt.FuncFormatter(format_func2))
plt.ylim(top=10)  # y axis limit values
plt.ylim(bottom=-10)
y_ticks = np.arange(-10, 10, 1)
plt.yticks(y_ticks)
fig
plt.show()
