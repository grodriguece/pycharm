def iqrcalc(q1, q3, n, std, mean):
    import numpy as np
    if .1 > mean > -.1:
        cv = 100 * std
    else:
        cv = 100 * std / abs(mean)
    return q3 + (1.58 * (q3 - q1) / np.sqrt(n)), q1 - (1.58 * (q3 - q1) / np.sqrt(n)), q3 - q1, cv
