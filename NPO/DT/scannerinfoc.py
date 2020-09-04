import pandas as pd
from datetime import date
from pathlib import Path
import numpy as np
from rfpack.switcherc import tecnol


def scaninf(datalog, techid):
    import pandas as pd
    if techn == 1:  # umts info
        # columnam = ['type', 'time', 'space', 'meas_system', 'headparms', 'uarfcn',
        #             'chtype', 'carr_rssi', 'band', 'meas', 'parpercell']
        dumts = []
        types = 'PILOTSCAN'
        for srow in datalog:
            if types in str(srow):
                dumts.append(srow)  # creates new list with umts scanner info
        umdf = pd.DataFrame([sub.split(",") for sub in dumts])  # text to columns
        umdf[9] = umdf[9].astype(int)
        maxcel = umdf[9].max()  # max cells number in msg
        # for i in range(maxcel):  # put columns names
        #     columnam.extend(['pscr' + str(i), 'ec_no' + str(i), 'rscp' + str(i),
        #                      'sir' + str(i), 'delay' + str(i), 'delay_spread' + str(i)])
        # umdf.columns = columnam
        umdft = []  # df to put cell alike info in the same columns
        for i in range(maxcel):
            umdf1 = umdf.iloc[:, [8, 5, 7, 11 + i * 6, 12 + i * 6, 13 + i * 6]]
            umdf1.columns = ['band', 'uarfcn', 'carr_rssi', 'pscr', 'ec_no', 'rscp']
            if len(umdft) == 0:
                umdft = umdf1
            else:
                umdft = pd.concat([umdft, umdf1], ignore_index=True)
        umdft['ec_no'].replace('', np.nan, inplace=True)  # convert empty strings as nan
        umdft.dropna(subset=['pscr', 'ec_no'], inplace=True)  # remove invalid info
        convert_dict = {'band': int,
                        'uarfcn': int,
                        'carr_rssi': float,
                        'pscr': int,
                        'ec_no': float,
                        'rscp' : float
                        }
        umdft = umdft.astype(convert_dict)  # converts to num format for grouping
        umgroup = umdft.groupby(['band', 'uarfcn', 'pscr']).agg({'carr_rssi': ['mean'],
                                                                 'ec_no': ['mean'], 'rscp': ['mean', 'count']})
        umgroup = umgroup.reset_index()
    return umgroup


scanf = Path('C:/SQLite/logs/20Feb25 144322.1.nmf')
workdir = scanf.parent
techn = 1
timetest = [14, 43, 26]  # time to search in scan file
timetest1 = list(timetest)
timetest1[2] = timetest1[2] - 1
timestr = ':'.join(map(str, timetest))
timestr1 = ':'.join(map(str, timetest1))
with open(scanf, 'rt') as myfile:  # Open scanf for reading text
    for line in myfile.readlines():
        if '#START' in line:  # time and date startlog
            startt = line
            break
mList = [int(e) if e.isdigit() else e for e in startt.split(',')]
hora = mList[1]
mlist2 = [int(e) if e.isdecimal() else float(e) for e in hora.split(':')]
fecha = mList[3]
fecha = fecha.translate(str.maketrans({'\n': '', '"': ''}))  # remove unwanted chars
mlist3 = [int(e) if e.isdigit() else e for e in fecha.split('.')]
# mList2 with time [hr, m, s] mList3 wit date [d, m, y]
dataLog = []
with open(scanf, 'rt') as myfile:  # Open scanf for reading text
    for line in myfile.readlines():
        if timestr in line or timestr1 in line:
            dataLog.append(line)  # filter for event time (2 secs)
scaninf(dataLog, techn)  # generates df with pscrs measuremets for the period selected


# dataLog = []
# with open(scanf, 'rt') as myfile:  # Open lorem.txt for reading text
#     for line in myfile.readlines():
#         if 'SCAN' in line or 'GPS' in line or 'START' in line:
#             # contents = myfile.read()              # Read the entire file to a string
#             dataLog.append(line)
# print(dataLog)  # Print the string

# timew =
# tabfile = datab.parent / Path('tablasSQL.csv')
# tabfileop = "tabla"
# scanfinf(scanf, time, tabfileop, 1, root, my_progress, proglabel2)

# myfile = open(scanf, "rt") # open lorem.txt for reading text
# contents = myfile.read()         # read the entire file to string
# myfile.close()                   # close the file
# print(contents)

