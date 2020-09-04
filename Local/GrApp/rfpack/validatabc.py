def validatab(datb, pfind, tabexc):
    import pandas as pd
    from pathlib import Path
    import sqlite3

    dat_dir = datb.parent
    output = 'tab_par.csv'  # file for tab_param output
    tex = pd.read_csv(tabexc)  # tables to exclude
    tlstex = list(tex.table_name)  # exclusion tables to a list to compare with query result
    conn = sqlite3.connect(datb)  # database connection
    c = conn.cursor()
    df1 = pd.read_csv(pfind)  # parameters to get tables
    parafind = df1.parameter.tolist() # para to find to a list for query
    try:
        # insert ? times according to parameter amount. Query only for parameters required
        quer = "select * from Fulltabcol WHERE parameter in ({})"
        df = pd.read_sql_query(quer.format(','.join(list('?' * len(parafind)))), conn, params=parafind)
        common = df[~df.table_name.isin(tlstex)]  # common only with default tables
        common.to_csv(dat_dir / output, index=False)
    except sqlite3.Error as error:  # sqlite error handling.
        print('SQLite error: %s' % (' '.join(error.args)))
        feedbk = tk.Label(top, text='SQLite error: %s' % (' '.join(error.args)))
        feedbk.pack()
    c.close()
    conn.close()
