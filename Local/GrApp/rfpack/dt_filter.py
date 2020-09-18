import math
from rfpack.dt_xtract import sib3cellinf
from rfpack.dt_timec import comptime


def scaninfx(scninf, dcall):
    pilotslt = []
    for lin in scninf:
        line = lin.split(",")  # string to list
        if line[0] == 'PILOTSCAN':
            if line[9] == '':  # cells calculation based on msg size
                line[9] = math.floor(int((len(line)-11)/6))  # 11 independent params, 6 common params per cell
            for cl in range(int(line[9])):  # cellmeas list build
                pilotslt.append([dcall, line[8], line[5], line[7], line[11 + 6 * cl], line[12 + 6 * cl],
                                 line[13 + 6 * cl]])
    return pilotslt  # just UMTS info from scan file


def cellmeasx(datainf1, dcall, sib3inf, lstcmeas):
    cellmlt = []
    calldet = []
    for lin in datainf1:
        line = lin.split(",")  # string to list *********
        if line[0] == 'CELLMEAS':
            disp1 = 3 * (int(line[5]) - 1)  # adjust for multiple channels in scan msg(cells without uarfcn decoded)
            if line[10 + disp1] == '':  # cells calculation based on msg size
                line[10 + disp1] = math.floor(int((len(line) - (12 + disp1)/17)))
            for cl in range(int(line[10 + disp1])):  # cellmeas list build
                cellmlt.append([dcall, line[1], line[7], line[8], line[12 + disp1 + 17 * cl],
                                line[14 + disp1 + 17 * cl], line[15 + disp1 + 17 * cl],
                                line[16 + disp1 + 17 * cl], line[18 + disp1 + 17 * cl]])
        elif line[0] == 'RRCSM':  # sib 3 list build
            line[9] = line[9].replace('"', "")  # remove unwanted characters
            rncid, cellid = sib3cellinf(line[9][0: 8])  # get cell info with sib 3 first 8 bytes msg
            sib3inf.append([dcall, line[1], rncid, cellid])
        elif line[0] == 'CAD':  # call disconnect list build include last cellmeas serving info
            calldet.append([dcall, line[0], line[1], line[3], line[5], line[6], line[7], lstcmeas])
        else:  # Call Restablishment case
            calldet.append([dcall, line[0], line[1], line[3], None, line[5], line[6], lstcmeas])
    return cellmlt, sib3inf, calldet


def fillinf(cellmeas, sibinf):
    cellm1 = list(cellmeas)
    sib31 = list(sibinf)
    listot = []
    sibtime = []  # sib times to compare with drp times
    i = 0  # control to iterate sib31
    for sb in sib31:
        sibtime.append(sb[1])  # create list with sib times to compare
    for cms in cellm1:
        if len(sib31) > 1:
            if comptime(cms[1], sib31[i+1][1], 0) == 0:
                sbt = list(sib31[i+1])  # next sib element to use in append
                if (i+2) < len(sib31):  # end limit validation
                    i += 1  # next sib31 item
            else:
                sbt = list(sib31[i])  # concatenate with current sib value
        else:
            sbt = list(sib31[i])  # 1 element sib list just concatenate cellmeas info
        for j in cms:
            sbt.append(j)  # concatenate cellm1 info to sib31 info
        listot.append(sbt)
    return listot
