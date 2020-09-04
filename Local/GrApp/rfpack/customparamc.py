import numpy as np
import pandas as pd
# from pathlib import Path
from datetime import date
import sqlite3
from plotnine import *
from pyexcelerate import Workbook
from pyexcelerate_to_excel import pyexcelerate_to_excel
from rfpack.switcherc import *
# from rfpack.carriersc import carriers
# from rfpack.carrierlc import carrierl
# from rfpack.carrtextc import carrtext
# from rfpack.carrtexlc import carrtexl
from rfpack.statzonc import statzon
from rfpack.par_auditc import par_audit
from rfpack.cleaniparmc import cleaniparm
from rfpack.cleaniparm2c import cleaniparm2
# from rfpack.pntopdc import pntopd
# from rfpack.tabconvc import tabconv
from mizani.transforms import trans


class asinh_trans(trans):
    """
        asinh Transformation
        """

    @staticmethod
    def transform(y):
        y = np.asarray(y)
        return np.arcsinh(y)

    @staticmethod
    def inverse(y):
        y = np.asarray(y)
        return np.sinh(y)


def customparam(datb, tab_par):
    dat_dir = datb.parent
    today = date.today()
    wb = Workbook()  # pyexcelerate Workbook
    pnglist = []
    consfull = []
    conspref = []
    tit = today.strftime("%y%m%d") + '_Feat1ParAudit'
    xls_file = tit + ".xlsx"
    xls_path = dat_dir / xls_file
    conn = sqlite3.connect(datb)  # database connection
    c = conn.cursor()
    ftab1 = tab_par + '.csv'  # tables and parameters to audit
    df3 = pd.read_csv(dat_dir / ftab1)
    df4 = df3.groupby('table_name')['parameter'].apply(list).reset_index(name='parlist')
    for index, row in df4.iterrows(): # table row iteration
        line = row['table_name']
        namtoinx = 'LNCELname'    # default values for lncel related tables
        carrfilt = 'earfcnDL'
        if line == 'RNFC' or line == 'LNBTS':  # carrier count - amount of graphs 1 for BTS
            n = 1    # 2 individual tables
        else:
            n = 5   # 11 tables with carries to graph
        paramst1 = row['parlist']  # parameter list
        if line == 'WCEL':
            paramsext = ('Prefijo', 'WBTS_id', 'UARFCN', 'WCELName', 'Banda', 'Encargado')
            namtoinx = 'WCELName'
            carrfilt = 'UARFCN'
        elif line == 'ANRPRL':
            paramsext = ('Prefijo', 'LNBTS_id', 'LNBTSname', 'Banda', 'Encargado')
            namtoinx = 'LNBTSname'
            carrfilt = 'targetCarrierFreq'
        elif line == 'RNFC':
            paramsext = ('Prefijo', 'RNC_id', 'RNCName', 'Encargado')
            namtoinx = 'RNCName'
            carr = 'RNC'
        elif line == 'LNBTS':
            paramsext = ('Prefijo', 'LNBTSname', 'Encargado')
            namtoinx = 'LNBTSname'
            carr = 'LNBTS'
        else:  # add columns to include in table query
            paramsext = ('Prefijo', 'LNBTS_id', 'earfcnDL', 'LNCELname', 'Banda', 'Encargado')
        paramst1.extend(paramsext)
        parstring = ','.join(paramst1)
        tabsq = tabconv(line)  # select reference table to get info
        try:  # include queries for all and carrier, pending
            datsrc = pd.read_sql_query("select " + parstring + " from " + tabsq + ";", conn,
                                       index_col=[namtoinx, 'Prefijo'])
            pyexcelerate_to_excel(wb, datsrc, sheet_name=line + '_data', index=True)  # saves raw info
            if not (line == 'LNBTS' or line == 'RNFC' or line == 'WBTS'):
                datsrc = datsrc.dropna(subset=['Banda'])  # cleans NaN band registers
            for i in range(0, n):  # loop for each carrier. once for no carrier tables
                if line == 'WCEL': # unique UMTS table
                    carr = carriers(i)
                    cart = carrtext(i)
                else:   # add columns to include in table query
                    carr = carrierl(i)  # carrier number
                    cart = carrtexl(i)  # carrier name
                if line == 'LNBTS' or line == 'RNFC' or line == 'WBTS' or carr == 'all':
                    df2 = datsrc
                else:
                    df2 = datsrc[:][datsrc[carrfilt] == carr]
                if len(df2) > 0:  # control for empty df
                    stpref = statzon(df2)  # stats per parameter and prefijo
                    st = par_audit(df2)  # stats per parameter full set
                    output = 'parametros.csv'
                    st.to_csv(dat_dir / output)
                    output = 'parametro.csv'
                    stpref.to_csv(dat_dir / output)
                    df2, st = cleaniparm(dat_dir, "ExParam.csv", "expfeat1", df2, st)  # info parameter removal
                    if line == 'LNBTS' or line == 'RNFC' or line == 'WBTS' or carr == 'all':
                        sttemp = st.copy(deep=True)
                        sttemp.insert(0, 'table', line)
                        sttemp1 = stpref.copy(deep=True)
                        sttemp1.insert(0, 'table', line)
                        if len(consfull) == 0:  # empty stzf control
                            consfull = sttemp
                        else:
                            consfull = consfull.append(sttemp)
                        if len(conspref) == 0:  # empty stzf control
                            conspref = sttemp1
                        else:
                            conspref = conspref.append(sttemp1)
                    else:
                        pyexcelerate_to_excel(wb, st, sheet_name=line + str(carr), index=True)
                        pyexcelerate_to_excel(wb, stpref, sheet_name=line + str(carr) + 'pref', index=True)
                    df2, st = cleaniparm2(df2, st)  # standardized params and NaN>0.15*n removal
                    parqty = len(st)   # parameter amount
                    if parqty > 0: # only for parameters with discrepancies
                        st['topdisc'] = range(parqty)  # top disc counter by IQR-CV
                        st['topdisc'] = st['topdisc'].floordiv(10)  # split disc in groups by 10
                        st.sort_values(by=['Median'], inplace=True, ascending=[False])  # for better visualization
                        st['counter'] = range(parqty)  # counter controls number of boxplots
                        st['counter'] = st['counter'].floordiv(10)  # split parameters in groups by 10
                        cols = ['StdDev', 'mean', 'Median', 'upper', 'lower', 'CV']
                        st[cols] = st[cols].round(1)  # scales colums with 1 decimal digit
                        stpref[cols] = stpref[cols].round(1)  # Prefijo info
                        # concat info to put text in boxplots
                        st['concat'] = st['StdDev'].astype(str) + ', ' + st['NoModeQty'].astype(str)
                        stpref['concat'] = stpref['StdDev'].astype(str) + ', ' + stpref['NoModeQty'].astype(str)
                        ldcol = list(st.index)  # parameters to include in melt command
                        # Structuring df2 according to ‘tidy data‘ standard
                        df2 = df2.reset_index()  # to use indexes in melt operation
                        df1 = df2.melt(id_vars=['Prefijo'], value_vars=ldcol,  # WCELName is not used
                                       var_name='parameter', value_name='value')
                        df1 = df1.dropna(subset=['value'])  # drop rows with value NaN
                        st.reset_index(inplace=True)  # parameter from index to col
                        stpref.reset_index(inplace=True)  # parameter from index to col
                        temp = st[['parameter', 'topdisc']]  # topdisc to be included in stpref
                        stpref = pd.merge(stpref, temp, on='parameter')
                        result = pd.merge(df1, st, on='parameter')  # merge by columns not by index
                        resultzon = pd.merge(df1, stpref, on=['parameter', 'Prefijo'])  # merge by columns not by index
                        # graph code
                        custom_axis = theme(axis_text_x=element_text(color="grey", size=6, angle=90, hjust=.3),
                                            axis_text_y=element_text(color="grey", size=6),
                                            plot_title=element_text(size=25, face="bold"),
                                            axis_title=element_text(size=10),
                                            panel_spacing_x=1.6, panel_spacing_y=.45,
                                            # 2nd value number of rows and colunms
                                            figure_size=(5 * 4, 3.5 * 4)
                                            )
                        # ggplot code:value 'concat' is placed in coordinate (parameter, stddev)
                        my_plot = (ggplot(data=result, mapping=aes(x='parameter', y='value')) + geom_boxplot() +
                                   geom_text(data=st, mapping=aes(x='parameter', y='StdDev', label='concat'),
                                             color='red', va='top', ha='left', size=7, nudge_x=.6, nudge_y=-1.5) +
                                   facet_wrap('counter', scales='free') + custom_axis + scale_y_continuous(
                                    trans=asinh_trans) + ylab("Values") + xlab("Parameters") +
                                   labs(title=line + " Parameter Audit " + cart) + coord_flip())
                        pngname = str(line) + str(carr) + ".png"  # saveplot
                        pngfile = dat_dir / pngname
                        my_plot.save(pngfile, width=20, height=10, dpi=300)
                        pnglist.append(pngfile)  # plots to be printed in pdf
                        if parqty < 11:
                            n = 1  # only 1 plot
                        else:
                            n = 2  # top 2 plots
                        for j in range(0, n):
                            toplot = resultzon.loc[resultzon['topdisc'] == j]  # filter info for parameter set to be printed
                            toplot1 = stpref.loc[stpref['topdisc'] == j]
                            custom_axis = theme(axis_text_x=element_text(color="grey", size=7, angle=90, hjust=.3),
                                                axis_text_y=element_text(color="grey", size=7),
                                                plot_title=element_text(size=25, face="bold"),
                                                axis_title=element_text(size=10),
                                                panel_spacing_x=0.6, panel_spacing_y=.45,
                                                # 2nd value number of rows and colunms
                                                figure_size=(5 * 4, 3.5 * 4)
                                                )
                            top_plot = (ggplot(data=toplot, mapping=aes(x='parameter', y='value')) + geom_boxplot() +
                                        geom_text(data=toplot1, mapping=aes(x='parameter', y='StdDev', label='concat'),
                                                  color='red', va='top', ha='left', size=7, nudge_x=.6, nudge_y=-1.5) +
                                        facet_wrap('Prefijo') + custom_axis + scale_y_continuous(
                                        trans=asinh_trans) + ylab("Values") + xlab("Parameters") +
                                        labs(title="Top " + str(j + 1) + " Disc Parameter per Zone. " + cart) + coord_flip())
                            pngname = str(line) + str(carr) + str(j + 1) + ".png"
                            pngfile = dat_dir / pngname
                            top_plot.save(pngfile, width=20, height=10, dpi=300)
                            pnglist.append(pngfile)
        except sqlite3.Error as error:  # sqlite error handling.
            print('SQLite error: %s' % (' '.join(error.args)))
    filterpar = list(df3.parameter)
    consfull = consfull.reset_index().rename(columns={'index': 'parameter'})
    consfull['Prefijo'] = 'full'
    conspref = conspref.reset_index().rename(columns={'index': 'parameter'})
    consfull = consfull.append(conspref, ignore_index = True)  # consfull info to show CV and nomodeper
    consfull = consfull[consfull['parameter'].isin(filterpar)]  # includes only input parameters
    consfull.dropna(subset=['CV'], inplace=True)
    for index, row in consfull.iterrows():  # table row iteration by Prefijo column type
        if row['Prefijo'] in znfrmt(0):
            consfull.loc[index, 'prorder'] = 0  # update column with print order id
        elif row['Prefijo'] in znfrmt(1):
            consfull.loc[index, 'prorder'] = 1
        elif row['Prefijo'] in znfrmt(2):
            consfull.loc[index, 'prorder'] = 2
        else:
            consfull.loc[index, 'prorder'] = 3
    pyexcelerate_to_excel(wb, consfull, sheet_name='Total', index=False)
    wb.save(xls_path)
    c.close()
    conn.close()
    return pnglist
