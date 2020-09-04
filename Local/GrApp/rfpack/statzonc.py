def statzon(df):
    from rfpack.zonec import zone
    from rfpack.par_auditc import par_audit

    df = df.copy(deep=True)  # Modifications to the data of the copy wont be reflected in the orig object
    dftemp = df.reset_index(level=(0, 1))
    stzf = []
    n = 10  # zone number
    for i in range(0, n):  # loop for each zone
        area = zone(i)
        dfzi = dftemp[:][dftemp.Prefijo == area]  # data per zone
        if len(dfzi) > 0:  # control for empty df
            if i == 0:
                stzf = par_audit(dfzi)
                stzf['Prefijo'] = area
            else:
                stz = par_audit(dfzi)
                stz['Prefijo'] = area
                if len(stzf) == 0:  # empty stzf control
                    stzf = stz
                else:
                    stzf = stzf.append(stz)
    return stzf
