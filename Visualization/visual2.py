# %matplotlib inline
from plotnine import *
import pandas as pd
import numpy as np

# surveys_complete = pd.read_csv("C:\\PyCharm\\Visualization\\data\\surveys.csv")
# surveys_complete = surveys_complete.dropna()
# custom_axis = p9.theme(axis_text_x = p9.element_text(color="grey", size=6, angle=90, hjust=.5),
#                            axis_text_y = p9.element_text(color="grey", size=9))
# # flip_xlabels = p9.theme(axis_text_x = p9.element_text(size=6, angle=90, hjust=1))
# # print(p9.ggplot(data=surveys_complete, mapping=p9.aes(x='factor(year)', fill = 'species_id'))
# #  + p9.geom_bar(stat='count') + custom_axis)
#
# # print(p9.ggplot(data=surveys_complete, mapping=p9.aes(x='factor(year)',
# # fill = 'species_id')) + p9.geom_bar(stat='count') +
# # custom_axis + p9.scale_fill_hue(l=.40) +
# # p9.guides(col = p9.guide_legend(nrow = 8, byrow = True),
# # fill = p9.guide_legend(title = "SPECIES", label_position = "left", label_hjust = 1))
# print(p9.ggplot(data=surveys_complete, mapping=p9.aes(x='factor(year)',
# fill = 'factor(species_id)')) + p9.geom_bar(stat='count') +
# custom_axis + p9.guides(colour = p9.guide_legend(nrow = 8, byrow = True))
# )

# multiple row/col legends

N = 20
letters = list('ABCDEFGHIJKLMNOPQRST')
df = pd.DataFrame({ 'x' : range(1, N + 1 ,1),
    'y' : range(1, N + 1 ,1)
    ,'color' : letters})
print(df)
#
#     'C' : pd.Series(random.choice(string.ascii_uppercase) for _ in range(N)) })
#
# df <- data.frame(x = [1:20], y = [1:20], color = letters[1:20])
print((ggplot(df, aes(x='x', y='y'))) + geom_point(aes(colour = 'color')) +
guides(col = guide_legend(nrow = 8)))
# p + guides(col = guide_legend(ncol = 8))
# p + guides(col = guide_legend(nrow = 8, byrow = TRUE))
#
# # reversed order legend
# p + guides(col = guide_legend(reverse = TRUE))
