def cleaniparm2(df, st):
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
