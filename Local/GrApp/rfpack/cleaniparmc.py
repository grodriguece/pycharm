def cleaniparm(dat_dir, pfile, dcol, df, st):
    import pandas as pd
    df = df.copy(deep=True)  # Modifications to the data of the copy wont be reflected in the orig object
    df1 = pd.read_csv(dat_dir / pfile, header=0)
    ldcol = df1.loc[:, dcol].dropna()  # list with column dcol without NaN
    df.drop(ldcol, axis=1, inplace=True, errors='ignore')  # delete params list in dataframes
    st.drop(ldcol, axis=0, inplace=True, errors='ignore')
    return df, st


def cleaniparm2(df, st):
    df = df.copy(deep=True)  # Modifications to the data of the copy wont be reflected in the orig object
    n = len(df.index)
    # ldcol = st.loc[]
    df.drop(st[st['StdDev'] == 0].index, axis=1, inplace=True)
    st.drop(st[st['StdDev'] == 0].index, inplace=True)
    df.drop(st[st['NoModeQty'] == 0].index, axis=1, inplace=True)
    st.drop(st[st['NoModeQty'] == 0].index, inplace=True)
    # parameter removal with high null percentage
    df.drop(st[st['NaNQty'] > n * .15].index, axis=1, inplace=True)
    st.drop(st[st['NaNQty'] > n * .15].index, inplace=True)
    st.sort_values(by=['IQR', 'CV'], ascending=False)
    return df, st

