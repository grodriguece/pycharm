from rfpack.dt_timec import decsecs, comptime


def sib3cellinf(msgstr):
    # 4 bit for each hex char 04b means 0-padded 4chars long binary string):
    res2 = "".join([f'{int(c, 16):04b}' for c in msgstr])  # 16 4 bit groups
    rnc = int(res2[2:14], base=2)
    cellid = int(res2[14:30], base=2)
    return rnc, cellid


def xtrctlns(filex, timetst):
    scanlog = []
    timestr = decsecs(timetst, 5)  # string with times to extract 5 secs
    with open(filex, 'rt') as myfile:  # Open scanf for reading text
        for line in myfile.readlines():
            for tim in timestr:  # check str list in line
                if tim in line:  # time window msg
                    scanlog.append(line)  # filter for event time (5 secs)
    return scanlog


def xtrctlnd(filex, timetst, drcall):
    datalog = []
    sib3inf = []
    timestr = decsecs(timetst, 5)  # string with times to extract
    with open(filex, 'rt') as myfile:  # open scanf for reading text
        for line in myfile.readlines():
            listemp = line.split(",")
            if listemp[0] == 'RRCSM':
                listemp[5] = listemp[5].replace('"', "")
                if listemp[5] == 'SYSTEM_INFORMATION_BLOCK_TYPE_3':
                    if comptime(listemp[1], timetst, 5) == 1:  # stores last sib3 info before window
                        sibfst = listemp[1]
                        listemp[9] = listemp[9].replace('"', "")
                        rncid, cellid = sib3cellinf(listemp[9][0: 8])
            for tim in timestr:  # check str list in line
                if tim in listemp[1]:  # time window msg
                    if listemp[0] == 'CARE' or listemp[0] == 'CAD' or listemp[0] == 'CELLMEAS':
                        datalog.append(line)  # filter for event time (5 secs)
                        if listemp[0] == 'CELLMEAS':
                            if comptime(listemp[1], timetst, 0) == 1:  # cmeas time < drp time
                                lastmeas = listemp[1]  # last meas time bef drop
                    if listemp[0] == 'RRCSM':
                        if listemp[5] == 'SYSTEM_INFORMATION_BLOCK_TYPE_3':
                            datalog.append(line)
    sib3inf.append([drcall, sibfst, rncid, cellid])  # sib3 initial msg
    return datalog, sib3inf, lastmeas


def readdrp(callog):  # get drop calls time in times list
    cllfl = callog.stem[0:7]  # date from file name 7 chars
    with open(callog, "r") as fi:
        idlst = []  # init drop msg list
        for ln in fi:
            if ln.startswith("CAD"):  # Call disconnect msg
                listemp = ln.split(",")  # string to list
                if int(listemp[6]) == 2:  # CS disc. status Dropped call
                    listemp.append(cllfl)
                    idlst.append(listemp)  # get entire msg
    return idlst
