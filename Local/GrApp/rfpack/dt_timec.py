import math


def decsecs(timestr, nsec):  # ret string with nsec decremented
    timelist = []
    timelst = [int(e) if e.isdecimal() else (float(e)) for e in timestr.split(":")]  # hour to list [hr, m, s]
    timelst.append(int(1000000 * (timelst[2] - math.floor(timelst[2])) + 1))  # micro secs
    timelst[2] = math.floor(timelst[2])  # secs int
    timetst = list(timelst[: 3])  # avoid change in timelst, microsecs discarded
    new_data = ['{:02d}'.format(x) for x in timetst]
    timestr = ':'.join(map(str, new_data))
    timelist.append(timestr)  # appends current time
    for sec in range(nsec-1):
        if timetst[2] - 1 < 0:
            timetst[2] = 59  # avoid negative values
            if timetst[1] == 0:
                timetst[1] = 59
                if timetst[0] == 0:
                    timetst[0] = 23
                else:
                    timetst[0] = timetst[0] -1
            else:
                timetst[1] = timetst[1] -1
        else:
            timetst[2] = timetst[2] - 1
        new_data = ['{:02d}'.format(x) for x in timetst]
        timestr = ':'.join(map(str, new_data))
        timelist.append(timestr)
    return timelist


def comptime(ref, tgt, sbef):  # compares 2 times with sbef shift
    cond = 1
    refl = [int(e) if e.isdecimal() else (float(e)) for e in ref.split(":")]  # hour to list [hr, m, s]
    tgtl = [int(e) if e.isdecimal() else (float(e)) for e in tgt.split(":")]
    if (3600 * refl[0] + 60 * refl[1] + refl[2]) >= (3600 * tgtl[0] + 60 * tgtl[1] + tgtl[2] - sbef):
        cond = 0  # returns 1 if ref < tgt - sbet
    return cond



