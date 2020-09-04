def par_audit(df):
    import functools
    import pandas as pd
    from rfpack.iqrcalcc import iqrcalc

    df = df.copy(deep=True)  # Modifications to the data of the copy wont be reflected in the orig object
    # n = len(df.index)  # row count
    # mode stored in columns
    modes = df.mode(dropna=False)
    # dummy rows delete
    modes = modes.dropna(subset=['Encargado'])
    # dictionaries. data (count values diff from mode in modes) data1 (count of values = mode in modes)
    data = {col: (~df[col].isin(modes[col])).sum() for col in df.iloc[:, 0:].columns}
    data1 = {col: df[col].isin(modes[col]).sum() for col in df.iloc[:, 0:].columns}
    # st3 mode info
    st3 = pd.DataFrame.from_dict(data, orient='index', columns=['NoModeQty'])
    st3['ModeQty'] = pd.DataFrame.from_dict(data1, orient='index')
    st3['NoModePer'] = 100 * (st3['NoModeQty'] / (st3['ModeQty'] + st3['NoModeQty']))
    # st3.index.name = 'parameter'
    st2 = modes.T
    st2.columns = ['Mode']
    # st2.index.name = 'parameter'
    st2 = st2.merge(st3, how='left', left_index=True, right_index=True)
    # st1 = pd.DataFrame({'Vmin': df.min(), 'StdDev': df.std(), 'NaNQty': df.isnull().sum(axis=0), 'Mean': df.mean(),
    #                     'Q1': df.quantile(.25), 'Q3': df.quantile(.75), 'Median': df.quantile(.5)})
    # st1[['Max', 'Min', 'IQR', 'CV']] = st1.apply(lambda row: iqrcalc(row['Q1'], row['Q3'], n, row['StdDev'],
    #                                                                  row['Mean']), axis=1, result_type='expand')
    df2 = df.describe().T
    df2.rename(columns={'25%': 'Q1', '50%': 'Median', '75%': 'Q3', 'std': 'StdDev',
                        'count': 'n', 'min': 'Vmin'}, inplace=True)
    st1 = pd.DataFrame({'NaNQty': df.isnull().sum(axis=0)})
    st1 = df2.merge(st1, how='left', left_index=True, right_index=True)
    st1[['upper', 'lower', 'IQR', 'CV']] = st1.apply(lambda row: iqrcalc(row['Q1'], row['Q3'], row['n'], row['StdDev'],
                                                                         row['mean']), axis=1, result_type='expand')
    st4 = st1.merge(st2, how='left', left_index=True, right_index=True)
    st4.index.name = 'parameter'
    # st1.index.name = 'parameter'
    # df merge
    # dfs = [st1, st2, st3]
    # st4 = functools.reduce(lambda left, right: pd.merge(left, right, on='parameter'), dfs)
    st4.sort_values(by=['IQR', 'CV'], inplace=True, ascending=[False, False])
    return st4
