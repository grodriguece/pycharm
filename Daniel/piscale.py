import numpy as np


def format_func4(value, tick_number):
    # find number of multiples of pi/4
    N = int(np.round(4 * value / np.pi))
    if N == 0:
        return "0"
    elif N == 1:
        return r"$\pi/4$"
    elif N == 2:
        return r"$\pi/2$"
    elif N == 3:
        return r"$3\pi/4$"
    elif N == 6:
        return r"$3\pi/2$"
    elif N == 4:
        return r"$\pi$"
    elif N % 4 > 0:
        return r"${0}\pi/4$".format(N)
    else:
        return r"${0}\pi$".format(N // 4)


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
