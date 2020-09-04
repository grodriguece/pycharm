from pathlib import Path
import pandas as pd
from plotnine import *
from rfpack.switcherc import znfrmt


def graffull(xls_file, csvnm, n, iterini, root1, my_progress1, proglabel21):
    pnglist1 = []
    file = xls_file.parent / 'csv' / Path(csvnm + '.csv')  # file Total
    df1 = pd.read_csv(file)
    for j in range(0, n):  # n plots, 3 regions per plot
        my_progress1['value'] = iterini + round(j / n * 15)  # prog bar up to iterini + 15
        proglabel21.config(text=my_progress1['value'])  # prog bar updt
        root1.update_idletasks()
        smrzd = df1.loc[df1['prorder'] == j]  # filter info for zones set to be printed
        custom_axis = theme(axis_text_x=element_text(color="grey", size=10, angle=90, hjust=.3),
                            axis_text_y=element_text(color="grey", size=10),
                            plot_title=element_text(size=25, face="bold"),
                            axis_title=element_text(size=10),
                            panel_spacing_x=1.6, panel_spacing_y=.45,  # review
                            figure_size=(3 * 4, 5 * 4)
                            )
        smrzd_plot = (ggplot(data=smrzd, mapping=aes(x='parameter'))
                      + geom_col(mapping=aes(y='CV'), size=0.1, color="darkblue", fill="white")
                      + geom_line(mapping=aes(y='NoModePer'), size=1.5, color="red", group=1)
                      + facet_wrap('Prefijo', ncol=1) + custom_axis + ylab("CV(bar) - NoMode(line)")
                      + xlab("Parameters")
                      + labs(title="Coefficient of variation - Out of Mode % " + ', '.join(znfrmt(j)))
                      )
        pngname = 'sumrzd' + str(j + 1) + '.png'
        pngfile = xls_file.parent / pngname
        smrzd_plot.save(pngfile, width=20, height=10, dpi=300)
        pnglist1.append(pngfile)
    return pnglist1
