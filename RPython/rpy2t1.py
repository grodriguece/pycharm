# import rpy2.robjects as robjects
#
# r = robjects.r
#
# x = robjects.IntVector(range(10))
# y = r.rnorm(10)
#
# r.X11()
#
# r.layout(r.matrix(robjects.IntVector([1,2,3,2]), nrow=2, ncol=2))
# r.plot(r.runif(10), y, xlab="runif", ylab="foo/bar", col="red")

# from rpy2 import robjects
# from rpy2.robjects import Formula, Environment
# from rpy2.robjects.vectors import IntVector, FloatVector
# from rpy2.robjects.lib import grid
# from rpy2.robjects.packages import importr, data
# from rpy2.rinterface_lib.embedded import RRuntimeError
# import warnings
#
# # The R 'print' function
# rprint = robjects.globalenv.find("print")
# stats = importr('stats')
# grdevices = importr('grDevices')
# base = importr('base')
# datasets = importr('datasets')
#
# grid.activate()
#
# import math, datetime
# import rpy2.robjects.lib.ggplot2 as ggplot2
# import rpy2.robjects as ro
# from rpy2.robjects.packages import importr
# base = importr('base')
#
# mtcars = data(datasets).fetch('mtcars')['mtcars']
#
# pp = (ggplot2.ggplot(mtcars) +
#       ggplot2.aes_string(x='wt', y='mpg', col='factor(cyl)') +
#       ggplot2.geom_point() +
#       ggplot2.geom_smooth(ggplot2.aes_string(group='cyl'),
#                           method='lm'))
# pp.plot()
# from rpy2.robjects.packages import importr
# grdevices = importr('grDevices')
#
# grdevices.png(file="path/to/file.png", width=512, height=512)
# # plotting code here
# grdevices.dev_off()
# from rpy2.robjects.packages import importr
# grdevices = importr('grDevices')
# palette = grdevices.palette()
# print(palette)
from rpy2 import robjects
from rpy2.robjects import Formula, Environment
from rpy2.robjects.vectors import IntVector, FloatVector
from rpy2.robjects.lib import grid
from rpy2.robjects.packages import importr, data
from rpy2.rinterface_lib.embedded import RRuntimeError
import warnings

# The R 'print' function
rprint = robjects.globalenv.find("print")
stats = importr('stats')
grdevices = importr('grDevices')
base = importr('base')
datasets = importr('datasets')

grid.activate()
lattice = importr('lattice')
xyplot = lattice.xyplot
datasets = importr('datasets')
mtcars = data(datasets).fetch('mtcars')['mtcars']
formula = Formula('mpg ~ wt')
formula.getenvironment()['mpg'] = mtcars.rx2('mpg')
formula.getenvironment()['wt'] = mtcars.rx2('wt')

p = lattice.xyplot(formula)
rprint(p)
p = lattice.xyplot(formula, groups = mtcars.rx2('cyl'))
rprint(p)
formula = Formula('mpg ~ wt | cyl')
formula.getenvironment()['mpg'] = mtcars.rx2('mpg')
formula.getenvironment()['wt'] = mtcars.rx2('wt')
formula.getenvironment()['cyl'] = mtcars.rx2('cyl')

p = lattice.xyplot(formula, layout = IntVector((3, 1)))
rprint(p)
p = lattice.bwplot(Formula('mpg ~ factor(cyl) | gear'),
                   data = mtcars, fill = 'grey')
rprint(p, nrow=1)
tmpenv = data(datasets).fetch("volcano")
volcano = tmpenv["volcano"]

p = lattice.wireframe(volcano, shade = True,
                      zlab = "",
                      aspect = FloatVector((61.0/87, 0.4)),
                      light_source = IntVector((10,0,10)))
rprint(p)