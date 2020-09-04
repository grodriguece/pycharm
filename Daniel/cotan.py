#!/usr/bin/python
from pylab import *

# rendering area
figure(figsize=(8,5), dpi=80)

# display area to use; can be modified to accomodate more graphs
subplot(111)

# range
x = np.linspace(0, (2 * np.pi), 256,endpoint=True)

# formulas to graph
sine = np.sin(x)
cosine = np.cos(x)
tangent = np.tan(x)
cotangent = 1/np.tan(x)
cosecant = 1/np.sin(x)
secant = 1/np.cos(x)

# line styles and labels
plot(x, sine, color="red", linewidth=2.5, linestyle="-", label="sin")
plot(x, cosine, color="blue", linewidth=2.5, linestyle="-", label="cos")
plot(x, tangent, color="orange", linewidth=2.5, linestyle="-", label="tan")
plot(x, cotangent, color="purple", linewidth=2.5, linestyle="-", label="cot")
plot(x, cosecant, color="green", linewidth=2.5, linestyle="-", label="csc")
plot(x, secant, color="yellow", linewidth=2.5, linestyle="-", label="sec")

# tick spines
ax = gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

# x tick limits and labels
xlim(x.min()*1.1, x.max()*1.1)
xticks([(-2 * np.pi), (-3 * np.pi/2), -np.pi, -np.pi/2, 0, np.pi/2, np.pi, (3 * np.pi/2), (2 * np.pi)], [r'$-2\pi$', r'$-3/2\pi$', r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$', r'$3/2\pi$', r'$2\pi$'])

# y tick limits and labels
ylim(-4, 4)
yticks([-4, -3, -2, -1, +1, +2, +3, +4], [r'$-4$', r'$-3$', r'$-2$', r'$-1$', r'$+1$', r'$+2$', r'$+3$', r'$+4$'])

# legend
legend(loc='upper left')

for label in ax.get_xticklabels() + ax.get_yticklabels():
  label.set_fontsize(16)
  label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65 ))

# display
show()
