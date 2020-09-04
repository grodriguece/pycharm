def cleaniparm(dat_dir, pfile, dcol, df, st):
    import pandas as pd
    df1 = pd.read_csv(dat_dir / pfile, header=0)
    ldcol = df1.loc[:, dcol].dropna()  # list with column dcol without NaN
    df.drop(ldcol, axis=1, inplace=True)  # delete params list in dataframes
    st.drop(ldcol, axis=0, inplace=True)
    return df, st
