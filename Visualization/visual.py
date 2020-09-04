import pandas as pd
from plotnine import *


demo = pd.read_csv("demo.csv")
print(demo)
# # good to compare info per rnc
# simple_point = (ggplot(demo, aes(color='shape', y='y', x='x')) + geom_point() + facet_grid('~ shape'))
# # simple_point = (ggplot(demo, aes(color='shape', y='y', x='x')) + geom_line())
simple_point = (ggplot(demo, aes(color='shape', y='y', x='x')) + geom_bar(stat='identity'))
print(simple_point)
# simple_point.save("simple_point.pdf", scale=0.6, height=6, width=8)
# troops = pd.read_csv("troops.csv")
# cities = pd.read_csv("cities.csv")
# # print(troops)
# plot_troops = (ggplot(troops, aes('long', 'lat')) + geom_path(aes(size='survivors', color="direction", group='group')))
# # print(plot_troops)
# both = plot_troops + geom_text(aes(label='city'), size=7, data=cities)
# polish = both + scale_color_manual(["#888888", "#990000"])
# print(polish)
# http://users.umiacs.umd.edu/~jbg/teaching/INST_414/
# https://datacarpentry.org/python-ecology-lesson/07-visualization-ggplot-python/index.html
# https://www.datacamp.com/community/tutorials/matplotlib-tutorial-python
# https://www.kdnuggets.com/2019/12/python-alternative-ggplot2.html
# https://dputhier.github.io/jgb53d-bd-prog_github/practicals/intro_ggplot/intro_ggplot.html
# http://www.dartmouth.edu/~chance/teaching_aids/books_articles/probability_book/book.html

