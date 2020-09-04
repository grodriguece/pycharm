# # import rpy2
# import rpy2.situation
# print(rpy2.__version__)
# for row in rpy2.situation.iter_info():
#     print(row)

# case 1
# import rpy2.robjects as robjects

# case 2
# from rpy2.robjects.packages import importr
# base = importr('base')      # import R's "base" package
# utils = importr('utils')        # import R's "utils" package

# case 3
# import rpy2's package module
import rpy2.robjects.packages as rpackages
# R vector of strings
from rpy2.robjects.vectors import StrVector
base = rpackages.importr('base')
# import R's utility package
utils = rpackages.importr('utils')
# select a mirror for R packages: select the first mirror in the list
utils.chooseCRANmirror(ind=1)
# R package names
packnames = ('ggplot2', 'hexbin')
# Selectively install what needs to be install.
# We are fancy, just because we can.
names_to_install = [x for x in packnames if not rpackages.isinstalled(x)]
if len(names_to_install) > 0:
    utils.install_packages(StrVector(names_to_install))

# # case 4
# import rpy2.robjects as robjects
# pi = robjects.r['pi']
# len(robjects.r['pi'])
# print(pi[0])
# # pi is not a scalar but a vector of length 1
# piplus2 = robjects.r('pi') + 2
# print(piplus2.r_repr())
# pi0plus2 = robjects.r('pi')[0] + 2
# print(pi0plus2)
#
# # R sequences of expressions. evaluation is performed in the Global Environment
# # creates an R function, then binds it to the symbol f (in R), finally calls that function f.
# # The results of the call (what the R function f is returns) is returned to Python.
# robjects.r('''
#         # create a function `f`
#         f <- function(r, verbose=FALSE) {
#             if (verbose) {
#                 cat("I am calling f().\n")
#             }
#             2 * pi * r
#         }
#         # call the function `f` with argument value 3
#         f(3)
#         ''')
# # r_f = robjects.globalenv['f']
# # print(r_f.r_repr())
# # an alternative way to get the function is to get it from the R singleton
# r_f = robjects.r['f']
# res = r_f(3)
# print(res)

# # Case 5
# # Interpolating R objects into R code strings
# import rpy2.robjects as robjects
# letters = robjects.r['letters']
# rcode = 'paste(%s, collapse="-")' %(letters.r_repr())
# res = robjects.r(rcode)
# print(res)

# Case 6
# # Creating rpy2 vectors
# import rpy2.robjects as robjects
# res = robjects.StrVector(['abc', 'def'])
# print(res.r_repr())
# res = robjects.IntVector([1, 2, 3])
# print(res.r_repr())
# res = robjects.FloatVector([1.1, 2.2, 3.3])
# print(res.r_repr())
# # R matrixes and arrays are just vectors with a dim attribute.
# v = robjects.FloatVector([1.1, 2.2, 3.3, 4.4, 5.5, 6.6])
# m = robjects.r['matrix'](v, nrow=2)
# print(m)
# # Calling R functions
# rsum = robjects.r['sum']
# res = rsum(robjects.IntVector([1, 2, 3]))[0]
# # res is int
# print(res)
# # Keywords
# rsort = robjects.r['sort']
# res = rsort(robjects.IntVector([1, 2, 3]), decreasing=True)
# print(res.r_repr())
