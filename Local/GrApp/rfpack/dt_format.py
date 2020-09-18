import pandas as pd
import numpy as np


def drclpd(drpclst):
    cddf = pd.DataFrame(drpclst)
    cddf.columns = ['callnbrd', 'timedrp', 'callid', 'typed', 'status', 'cause', 'timesref',
                    'callnbrs', 'timesib', 'rncid', 'cellid', 'callnbr', 'timeas', 'carrier',
                    'carr_rssi', 'type', 'uarfcn', 'pscr', 'ec_no', 'rscp']
    cddf = cddf[['callnbrd', 'timedrp', 'callid', 'typed', 'status', 'cause', 'timesib', 'rncid',
                 'cellid', 'timeas', 'carrier', 'carr_rssi', 'type', 'uarfcn', 'pscr', 'ec_no', 'rscp']]
    cddf['ec_no'].replace('', np.nan, inplace=True)  # convert empty strings as nan
    cddf['uarfcn'].replace('', np.nan, inplace=True)  # convert empty strings as nan
    cddf.dropna(subset=['pscr', 'uarfcn', 'ec_no'], inplace=True)  # remove invalid info
    convert_dict = {'callnbrd': int,
                    'callid': int,
                    'typed': int,
                    'status': int,
                    'rncid': int,
                    'cellid': int,
                    'carrier': int,
                    'carr_rssi': float,
                    'type': int,
                    'uarfcn': int,
                    'pscr': int,
                    'ec_no': float,
                    'rscp': float
                    }
    cddf = cddf.astype(convert_dict)  # converts to num format for grouping
    return cddf


def scanpd(scanlst):  # group scan info after consolidation for all drops
    umdf = pd.DataFrame(scanlst)  # text to columns
    umdf.columns = ['drpcall', 'band', 'uarfcn', 'carr_rssi', 'pscr', 'ec_no', 'rscp']
    umdf['ec_no'].replace('', np.nan, inplace=True)  # convert empty strings as nan
    umdf.dropna(subset=['pscr', 'ec_no'], inplace=True)  # remove invalid info
    convert_dict = {'drpcall': int,
                    'band': int,
                    'uarfcn': int,
                    'carr_rssi': float,
                    'pscr': int,
                    'ec_no': float,
                    'rscp': float
                    }
    umdf = umdf.astype(convert_dict)  # converts to num format for grouping
    umgroup = umdf.groupby(['drpcall', 'band', 'uarfcn',
                            'pscr']).agg({'carr_rssi': ['mean'], 'ec_no': ['mean'], 'rscp': ['mean', 'count']})
    umgroup = umgroup.reset_index()
    umgroup.columns = ['drpcall', 'band', 'uarfcn', 'pscr', 'carr_rssi', 'ec_no', 'rscp', 'count']
    umgroup = umgroup.sort_values(["drpcall", "count", 'ec_no'], ascending=(True, False, False))
    return umgroup


def celmpd(droplst):  # group scan info after consolidation for all drops
    cmdf = pd.DataFrame(droplst)  # text to columns
    cmdf.columns = ['callnbrs', 'timesib', 'rncid', 'cellid', 'drpcall', 'timeas',
                    'carrier', 'carr_rssi', 'type', 'uarfcn', 'pscr', 'ec_no', 'rscp']
    cmdf['ec_no'].replace('', np.nan, inplace=True)  # convert empty strings as nan
    cmdf['uarfcn'].replace('', np.nan, inplace=True)  # convert empty strings as nan
    cmdf.dropna(subset=['pscr', 'uarfcn', 'ec_no'], inplace=True)  # remove invalid info
    convert_dict = {'rncid': int,
                    'cellid': int,
                    'drpcall': int,
                    'carrier': int,
                    'carr_rssi': float,
                    'type': int,
                    'uarfcn': int,
                    'pscr': int,
                    'ec_no': float,
                    'rscp': float
                    }
    cmdf = cmdf.astype(convert_dict)  # converts to num format for grouping
    ucgroup = cmdf.groupby(['rncid', 'cellid', 'drpcall', 'carrier', 'type', 'uarfcn',
                            'pscr']).agg({'carr_rssi': ['mean'], 'ec_no': ['max'], 'rscp': ['max', 'count']})
    ucgroup = ucgroup.reset_index()
    ucgroup.columns = ['rncid', 'cellid', 'drpcall', 'carrier', 'type', 'uarfcn',
                       'pscr', 'carr_rssi', 'ec_no', 'rscp', 'count']
    ucgroup = ucgroup.sort_values(['drpcall', 'type', 'count', 'ec_no'], ascending=(True, True, False, False))
    return ucgroup
